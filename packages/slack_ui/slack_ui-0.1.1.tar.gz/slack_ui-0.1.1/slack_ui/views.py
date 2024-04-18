from typing import List, Optional

from slack_ui.blocks import Block
from slack_ui.domain import BlocksList
from slack_ui.forms import Form


class Message:
    blocks: BlocksList = []

    def slack_view(self) -> List[dict]:
        return self.generate_blocks()

    def add_block(self, block: Block):
        self.blocks.append(block)

    def add_blocks(self, blocks: BlocksList):
        for block in blocks:
            self.add_block(block)

    def generate_blocks(self) -> List[dict]:
        return [b.slack_block() for b in self.blocks]


class Modal(Message):
    title: str
    callback_id: str

    def __init__(self, title: str, callback_id: str) -> None:
        self.callback_id = callback_id
        self.title = title

    def slack_view(self) -> dict:
        return {
            "type": "modal",
            "callback_id": self.callback_id,
            "title": {"type": "plain_text", "text": self.title},
            "blocks": self.generate_blocks(),
            **self.additional_blocks(),
        }

    def additional_blocks(self) -> dict:
        return {}


class FormModal(Modal):
    form: Form
    submit_text: str

    def __init__(
        self,
        title: str,
        callback_id: str,
        form: Form,
        submit_text: Optional[str] = "Submit",
    ) -> None:
        super().__init__(title, callback_id)
        self.submit_text = submit_text
        self.form = form

    def generate_blocks(self) -> List[dict]:
        return self.form.slack_view()

    def additional_blocks(self) -> dict:
        return {"submit": {"type": "plain_text", "text": self.submit_text}}
