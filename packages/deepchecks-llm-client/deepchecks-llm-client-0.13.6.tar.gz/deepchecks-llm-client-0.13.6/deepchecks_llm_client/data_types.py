import enum
from dataclasses import dataclass, field

__all__ = ["Tag", "EnvType", "AnnotationType", "Interaction", "Step", "StepType"]

from datetime import datetime
from typing import Any, Dict, List, Optional, Union

import pytz


class Tag(str, enum.Enum):
    """
    Namespace for useful tags that deepchecks case use
    You can use `dc_client.set_tag()` to pass user tags to deepchecks

    INPUT
        Relevant only for auto_collect=True, should contain the input as the user supply it

    INFORMATION_RETRIEVAL
        Relevant only for auto_collect=True, should contain the "information retrieval" if exist

    USER_ID
        The external user that used the AI model

    USER_INTERACTION_ID
        An unique id the user can set (in the context of a specific version), this id can be used later on
        to annotate the interaction, and also to find similar interactions cross-versions
        if USER_INTERACTION_ID was not supplied by the user, deepchecks will try to capture openai response id
        (i.e. - {"id": <openai unique id>, ...} and will set it as the "user_interaction_id" of the logged interaction
        elsewhere, deepchecks will generate a unique id for the interaction.
    """

    INPUT = "input"
    INFORMATION_RETRIEVAL = "information_retrieval"
    USER_ID = "user_id"
    USER_INTERACTION_ID = "user_interaction_id"


class EnvType(str, enum.Enum):
    PROD = "PROD"
    EVAL = "EVAL"
    PENTEST = "PENTEST"


class AnnotationType(str, enum.Enum):
    GOOD = "good"
    BAD = "bad"
    UNKNOWN = "unknown"


class PropertyColumnType(str, enum.Enum):
    CATEGORICAL = "categorical"
    NUMERIC = "numeric"


@dataclass
class Interaction:
    user_interaction_id: str
    input: str
    information_retrieval: str
    full_prompt: str
    output: str
    topic: str
    output_properties: Dict[str, Any]
    input_properties: Dict[str, Any]
    custom_properties: Dict[str, Any]
    llm_properties: Dict[str, Any]
    llm_properties_reasons: Dict[str, Any]
    created_at: datetime


class StepType(str, enum.Enum):
    LLM = "LLM"
    INFORMATION_RETRIEVAL = "INFORMATION_RETRIEVAL"
    TRANSFORMATION = "TRANSFORMATION"
    FILTER = "FILTER"
    FINE_TUNING = "FINE_TUNING"
    PII_REMOVAL = "PII_REMOVAL"
    UDF = "UDF"


@dataclass
class Step:
    name: str
    type: StepType
    attributes: Dict[str, Any]
    started_at: datetime = field(default_factory=lambda: datetime.now(tz=pytz.UTC))
    annotation: Union[AnnotationType, None] = None
    finished_at: Union[datetime, None] = None
    input: Union[str, None] = None
    output: Union[str, None] = None
    error: Union[str, None] = None

    def to_json(self):
        return {
            "name": self.name,
            "annotation": self.annotation.value
            if self.annotation is not None
            else None,
            "type": self.type.value,
            "attributes": self.attributes,
            "started_at": self.started_at.astimezone().isoformat(),
            "finished_at": self.finished_at.astimezone().isoformat()
            if self.finished_at
            else None,
            "input": self.input,
            "output": self.output,
            "error": self.error,
        }

    @classmethod
    def as_jsonl(cls, steps):
        if steps is None:
            return None
        return [step.to_json() for step in steps]


@dataclass
class LogInteractionType:
    """A dataclass representing an interaction.

    Attributes
    ----------
    input : str
        Input data
    output : str
        Output data
    full_prompt : str, optional
        Full prompt data, defaults to None
    annotation : AnnotationType, optional
        Annotation type of the interaction, defaults to None
    user_interaction_id : str, optional
        Unique identifier of the interaction, defaults to None
    steps : list of Step, optional
        List of steps taken during the interaction, defaults to None
    custom_props : dict, optional
        Additional custom properties, defaults to None
    information_retrieval : str, optional
        Information retrieval, defaults to None
    raw_json_data : dict
        Raw JSON data dictionary
    annotation_reason : str, optional
        Reason for the annotation, defaults to None
    started_at : datetime, optional
        Timestamp the interaction started at, defaults to None
    finished_at : datetime, optional
        Timestamp the interaction finished at, defaults to None
    vuln_type : str, optional
        Type of vulnerability (Only used in case of EnvType.PENTEST and must be sent there), defaults to None
    vuln_trigger_str : str, optional
        Vulnerability trigger string (Only used in case of EnvType.PENTEST and is optional there), defaults to None
    """
    input: str
    output: str
    full_prompt: Optional[str] = None
    annotation: Optional[AnnotationType] = None
    user_interaction_id: Optional[str] = None
    steps: Optional[List[Step]] = None
    custom_props: Optional[Dict[str, Any]] = None
    information_retrieval: Optional[Union[str, list[str]]] = None
    raw_json_data: Dict[str, Any] = None
    annotation_reason: Optional[str] = None
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    vuln_type: Optional[str] = None
    vuln_trigger_str: Optional[str] = None
    topic: Optional[str] = None

    def to_json(self):
        data = {
            "input": self.input,
            "output": self.output,
            "full_prompt": self.full_prompt,
            "information_retrieval": self.information_retrieval \
                if self.information_retrieval is None or isinstance(self.information_retrieval, list) \
                else [self.information_retrieval],
            "annotation": self.annotation.value if self.annotation else None,
            "user_interaction_id": self.user_interaction_id,
            "steps": [step.to_json() for step in self.steps] if self.steps else None,
            "custom_props": self.custom_props,
            "raw_json_data": self.raw_json_data,
            "annotation_reason": self.annotation_reason,
            "vuln_type": self.vuln_type,
            "vuln_trigger_str": self.vuln_trigger_str,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "finished_at": self.finished_at.isoformat() if self.finished_at else None,
            "topic": self.topic,
        }
        return data


@dataclass
class CustomPropertyType:
    display_name: str
    type: PropertyColumnType
    description: str


class ApplicationType(str, enum.Enum):
    QA = "QA"
    CHAT = "CHAT"
    SUMMARIZATION = "SUMMARIZATION"
    GENERATION = "GENERATION"
    CLASSIFICATION = "CLASSIFICATION"


@dataclass
class ApplicationVersionSchema:
    name: str

    def to_json(self):
        return {"name": self.name}
