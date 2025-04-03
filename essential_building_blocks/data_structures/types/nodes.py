"""
essential_building_blocks.data_structures.types.nodes

This module contains the base classes for nodes in linked lists, trees, graphs, and
other data structures.

NodeBase
--------

A base class for nodes in linked lists, trees, graphs, and other data structures. It
provides a `value` attribute and methods for getting and setting the value.

SingleLinkNode
-------------

A single linked list node. It provides a `next` attribute and methods for getting and
setting the next node.

DoubleLinkNode
-------------

A double linked list node. It provides `next` and `prev` attributes and methods for
getting and setting the next and previous nodes.

TreeNode
--------

A tree node. It provides a `key` attribute and methods for getting and setting the key.

BinaryTreeNode
-------------

A binary tree node. It provides `key`, `value`, `left`, and `right` attributes and
methods for getting and setting the key, value, left child, and right child.

"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

@dataclass
class NodeBase(ABC):
    """
    A base class for nodes in linked lists, trees, graphs, and other data structures.
    """

    value: Any

    def get_value(self) -> Any:
        """
        Returns the value of the node.

        Returns:
            Any: The value of the node.
        """
        return self.value

    def set_value(self, value: Any) -> None:
        """
        Sets the value of the node.

        Args:
            value (Any): The value to set.
        """
        self.value = value


class SingleLinkNode(NodeBase):
    """
    A single linked list node.
    """

    def __init__(self, value: Any, next_node: "SingleLinkNode | None" = None):
        super().__init__(value)
        self.next: "SingleLinkNode | None" = next_node

    def get_next(self) -> "SingleLinkNode | None":
        """
        Returns the next node in the linked list.

        Returns:
            SingleLinkNode | None: The next node if it exists, otherwise None.
        """

        return self.next

    def set_next(self, next_node: "SingleLinkNode | None") -> None:
        """
        Sets the next node in the linked list.

        Args:
            next_node (SingleLinkNode | None): The next node if it exists, otherwise None.
        """
        if next_node is not None and not isinstance(next_node, SingleLinkNode):
            raise TypeError("next_node must be a SingleLinkNode")
        self.next = next_node

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


class DoubleLinkNode(NodeBase):
    """
    A double linked list node.
    """

    def __init__(
        self,
        value: Any,
        next_node: "DoubleLinkNode | None" = None,
        prev_node: "DoubleLinkNode | None" = None,
    ):
        super().__init__(value)
        self.next: "DoubleLinkNode | None" = next_node
        self.prev: "DoubleLinkNode | None" = prev_node

    def get_next(self) -> "DoubleLinkNode | None":
        """
        Returns the next node in the linked list.

        Returns:
            DoubleLinkNode | None: The next node if it exists, otherwise None.
        """
        return self.next

    def set_next(self, next_node: "DoubleLinkNode | None") -> None:
        """
        Sets the next node in the double linked list.

        Args:
            next_node (DoubleLinkNode | None): The next node if it exists, otherwise None.

        Raises:
            TypeError: If the next_node is not of type DoubleLinkNode.
        """

        if next_node is not None and not isinstance(next_node, DoubleLinkNode):
            raise TypeError("next_node must be a DoubleLinkNode")
        self.next = next_node

    def get_prev(self) -> "DoubleLinkNode | None":
        """
        Returns the previous node in the double linked list.

        Returns:
            DoubleLinkNode | None: The previous node if it exists, otherwise None.
        """

        return self.prev

    def set_prev(self, prev_node: "DoubleLinkNode | None") -> None:
        """
        Sets the previous node in the double linked list.

        Args:
            prev_node (DoubleLinkNode | None): The previous node if it exists, otherwise None.

        Raises:
            TypeError: If the prev_node is not of type DoubleLinkNode.
        """

        if prev_node is not None and not isinstance(prev_node, DoubleLinkNode):
            raise TypeError("prev_node must be a DoubleLinkNode")
        self.prev = prev_node

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


class AbstractTreeNode(NodeBase):
    """
    An abstract base class for nodes in trees.
    """

    def __init__(self, key: int, value: Any):
        if not isinstance(key, (int, float)):
            raise TypeError("key must be an integer or float")

        super().__init__(value)
        self.key: int = key

    def get_key(self) -> int:
        """
        Returns the key of the node.

        Returns:
            int: The key of the node.
        """
        return self.key

    def set_key(self, key: int) -> None:
        """
        Sets the key of the node.

        Args:
            key (int): The key to set.
        """
        if not isinstance(key, int):
            raise TypeError("key must be an integer")
        self.key = key


class TreeNode(AbstractTreeNode):
    """
    A node in a tree.
    """

    def __init__(
        self,
        key: int,
        value: Any,
        parent: "TreeNode | None" = None,
        children: list["TreeNode"] | None = None,
    ):
        if not isinstance(parent, TreeNode) and parent is not None:
            raise TypeError("parent must be an instance of TreeNode")

        if not isinstance(children, list) and children is not None:
            raise TypeError("children must be a list of TreeNodes or None")

        super().__init__(key, value)
        self.parent: "TreeNode | None" = parent
        self.children: list["TreeNode"] = children if children else []

    def get_parent(self) -> "TreeNode | None":
        """
        Returns the parent of the node.

        Returns:
            TreeNode | None: The parent of the node if it exists, otherwise None.
        """
        return self.parent

    def set_parent(self, parent: "TreeNode | None") -> None:
        """
        Sets the parent of the node.

        Args:
            parent (TreeNode | None): The parent of the node if it exists, otherwise None.

        Raises:
            TypeError: If the parent is not of type TreeNode.
        """

        if parent is not None and not isinstance(parent, TreeNode):
            raise TypeError("parent must be a TreeNode")
        self.parent = parent

    def get_children(self) -> list["TreeNode"]:
        """
        Returns the children of the node.

        Returns:
            list[TreeNode]: The children of the node.
        """
        return self.children

    def add_child(self, child: "TreeNode") -> None:
        """
        Adds a child to the node.

        Args:
            child (TreeNode): The child to add.
        """
        if not isinstance(child, TreeNode):
            raise TypeError("child must be a TreeNode")
        self.children.append(child)

    def remove_child(self, child: "TreeNode") -> None:
        """
        Removes a child from the node.

        Args:
            child (TreeNode): The child to remove.
        """
        if not isinstance(child, TreeNode):
            raise TypeError("child must be a TreeNode")
        self.children.remove(child)

    def get_children_count(self) -> int:
        """
        Returns the number of children of the node.

        Returns:
            int: The number of children of the node.
        """
        return len(self.children)

    def to_dict(self) -> dict:
        """
        Converts the node to a dictionary.

        Returns:
            dict: A dictionary representation of the node.
        """
        return {
            "key": self.key,
            "value": self.value,
            "parent": self.parent.key if self.parent is not None else None,
            "children": [child.key for child in self.children],
        }

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self)


class BinaryTreeNode(AbstractTreeNode):
    """
    A node in a binary tree.
    """

    def __init__(
        self,
        key: int,
        value: Any,
        parent: "BinaryTreeNode | None" = None,
        left: "BinaryTreeNode | None" = None,
        right: "BinaryTreeNode | None" = None,
    ):
        if not isinstance(parent, BinaryTreeNode) and parent is not None:
            raise TypeError("parent must be an instance of BinaryTreeNode")

        if not isinstance(left, BinaryTreeNode) and left is not None:
            raise TypeError("left must be an instance of BinaryTreeNode or None")

        if not isinstance(right, BinaryTreeNode) and right is not None:
            raise TypeError("right must be an instance of BinaryTreeNode or None")

        super().__init__(key, value)
        self.parent: "BinaryTreeNode | None" = parent
        self.left: "BinaryTreeNode | None" = left
        self.right: "BinaryTreeNode | None" = right

    def to_dict(self) -> dict:
        """
        Converts the node to a dictionary.

        Returns:
            dict: The dictionary with keys "key", "value", "parent", "left", and "right".
        """
        return {
            "key": self.key,
            "value": self.value,
            "parent": self.parent.key if self.parent else None,
            "left": self.left.key if self.left else None,
            "right": self.right.key if self.right else None,
        }

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self)
