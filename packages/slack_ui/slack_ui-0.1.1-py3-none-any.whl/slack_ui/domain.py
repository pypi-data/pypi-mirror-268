from __future__ import annotations

from typing import List, Union

from slack_ui.blocks import Block

BlocksList = List[Block]
DeeperBlocksList = List[Union[Block, BlocksList]]
DeepBlocksList = List[Union[Block, DeeperBlocksList]]
