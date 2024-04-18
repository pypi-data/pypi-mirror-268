import json
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Literal, Optional


class Block(ABC):
    """Abstract base class representing a Slack block.

    This class defines the interface for all Slack blocks.

    Methods:
        slack_block: Abstract method that returns a dict representing the Slack block.
    """
    @abstractmethod
    def slack_block(self) -> dict:
        pass


class Element(Block, ABC):
    pass


class Button(Element):
    style: Optional[Literal["primary", "danger"]]
    action_id: str
    value: Any
    text: str

    def __init__(
        self,
        action_id: str,
        text: str,
        value: Any,
        style: Optional[Literal["primary", "danger"]] = None,
    ):
        assert style in [None, "primary", "danger"]

        self.action_id = action_id
        self.value = value
        self.style = style
        self.text = text

    def slack_block(self) -> dict:
        return {
            "type": "button",
            "text": {"type": "plain_text", "text": self.text},
            "value": json.dumps(self.value),
            "action_id": self.action_id,
            **({"style": self.style} if self.style else {}),
        }


class ActionsBlock(Block):
    elements: List[Element]

    def __init__(self, elements: Optional[List[Element]] = None):
        self.elements = elements if elements else None

    def slack_block(self) -> dict:
        return {
            "type": "actions",
            "elements": [element.slack_block() for element in self.elements],
        }


class HeaderBlock(Block):
    text: str

    def __init__(self, text: str) -> None:
        assert (
            len(text) <= 150
        ), "[Header Block] Text can't be longer then 150 characters"

        self.text = text

    def slack_block(self) -> dict:
        return {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": self.text,
            },
        }


class TextBlock(Block):
    text: str

    def __init__(self, text: str) -> None:
        assert (
            len(text) <= 3000
        ), "[Text Block] Text can't be longer then 3000 characters"

        self.text = text

    def slack_block(self) -> dict:
        return {
            "type": "section",
            "text": self.slack_field(),
        }

    def slack_field(self) -> Dict[str, str]:
        return {"type": "mrkdwn", "text": self.text}

    def __str__(self):
        return f"TextBlock({self.text})"


class SectionBlock(Block):
    fields: List[str] = []
    text: Optional[str]

    def __init__(self, text: Optional[str], fields: Optional[List[str]] = None) -> None:
        assert (
            text is None or len(text) <= 3000
        ), "[Section Block] Text can't be longer then 3000 characters"
        assert (
            max(len(s) for s in fields) <= 2000
        ), "[Section Block] No one text in fields can't be longer then 2000 characters"
        assert len(fields) <= 10, "[Section Block] Max number of fields is 10"

        self.fields = fields if fields is not None else []
        self.text = text

    def slack_block(self) -> dict:
        return {
            "type": "section",
            **({"text": {"type": "mrkdwn", "text": self.text}} if self.text else {}),
            **(
                {"fields": [{"type": "mrkdwn", "text": field} for field in self.fields]}
                if len(self.fields)
                else {}
            ),
        }


class ContextBlock(Block):
    context: List[TextBlock]

    def __init__(self, context: List[TextBlock]) -> None:
        assert len(context) <= 10, "[Context Block] Max number of fields is 10"

        self.context = context

    def slack_block(self) -> dict:
        return {
            "type": "context",
            "elements": [field.slack_field() for field in self.context],
        }


class DividerBlock(Block):
    def slack_block(self) -> dict:
        return {"type": "divider"}
