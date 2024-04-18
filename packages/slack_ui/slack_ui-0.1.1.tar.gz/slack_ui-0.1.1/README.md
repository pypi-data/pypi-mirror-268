# Python's Slack Blocks Builder

The **Slack Bot** ([Slack Bolt](https://slack.dev/bolt-python/concepts)) lacks a user-friendly 
way to utilize [Slack Blocks](https://api.slack.com/block-kit) out of the box. 
But, using this library will afford you the convenience you need to construct fancy 
messages on Slack without having to resort to using dictionaries.

Support for Forms - package allow you to easier create a form ([more details](#Forms)). 

## Getting Started

You can install this library using your preferred package manager:

* For **Poetry**: `poetry add slack_ui`
* For **PIP**: `pip install slack_ui`

Now, you can use kit e.g.:

```python
import slack_ui

message = slack_ui.views.Message()

message.add_blocks(
    [
        slack_ui.HeaderBlock(":bar_chart: Summary of Week"),
        slack_ui.DividerBlock(),
        slack_ui.TextBlock(
            "What happened at this week?\n"
            "What is Top 10 of cats?"
        ),
    ]
)

message.add_block(
    slack_ui.ContextBlock(
        [
            slack_ui.TextBlock("col 1"),
            slack_ui.TextBlock("col 2"),
            slack_ui.TextBlock("col 2"),
        ]
    )
)

bot_app.client.chat_postMessage(
    ..., 
    blocks=message.slack_view(),
)

```

## Blocks 

| Name           | Parameters                                               | Docs reference                                                   | Note                               |
|----------------|----------------------------------------------------------|------------------------------------------------------------------|------------------------------------|
| `HeaderBlock`  | `text: str`                                              | [docs](https://api.slack.com/reference/block-kit/blocks#header)  | support for emoji                  |
| `TextBlock`    | `text: str`                                              | [docs](https://api.slack.com/reference/block-kit/blocks#header)  | support for emoji and markdown     |
| `ContextBlock` | `context: List[TextBlock]`                               | [docs](https://api.slack.com/reference/block-kit/blocks#context) | columns divided                    |
| `SectionBlock` | `text: Optional[str]` <br> `fields: Optional[List[str]]` | [docs](https://api.slack.com/reference/block-kit/blocks#section) |                                    |
| `DividerBlock` |                                                          | [docs](https://api.slack.com/reference/block-kit/blocks#divider) | divided line similar to hr in html |

## Forms

You can defined class which will be converted to slack form view. \
Class have to inheritance class `Form` and define a `slack_blocks.forms.Field`.

### Example:

```python
import slack_ui

class HolidayKind(slack_ui.forms.SelectFormEnum):
    HOLIDAYS = "holidays_leave", "Resting"
    SICK = "sick_leave", "Sick"


class HolidayRequestForm(slack_ui.forms.Form):
    start_at = slack_ui.forms.DateField(label="Date start")
    end_at = slack_ui.forms.DateField(label="Date end")
    kind_of = slack_ui.forms.StaticSelectField(
        label="Kind of", 
        options=HolidayKind,
    )

def handle_holidays_request(ack, shortcut, client, body):
    """Handle button action and show form modal"""
    
    form = HolidayRequestForm()
    form_modal = slack_ui.views.FormModal(
        "Holidays request",  # Title of form modal
        "callback_id",  # id of defined callback action 
        form
    )
    
    (...)
    client.views_open(
        trigger_id=body["trigger_id"], 
        view=form_modal.slack_view(),
    )
    (...)
```

### Form Inputs 

| Name                | Attributes                                                                                      | Note                                     |
|---------------------|-------------------------------------------------------------------------------------------------|------------------------------------------|
| `TextField`         | `label: str`                                                                                    | Text field, ask user for some text input |
| `DateField`         | `label: str`<br/>`initial_date: Optional[date] = None`<br/>`placeholder: str = "Select a date"` | Date fields, ask user for date           |
| `StaticSelectField` | `label: str`<br/> `options=None`<br/> `placeholder: str = "Select an item"`                     | Select field, ask user for choose option |

## Views

Package provide views: Modal, FormModal, Message. \
You can use each after import `from slack_blocks.views import Message, Modal, FormModal`.

### Message

Simple type, message is common unit in this kit. \
When you want to send message = use message. 

#### example:
```python
import slack_ui

message = slack_ui.views.Message()
message.add_blocks(
    [
        slack_ui.HeaderBlock(":bar_chart: Summary of Week"),
        slack_ui.TextBlock("What happened at this week?"),
    ]
)
message.slack_view()
```

### Modal

[Slack bolt documentation "Opening modals"](https://slack.dev/bolt-python/concepts#opening-modals)

> Modals are focused surfaces that allow you to collect user data and display dynamic information. \
> You can open a modal by passing a valid `trigger_id` and a view payload to the built-in client’s `views.open` method. 

#### example:
```python
from slack_ui.views import Modal
import slack_ui 

modal = Modal("Modal title", "callback_id_0001")
modal.add_block(slack_ui.TextBlock("Some text"))
modal.slack_view()
```

### FormModal

This is specified type of modal where inside is generated a form view. \
The form have to be instance of class base on `slack_blocks.forms.Form`

#### example:
```python
from slack_ui.views import FormModal

form = DefinedForm()

modal = FormModal("Modal title", "callback_id_0001", form)
modal.slack_view()
```
