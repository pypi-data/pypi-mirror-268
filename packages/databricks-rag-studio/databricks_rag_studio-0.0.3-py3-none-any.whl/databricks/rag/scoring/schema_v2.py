from __future__ import annotations

import json
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional


class StatusCode(str, Enum):
    OK = "OK"
    ERROR = "ERROR"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Status:
    """
    Status of the trace or span.
    """

    status_code: StatusCode
    description: str = ""

    def json(self) -> Dict[str, str]:
        return {
            "status_code": str(self.status_code),
            "description": self.description,
        }


class SpanType(str, Enum):
    """
    Default enum of span types
    """

    LLM = "LLM"
    CHAIN = "CHAIN"
    AGENT = "AGENT"
    TOOL = "TOOL"
    CHAT_MODEL = "CHAT_MODEL"
    RETRIEVER = "RETRIEVER"
    EMBEDDING = "EMBEDDING"
    RERANKER = "RERANKER"
    PARSER = "PARSER"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)


def _dump_dictionary(d: Optional[Dict[str, Any]]) -> Optional[str]:
    if d is None:
        return None
    return json.dumps(d, cls=CustomEncoder)


@dataclass
class Span:
    """
    Span object.
    """

    name: str
    context: SpanContext
    status: Status
    span_type: str = SpanType.UNKNOWN.value
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    parent_span_id: Optional[str] = None
    inputs: Optional[Dict[str, Any]] = None
    outputs: Optional[Dict[str, Any]] = None
    attributes: Optional[Dict[str, Any]] = None
    events: Optional[List[Event]] = None

    def json(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "context": asdict(self.context),
            "status": self.status.json(),
            "span_type": str(self.span_type),
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "parent_span_id": self.parent_span_id,
            "inputs": _dump_dictionary(self.inputs),
            "outputs": _dump_dictionary(self.outputs),
            "attributes": _dump_dictionary(self.attributes),
            "events": (
                [event.json() for event in self.events] if self.events else None
            ),
        }


@dataclass
class SpanContext:
    request_id: str = ""
    span_id: str = field(default_factory=lambda: str(uuid.uuid4()))


@dataclass
class Event:
    name: str
    timestamp: datetime
    attributes: Optional[Dict[str, Any]] = None

    def json(self):
        return {
            "name": self.name,
            "timestamp": self.timestamp.isoformat(),
            "attributes": _dump_dictionary(self.attributes),
        }


class CustomEncoder(json.JSONEncoder):
    """
    Custom encoder to handle json serialization.
    """

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, uuid.UUID):
            return str(o)
        try:
            return super().default(o)
        # temp solution to avoid error in serialization
        except TypeError:
            return str(o)
