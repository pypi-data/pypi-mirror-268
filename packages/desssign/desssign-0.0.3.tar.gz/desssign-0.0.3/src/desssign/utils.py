from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


def flatten_list(mixed_list: tuple[Any] | list[Any]) -> list[Any]:
    """
    Flatten a list containing nested lists into a single list with all the elements.

    Iterates through the input list and extends the output list with the elements of any inner
    lists found. Non-list items are appended directly to the output list.

    :param mixed_list: A list potentially containing nested lists along with other items.
    :return: A single, flattened list containing all elements from the input, preserving order.
    """
    flat_list = []
    for item in mixed_list:
        if isinstance(item, (list, tuple)):  # Check if the item is a list or tuple
            flat_list.extend(flatten_list(item))  # Recursively flatten and extend
        else:
            flat_list.append(item)  # Append the item directly if it's not a list
    return flat_list
