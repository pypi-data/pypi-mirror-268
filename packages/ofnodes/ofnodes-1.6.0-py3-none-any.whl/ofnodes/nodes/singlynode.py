"""Defines a node for a singly linked list.

This module contains the definition for the `SinglyNode` class, which represents
a node in a singly linked list. Each node contains data and a reference to the
next node in the list.

Example:
    Typical usage example:

        uni_node = SinglyNode("a string of characters")
"""

from typing import Any, Optional


class SinglyNode:
    """Represents a node in a singly linked list.

    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the linked list. Defaults to None.
    """

    __slots__ = ('_data', '_next')

    def __init__(self, data: Any) -> None:
        self._data: Optional[Any] = data
        self._next: Optional[SinglyNode] = None

    def __dir__(self) -> list[str]:
        # Get the list of attributes and methods from the parent classes
        parent_dir = set(super().__dir__())
        # Filter out private attributes and methods
        parent_dir = {attr for attr in parent_dir if attr not in {'_data', '_next',}}
        # Return a sorted list of all attributes and methods
        return sorted(parent_dir)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if value: #  TODO: perform data validation
            validated_data = value
        setattr(self, '_data', validated_data)

    @data.deleter
    def data(self):
        """Deleter property for the data attribute of the singly node.

        Raises:
            AttributeError: Deleting the `head` attribute is not allowed.
        """
        raise AttributeError(
            f"{type(self).__name__}'s `data` attribute " "cannot be deleted."
        )

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        raise AttributeError("Cannot set 'next' attribute directly. Use linked list methods for modification.")

    @next.deleter
    def next(self):
        """Deleter property for the next attribute of the singly node.

        Raises:
            AttributeError: Deleting the `next` attribute is not allowed.
        """
        raise AttributeError(
            f"{type(self).__name__}'s `next` attribute " "cannot be deleted."
        )

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}"
            "("
            f"data={repr(self.data)}"
            ")"
        )

    def __str__(self) -> str:
        return str(self.data)
