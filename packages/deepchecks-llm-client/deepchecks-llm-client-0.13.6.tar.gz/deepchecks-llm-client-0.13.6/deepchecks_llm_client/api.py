import logging
import typing as t
from copy import copy

import deepchecks_llm_client
import httpx
import packaging.version
from deepchecks_llm_client.data_types import (
    AnnotationType,
    ApplicationType,
    ApplicationVersionSchema,
    EnvType,
    LogInteractionType,
    PropertyColumnType,
    Step,
    Tag,
)
from deepchecks_llm_client.utils import maybe_raise
from httpx import URL

__all__ = ["API"]

logger = logging.getLogger(__name__)

TAPI = t.TypeVar("TAPI", bound="API")  # pylint: disable=invalid-name
MAX_TOPIC_LENGTH = 40


def _check_topic(topic: t.Union[str, None]):
    """Check topic length and log warning that topic must not be more than 40 characters long."""
    if topic and len(topic) > MAX_TOPIC_LENGTH:
        logger.warning(f"Topic {topic} is too long and will be truncated to {MAX_TOPIC_LENGTH} during interaction upload")


class API:
    session: httpx.Client
    original_host: URL

    @classmethod
    def instantiate(cls: t.Type[TAPI],
                    host: str,
                    token: t.Optional[str] = None,
                    validate_connection: bool = False) -> TAPI:
        headers = (
            {"Authorization": f"Basic {token}", "x-deepchecks-origin": "SDK"}
            if token
            else {"x-deepchecks-origin": "SDK"}
        )
        return cls(
            session=httpx.Client(
                base_url=host,
                headers=headers,
                timeout=60
            ),
            validate_connection=validate_connection
        )

    def __init__(self, session: httpx.Client, validate_connection: bool = False):
        self.session = copy(session)
        self.original_host = self.session.base_url
        self.session.base_url = self.session.base_url.join("/api/v1")
        self._app_name: str = None
        self._version_name: str = None
        self._env_type: EnvType = None
        self._tags: t.Dict[Tag, str] = {}

        try:
            backend_version = packaging.version.parse(self.retrieve_backend_version())
            client_version = packaging.version.parse(deepchecks_llm_client.__version__)
        except packaging.version.InvalidVersion as ex:
            raise RuntimeError("Not able to compare backend and client versions, "
                               "backend or client use incorrect or legacy versioning schema.") from ex
        except httpx.ConnectError as ex:
            logger.exception(f"Could not connect to backend {self.original_host}, either the server is down or "
                             f"you are using an incorrect host name")
            if validate_connection:
                raise ex

        else:
            if backend_version.major != client_version.major:
                logger.warning(
                    f"You are using an old client version.\n"
                    f"Client version is {client_version}, Backend version is {backend_version}\n"
                    f"We recommend you to upgrade \"deepchecks-llm-client\" version by running:\n"
                    f">> pip install -U deepchecks-llm-client"
                )

    @property
    def app_name(self) -> str:
        return self._app_name

    @app_name.setter
    def app_name(self, new_app_name: str):
        if new_app_name is None:
            raise ValueError("new_app_name cannot be set to None")
        self._app_name = new_app_name

    @property
    def version_name(self):
        return self._version_name

    @version_name.setter
    def version_name(self, new_version_name: str):
        if new_version_name is None:
            raise ValueError("new_version_name cannot be set to None")
        self._version_name = new_version_name

    @property
    def env_type(self):
        return self._env_type

    @env_type.setter
    def env_type(self, new_env_type: EnvType):
        if new_env_type is None:
            raise ValueError("new_env_type cannot be set to None")
        if new_env_type not in (EnvType.PROD, EnvType.EVAL, EnvType.PENTEST):
            raise ValueError("new_env_type must be one of: EnvType.PROD or EnvType.EVAL or EnvType.PENTEST")

        self._env_type = new_env_type

    def set_tags(self, tags: t.Dict[Tag, str]):
        if tags is None:
            self._tags = {}
        else:
            self._tags = tags

    def retrieve_backend_version(self) -> str:
        payload = maybe_raise(self.session.get("backend-version")).json()
        return payload["version"]

    def get_application(self, app_name: t.Union[str, None] = None) -> t.Dict[str, t.Any]:
        if app_name is None:
            app_name = self._app_name
        payload = maybe_raise(self.session.get("applications", params={"name": [app_name]})).json()
        return payload[0] if len(payload) > 0 else None

    def create_application_version(self, application_id: int, version_name: str):
        return maybe_raise(
            self.session.post(
                "application-versions",
                json={"application_id": application_id, "name": version_name},
            )
        ).json()

    def create_application(
            self,
            application_name: str,
            app_type: ApplicationType,
            versions: t.Optional[t.List[ApplicationVersionSchema]] = None,
            description: t.Optional[str] = None,
    ):
        return maybe_raise(
            self.session.post(
                "applications",
                json={
                    "name": application_name,
                    "kind": app_type,
                    "versions": [version.to_json() for version in versions] if versions else [],
                    "description": description,
                },
            )
        ).json()

    def load_openai_data(self, data: t.List[t.Dict[str, t.Any]]) -> t.Optional[httpx.Response]:
        if Tag.INPUT not in self._tags:
            logger.warning(
                "OpenAI latest input message will be used as input data. "
                "Set input data manually as tag (Tag.INPUT) to set your exact input"
            )

        for row in data:
            row["user_data"] = self._tags

        return maybe_raise(
            self.session.post(
                "openai-load",
                json=data,
                params={
                    "app_name": self._app_name,
                    "version_name": self._version_name,
                    "env_type": self._env_type.value
                }
            )
        )

    def annotate(self,
                 user_interaction_id: str,
                 version_id: int,
                 annotation: AnnotationType = None,
                 reason: t.Optional[str] = None) \
            -> t.Optional[httpx.Response]:
        # pylint: disable=redefined-builtin
        return maybe_raise(self.session.put("annotations", json={"user_interaction_id": user_interaction_id,
                                                                 "application_version_id": version_id,
                                                                 "value": annotation.value,
                                                                 "reason": reason}))

    def update_interaction(
            self,
            user_interaction_id: str,
            app_version_id: int,
            annotation: AnnotationType = None,
            annotation_reason: t.Optional[str] = None,
            custom_props: t.Union[t.Dict[str, t.Any], None] = None,
    ) -> t.Optional[httpx.Response]:
        return maybe_raise(
            self.session.put(
                f"application_versions/{app_version_id}/interactions/{user_interaction_id}",
                json={"custom_properties": custom_props, "annotation": annotation, "annotation_reason": annotation_reason},
            )
        )

    def delete_interactions(self, user_interaction_ids: t.List[str], app_version_id: int):
        return maybe_raise(
            self.session.request(
                method="DELETE",
                url="interactions",
                params={"application_version_id": app_version_id},
                json=user_interaction_ids,
            )
        )

    def log_batch(self, interactions: t.List[LogInteractionType]):
        for interaction in interactions:
            interaction.raw_json_data = self._tags
            _check_topic(interaction.topic)

        return maybe_raise(
            self.session.post(
                "interactions",
                json={
                    "app_name": self._app_name,
                    "version_name": self._version_name,
                    "env_type": self._env_type.value,
                    "interactions": [interaction.to_json() for interaction in interactions],
                },
            ),
            expected=201,
        )

    def log_interaction(self,
                        input: str,
                        output: str,
                        full_prompt: str,
                        information_retrieval: t.Union[list[str], str],
                        annotation: AnnotationType,
                        user_interaction_id: str,
                        started_at: str,
                        finished_at: str,
                        steps: t.List[Step],
                        custom_props: t.Dict[str, t.Any],
                        annotation_reason: t.Optional[str] = None,
                        vuln_type: t.Optional[str] = None,
                        vuln_trigger_str: t.Optional[str] = None,
                        topic: t.Optional[str] = None,
                        ) -> t.Optional[httpx.Response]:
        """The log_interaction method is used to log user interactions.

        Parameters
        ----------
        input : str
            Input data
        output : str
            Output data
        full_prompt : str
            Full prompt data
        information_retrieval : str
            Information retrieval
        annotation : AnnotationType
            Annotation type of the interaction
        user_interaction_id : str
            Unique identifier of the interaction
        started_at : datetime
            Timestamp the interaction started at
        finished_at : datetime
            Timestamp the interaction finished at
        steps : list of Step
            List of steps taken during the interaction
        custom_props : dict
            Additional custom properties
        annotation_reason : str, optional
            Reason for the annotation
        vuln_type : str, optional
            Type of vulnerability (Only used in case of EnvType.PENTEST and must be sent there).
        vuln_trigger_str : str, optional
            Vulnerability trigger string (Only used in case of EnvType.PENTEST and is optional there).
        topic: str, optional
            Topic associated with the interaction. Topic longer than 40 characters will be truncated
        Returns
        -------
        httpx.Response
            The HTTP response from logging the user interaction

        """
        # pylint: disable=redefined-builtin
        interaction = {
            "user_interaction_id": user_interaction_id,
            "input": input,
            "output": output,
            "full_prompt": full_prompt,
            "information_retrieval": information_retrieval \
                if information_retrieval is None or isinstance(information_retrieval, list) \
                else [information_retrieval],
            "annotation": annotation.value if annotation else None,
            "annotation_reason": annotation_reason,
            "raw_json_data": {"user_data": self._tags},
            "steps": Step.as_jsonl(steps),
            "custom_props": custom_props,
            "vuln_type": vuln_type,
            "vuln_trigger_str": vuln_trigger_str,
            "topic": topic,
        }
        _check_topic(topic)
        if started_at:
            interaction["started_at"] = started_at

        if finished_at:
            interaction["finished_at"] = finished_at

        return maybe_raise(
            self.session.post(
                "interactions",
                json={"env_type": self._env_type,
                      "app_name": self._app_name,
                      "version_name": self._version_name,
                      "interactions": [interaction]}
            ),
            expected=201
        )

    def get_interactions(self, application_version_id: int,
                         limit: int, offset: int,
                         environment: t.Union[EnvType, str],
                         start_time_epoch: t.Union[int, None],
                         end_time_epoch: t.Union[int, None],
                         user_interaction_ids: t.Union[t.List[str], None] = None) -> t.List:
        return maybe_raise(
            self.session.post("get-interactions-by-filter",
                              json={
                                  "application_version_id": application_version_id,
                                  "environment": environment.value if isinstance(environment, EnvType) else environment,
                                  "limit": limit,
                                  "offset": offset,
                                  "start_time_epoch": start_time_epoch,
                                  "end_time_epoch": end_time_epoch,
                                  "user_interaction_ids": user_interaction_ids,
                              }, params={"return_topics": True, "return_input_props": False})
        ).json()

    def get_interactions_csv(
            self,
            application_version_id: int,
            return_topics: bool,
            return_annotation_data: bool,
            return_input_props: bool,
            return_output_props: bool,
            return_custom_props: bool,
            return_llm_props: bool,
            return_similarities: bool,
            environment: t.Union[EnvType, str],
            start_time_epoch: t.Union[int, None],
            end_time_epoch: t.Union[int, None],
            user_interaction_ids: t.Union[t.List[str], None] = None,
    ) -> str:
        return maybe_raise(
            self.session.post(
                "interactions-download-all-by-filter",
                json={
                    "application_version_id": application_version_id,
                    "environment": environment.value if isinstance(environment, EnvType) else environment,
                    "start_time_epoch": start_time_epoch,
                    "end_time_epoch": end_time_epoch,
                    "user_interaction_ids": user_interaction_ids,
                },
                params={"return_topics": return_topics,
                        "return_input_props": return_input_props,
                        "return_output_props": return_output_props,
                        "return_custom_props": return_custom_props,
                        "return_llm_props": return_llm_props,
                        "return_annotation_data": return_annotation_data,
                        "return_similarities": return_similarities,
                        }
            )
        ).text

    def get_interaction_by_user_interaction_id(self, version_id: int, user_interaction_id: str):
        return maybe_raise(self.session.get(
            f"application_versions/{version_id}/interactions/{user_interaction_id}"
        )).json()

    def update_application_config(self, application_id: int, file):
        if isinstance(file, str):
            with open(file, "rb") as f:
                data = {"file": ("filename", f)}
        else:
            data = {"file": ("filename", file)}
        maybe_raise(self.session.put(f"applications/{application_id}/config", files=data))

    def get_application_config(self, application_id: int, file_save_path: t.Union[str, None] = None) -> str:
        text = maybe_raise(self.session.get(f"applications/{application_id}/config")).text
        if file_save_path:
            with open(file_save_path, "w", encoding="utf-8") as f:
                f.write(text)
        return text

    def get_pentest_prompts(
            self,
            app_id: int,
            probes: t.Optional[list[str]] = None,
    ) -> str:
        if probes:
            return maybe_raise(self.session.get("pentest-prompts", params={"probes": probes, "app_id": app_id})).text
        return maybe_raise(self.session.get("pentest-prompts", params={"app_id": app_id})).text

    def get_custom_properties_definitions(self, application_id: int) -> list[dict]:
        return maybe_raise(self.session.get(f"applications/{application_id}/custom-prop-definitions")).json()

    def update_custom_property_definition(self, application_id: int, old_name: str, new_name: str, description: str) -> None:
        return maybe_raise(
            self.session.put(
                f"applications/{application_id}/custom-prop-definitions",
                json=[{"old_name": old_name, "new_name": new_name, "description": description}]
            )
        )

    def create_custom_property_definition(self, application_id: int, name: str, prop_type: PropertyColumnType, description: str = "") -> None:
        return maybe_raise(
            self.session.post(
                f"applications/{application_id}/custom-prop-definitions",
                json=[{"display_name": name, "type": prop_type.value, "description": description}]
            )
        )

    def delete_custom_property_definition(self, application_id: int, name: str):
        return maybe_raise(
            self.session.delete(
                f"applications/{application_id}/custom-prop-definitions",
                params={"prop_names_to_delete": [name]}
            )
        )
