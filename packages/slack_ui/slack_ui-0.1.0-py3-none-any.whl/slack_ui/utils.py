from __future__ import annotations

from slack_ui.blocks import Block
from slack_ui.domain import BlocksList, DeepBlocksList


def flat_blocks_list(*blocks_list: Block | DeepBlocksList) -> BlocksList:
    """
    Flatten a list of blocks and deep blocks lists into a single list.

    :param blocks_list: A variable number of Block or DeepBlocksList objects.
    :type blocks_list: tuple[Block | DeepBlocksList]

    :return: A list containing all the blocks in the input, flattened.
    :rtype: list[Block]
    """
    result: BlocksList = []

    for block in blocks_list:
        if isinstance(block, Block):
            result.append(block)
        elif isinstance(block, (list, tuple)):
            result.extend(flat_blocks_list(*block))

    return result
