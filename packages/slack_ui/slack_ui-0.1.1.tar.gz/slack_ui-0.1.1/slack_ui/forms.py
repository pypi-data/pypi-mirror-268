# fields
from abc import ABC
from datetime import date
from enum import Enum
from typing import Dict, List, Optional, Union

from slack_ui.blocks import Block


class Field(Block, ABC):
    name: str
    label: str

    def __init__(self, label: str):
        self.label = label

    @property
    def action_id(self) -> str:
        return "%(name)s-action" % {"name": self.name}


class TextField(Field):
    def slack_block(self) -> dict:
        return {
            "type": "input",
            "element": {
                "type": "plain_text_input",
                "action_id": self.action_id,
            },
            "label": {"type": "plain_text", "text": self.label, "emoji": True},
        }


class SelectFormEnum(Enum):
    @classmethod
    def get_select_options(cls):
        return {a.key: a.label for a in cls}

    @property
    def key(self):
        try:
            return self.value[0] if self.is_enumerated else self.value
        except (KeyError, AttributeError, IndexError):
            return self.name

    @property
    def label(self):
        try:
            return self.value[1] if self.is_enumerated else self.value
        except (KeyError, AttributeError, IndexError):
            return self.name

    @property
    def is_enumerated(self) -> bool:
        return isinstance(self.value, (tuple, list))


class StaticSelectField(Field):
    options: Union[Dict[str, str], SelectFormEnum] = {}
    placeholder: str = "Select an item"

    def __init__(self, label: str, options=None, placeholder: str = "Select an item"):
        super().__init__(label)
        self.options = options if options else {}
        self.placeholder = placeholder

    def slack_block(self) -> dict:
        return {
            "type": "input",
            "element": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": self.placeholder,
                    "emoji": True,
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": self.get_options()[key],
                            "emoji": True,
                        },
                        "value": key,
                    }
                    for key in self.get_options()
                ],
                "action_id": self.action_id,
            },
            "label": {"type": "plain_text", "text": self.label, "emoji": True},
        }

    def get_options(self) -> dict:
        # noinspection PyTypeChecker
        return (
            self.options.get_select_options()
            if issubclass(self.options, SelectFormEnum)
            else self.options
        )


class DateField(Field):
    initial_date: Optional[date] = None
    placeholder: str = "Select a date"

    def __init__(
        self,
        label: str,
        initial_date: Optional[date] = None,
        placeholder: str = "Select a date",
    ):
        super().__init__(label)
        self.initial_date = initial_date if initial_date else None
        self.placeholder = placeholder

    def slack_block(self) -> dict:
        return {
            "type": "input",
            "element": {
                "type": "datepicker",
                "placeholder": {
                    "type": "plain_text",
                    "text": self.placeholder,
                    "emoji": True,
                },
                "action_id": self.action_id,
                **(
                    {"initial_date": self.initial_date.strftime("%Y-%m-%d")}
                    if self.initial_date
                    else {}
                ),
            },
            "label": {"type": "plain_text", "text": self.label, "emoji": True},
        }


class FormMetadata(type):
    def __new__(mcs, name, bases, attrs):
        # Collect fields from current class and remove them from attrs.
        attrs["declared_fields"] = {
            key: attrs.pop(key)
            for key, value in list(attrs.items())
            if isinstance(value, Field)
        }

        new_class = super().__new__(mcs, name, bases, attrs)

        # Walk through the MRO.
        declared_fields = {}
        for base in reversed(new_class.__mro__):
            # Collect fields from base class.
            if hasattr(base, "declared_fields"):
                declared_fields.update(base.declared_fields)

            # Field shadowing.
            for attr, value in base.__dict__.items():
                if value is None and attr in declared_fields:
                    declared_fields.pop(attr)

        new_class.base_fields = declared_fields
        new_class.declared_fields = declared_fields

        return new_class


class Form(metaclass=FormMetadata):
    def get_fields(self) -> List[Field]:
        fields: List[Field] = []
        for field_name in self.declared_fields:
            field = self.declared_fields[field_name]
            field.name = field_name
            fields.append(field)
        return fields

    def slack_view(self) -> List[Dict]:
        return [field.slack_block() for field in self.get_fields()]
