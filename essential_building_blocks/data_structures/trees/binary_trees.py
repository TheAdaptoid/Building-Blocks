from abc import abstractmethod
from essential_building_blocks.data_structures.types.nodes import BinaryTreeNode
from essential_building_blocks.data_structures.lists import Queue


class BinaryTree:
    """
    An abstract class representing a binary tree.
    """

    def __init__(self, root: BinaryTreeNode | None = None):
        if not isinstance(root, BinaryTreeNode) and root is not None:
            raise TypeError("root must be an instance of BinaryTreeNode or None")

        self.root: BinaryTreeNode | None = root

    def is_empty(self) -> bool:
        """
        Checks if the binary tree is empty.

        Returns:
            bool: True if the tree is empty, False otherwise.
        """
        return self.size() == 0

    def size(self) -> int:
        """
        Calculates the number of nodes in the binary tree.

        Returns:
            int: The total number of nodes in the tree.
        """
        if self.root is None:
            return 0

        size = 0
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            size += 1

            if node.left is not None:
                queue.enqueue(node.left)

            if node.right is not None:
                queue.enqueue(node.right)

        return size

    def height(self, node: BinaryTreeNode | None = None) -> int:
        """
        Calculates the height of the binary tree.

        Returns:
            int: The height of the tree.
        """
        if node is not None:
            if not isinstance(node, BinaryTreeNode):
                raise TypeError("node must be an instance of BinaryTreeNode")
        else:
            node = self.root

        if node is None:
            return 0

        queue = Queue()
        queue.enqueue((node, 1))
        height = 0

        while not queue.is_empty():
            current_node, current_height = queue.dequeue()
            height = max(height, current_height)

            if current_node.left is not None:
                queue.enqueue((current_node.left, current_height + 1))

            if current_node.right is not None:
                queue.enqueue((current_node.right, current_height + 1))

        return height

    @abstractmethod
    def insert(self, node: BinaryTreeNode) -> None:
        """
        Inserts a new node into the binary tree.

        Args:
            node (BinaryTreeNode): The node to insert.
        """

    @abstractmethod
    def delete(self, node: BinaryTreeNode) -> None:
        """
        Deletes a node from the binary tree.

        Args:
            node (BinaryTreeNode): The node to delete.
        """

    @abstractmethod
    def search(self, key: int) -> BinaryTreeNode | None:
        """
        Searches for a node with the given key in the binary tree.

        Args:
            key (int): The key of the node to search for.

        Returns:
            BinaryTreeNode | None: The node with the specified key if found, otherwise None.
        """

    @abstractmethod
    def traverse_in_order(
        self, start: BinaryTreeNode | None = None
    ) -> list[BinaryTreeNode]:
        """
        Traverses the binary tree in-order (left-root-right) and returns a list of visited nodes.

        Args:
            start (BinaryTreeNode | None): The node to start traversing from.
                Defaults to the root node.

        Returns:
            list[BinaryTreeNode]: A list of visited nodes in the order they were traversed.
        """

    @abstractmethod
    def traverse_pre_order(
        self, start: BinaryTreeNode | None = None
    ) -> list[BinaryTreeNode]:
        """
        Traverses the binary tree pre-order (root-left-right) and returns a list of visited nodes.

        Args:
            start (BinaryTreeNode | None): The node to start traversing from.
                Defaults to the root node.

        Returns:
            list[BinaryTreeNode]: A list of visited nodes in the order they were traversed.
        """

    @abstractmethod
    def traverse_post_order(
        self, start: BinaryTreeNode | None = None
    ) -> list[BinaryTreeNode]:
        """
        Traverses the binary tree post-order (left-right-root) and returns a list of visited nodes.

        Args:
            start (BinaryTreeNode | None): The node to start traversing from.
                Defaults to the root node.

        Returns:
            list[BinaryTreeNode]: A list of visited nodes in the order they were traversed.
        """

    @abstractmethod
    def max_node(self) -> BinaryTreeNode | None:
        """
        Finds the node with the maximum key in the binary tree.

        Returns:
            BinaryTreeNode | None: The node with the maximum key if found, otherwise None.
        """

    @abstractmethod
    def min_node(self) -> BinaryTreeNode | None:
        """
        Finds the node with the minimum key in the binary tree.

        Returns:
            BinaryTreeNode | None: The node with the minimum key if found, otherwise None.
        """


class BinarySearchTree(BinaryTree):
    """
    A binary search tree implementation.
    """

    def search(self, key: int) -> BinaryTreeNode | None:
        """
        Searches for a node with the given key in the binary search tree.

        Args:
            key (int): The key of the node to search for.

        Returns:
            BinaryTreeNode | None: The node with the specified key if found, otherwise None.
        """
        if not isinstance(key, int):
            raise TypeError("key must be an integer")

        return self.__search(key, self.root)

    def __search(self, key: int, node: BinaryTreeNode | None) -> BinaryTreeNode | None:
        """
        Utility method that recursively searches for a node
        with the given key starting from the specified node.

        Args:
            key (int): The key of the node to search for.
            node (BinaryTreeNode | None): The node to start searching from.

        Returns:
            BinaryTreeNode | None: The node with the specified key if found, otherwise None.
        """

        if node is None:
            return None

        if node.key == key:
            return node

        if key < node.key:
            return self.__search(key, node.left)

        return self.__search(key, node.right)

    def traverse_in_order(
        self, start: BinaryTreeNode | None = None
    ) -> list[BinaryTreeNode]:
        """
        Traverses the binary tree in-order (left-root-right) and returns a list of visited nodes.

        Args:
            start (BinaryTreeNode | None): The node to start traversing from.
                Defaults to the root node.

        Returns:
            list[BinaryTreeNode]: A list of visited nodes in the order they were traversed.
        """
        if start is None:
            start = self.root
        else:
            if not isinstance(start, BinaryTreeNode):
                raise TypeError("start must be an instance of BinaryTreeNode")

        if start is None:
            return []

        in_order_list = []

        if start.left is not None:
            in_order_list.extend(self.traverse_in_order(start.left))

        in_order_list.append(start)

        if start.right is not None:
            in_order_list.extend(self.traverse_in_order(start.right))

        return in_order_list

    def traverse_pre_order(
        self, start: BinaryTreeNode | None = None
    ) -> list[BinaryTreeNode]:
        """
        Traverses the binary tree pre-order (root-left-right) and returns a list of visited nodes.

        Args:
            start (BinaryTreeNode | None): The node to start traversing from.
                Defaults to the root node.

        Returns:
            list[BinaryTreeNode]: A list of visited nodes in the order they were traversed.
        """

        if start is None:
            start = self.root
        else:
            if not isinstance(start, BinaryTreeNode):
                raise TypeError("start must be an instance of BinaryTreeNode")

        if start is None:
            return []

        pre_order_list = [start]

        if start.left is not None:
            pre_order_list.extend(self.traverse_pre_order(start.left))

        if start.right is not None:
            pre_order_list.extend(self.traverse_pre_order(start.right))

        return pre_order_list

    def traverse_post_order(
        self, start: BinaryTreeNode | None = None
    ) -> list[BinaryTreeNode]:
        """
        Traverses the binary tree post-order (left-right-root) and returns a list of visited nodes.

        Args:
            start (BinaryTreeNode | None): The node to start traversing from.
                Defaults to the root node.

        Returns:
            list[BinaryTreeNode]: A list of visited nodes in the order they were traversed.
        """
        if start is None:
            start = self.root
        else:
            if not isinstance(start, BinaryTreeNode):
                raise TypeError("start must be an instance of BinaryTreeNode")

        if start is None:
            return []

        post_order_list = []

        if start.left is not None:
            post_order_list.extend(self.traverse_post_order(start.left))

        if start.right is not None:
            post_order_list.extend(self.traverse_post_order(start.right))

        post_order_list.append(start)

        return post_order_list

    def insert(self, node: BinaryTreeNode) -> None:
        """
        Inserts a new node into the binary search tree.

        Args:
            node (BinaryTreeNode): The node to insert. It must be an instance of BinaryTreeNode.

        Raises:
            TypeError: If the node is not an instance of BinaryTreeNode.
        """

        if not isinstance(node, BinaryTreeNode):
            raise TypeError("node must be an instance of BinaryTreeNode")

        if self.root is None:
            self.root = node
        else:
            self.__insert(node, self.root)

    def __insert(self, node: BinaryTreeNode, parent: BinaryTreeNode) -> None:
        """
        Recursive utility method to insert a node into the binary search tree.

        Args:
            node (BinaryTreeNode): The node to insert.
            parent (BinaryTreeNode): The parent node to insert against.

        Raises:
            ValueError: If the key already exists in the tree.
        """
        # key is less than parent
        if node.key < parent.key:

            # assign to left child
            if parent.left is None:
                parent.left = node
                node.parent = parent

            # recursive call against the left child
            else:
                self.__insert(node, parent.left)

        # key is greater than or equal to parent
        elif node.key > parent.key:

            # assign to right child
            if parent.right is None:
                parent.right = node
                node.parent = parent

            # recursive call against the right child
            else:
                self.__insert(node, parent.right)

        # key is equal to parent
        else:
            raise ValueError("Key already exists in the tree")

    def delete(self, node: BinaryTreeNode) -> None:
        """
        Deletes a node from the binary search tree.

        Args:
            node (BinaryTreeNode): The node to delete. It must be an instance of BinaryTreeNode.

        Raises:
            TypeError: If the node is not an instance of BinaryTreeNode.
            ValueError: If the tree is empty.
        """

        if not isinstance(node, BinaryTreeNode):
            raise TypeError("node must be an instance of BinaryTreeNode")

        if self.root is None:
            raise ValueError("Tree is empty")

        self.__delete(node)

    def __delete(self, node: BinaryTreeNode) -> None:
        """
        Utility method to delete a node from the binary search tree.

        This method handles the deletion by determining the type of node (i.e.,
        whether it has no children, only a left child, only a right child, or both children)
        and delegates the deletion process to the appropriate helper method.

        Args:
            node (BinaryTreeNode): The node to delete.
        """

        left_child = node.left
        right_child = node.right

        # Only left child
        if left_child and (right_child is None):
            self.__delete_with_left_child(node)

        # Only right child
        elif (left_child is None) and right_child:
            self.__delete_with_right_child(node)

        # Both children
        elif left_child and right_child:
            self.__delete_with_two_children(node)

        # No children
        else:
            self.__delete_no_children(node)

    def __delete_with_left_child(self, node: BinaryTreeNode) -> None:
        """
        Utility function to delete a node with only a left child.

        Args:
            node (BinaryTreeNode): The node to delete.
        """
        parent = node.parent
        left_child = node.left

        # Assign the left child to the parent
        if parent is not None:
            parent.left = left_child
            if left_child is not None:
                left_child.parent = parent

        # Assign the left child to the root
        else:
            self.root = left_child
            if left_child is not None:
                left_child.parent = None

    def __delete_with_right_child(self, node: BinaryTreeNode) -> None:
        """
        Utility method to delete a node with only a right child.

        Args:
            node (BinaryTreeNode): The node to delete.
        """
        parent = node.parent
        right_child = node.right

        # Assign the right child to the parent
        if parent is not None:
            parent.right = right_child
            if right_child is not None:
                right_child.parent = parent

        # Assign the right child to the root
        else:
            self.root = right_child
            if right_child is not None:
                right_child.parent = None

    def __delete_with_two_children(self, node: BinaryTreeNode) -> None:
        """
        Utility method to delete a node with two children.

        Args:
            node (BinaryTreeNode): The node to delete.

        Raises:
            ValueError: Raised if the tree is empty.
        """
        # Find the successor
        replacement_node = self.__successor(node)
        if replacement_node is None:
            raise ValueError("Tree is empty.")

        # Create a temporary node
        temp_node = BinaryTreeNode(
            key=0,
            value="Temp_Value",
        )
        # Move the temporary node to the deletion node's position
        self.__swap_node_positions(node, temp_node)

        # Move the deletion node to the replacement node's position
        self.__swap_node_positions(replacement_node, node)

        # Move the replacement node to the temporary node's position
        self.__swap_node_positions(temp_node, replacement_node)

        # Delete the deletion node
        self.__delete(node)

    def __delete_no_children(self, node: BinaryTreeNode) -> None:
        """
        Utility method to delete a node with no children.

        Args:
            node (BinaryTreeNode): The node to delete.
        """
        parent = node.parent

        if parent is not None:
            if parent.left is node:
                parent.left = None
            if parent.right is node:
                parent.right = None
        else:
            self.root = None

    def __swap_node_positions(
        self, node1: BinaryTreeNode, node2: BinaryTreeNode
    ) -> None:
        """
        Utility method that swaps the positions of two nodes.
        Node2 will inherit node1's position.

        Args:
            node1 (BinaryTreeNode): The outgoing node.
            node2 (BinaryTreeNode): The incoming node.
        """
        # Inherit node1's references
        node2.parent = node1.parent
        node2.left = node1.left
        node2.right = node1.right

        # Update node1's children
        if node1.left is not None:
            node1.left.parent = node2
        if node1.right is not None:
            node1.right.parent = node2

        # Update node1's parent
        if node1.parent is not None:
            if node1.parent.left is node1:
                node1.parent.left = node2
            if node1.parent.right is node1:
                node1.parent.right = node2
        else:
            self.root = node2

    def __successor(self, node: BinaryTreeNode) -> BinaryTreeNode | None:
        """
        Finds the in-order predecessor of a given node in the binary search tree.

        Args:
            node (BinaryTreeNode): The node to find the predecessor for.

        Returns:
            BinaryTreeNode | None: The predecessor node if it exists, otherwise None.
        """

        if node.left is None:
            if node.right is None:
                return None

            min_node = self.__min_node(node.right)
            return min_node

        max_node = self.__max_node(node.left)
        return max_node

    def max_node(self) -> BinaryTreeNode | None:
        """
        Finds the node with the maximum key in the binary tree.

        Returns:
            BinaryTreeNode | None: The node with the maximum key if found, otherwise None.
        """
        return self.__max_node(self.root)

    def __max_node(self, node: BinaryTreeNode | None) -> BinaryTreeNode | None:
        """
        Utility method that finds the node with the maximum key in a subtree.

        Args:
            node (BinaryTreeNode | None): The root node of the subtree.

        Returns:
            BinaryTreeNode | None: The node with the maximum key in the subtree if found,
                otherwise None.
        """

        if node is None:
            return None

        current_node = node
        while current_node.right is not None:
            current_node = current_node.right

        return current_node

    def min_node(self) -> BinaryTreeNode | None:
        """
        Finds the node with the minimum key in the binary tree.

        Returns:
            BinaryTreeNode | None: The node with the minimum key if found, otherwise None.
        """
        return self.__min_node(self.root)

    def __min_node(self, node: BinaryTreeNode | None) -> BinaryTreeNode | None:
        """
        Utility method that finds the node with the minimum key in a subtree.

        Args:
            node (BinaryTreeNode | None): The root node of the subtree.

        Returns:
            BinaryTreeNode | None: The node with the minimum key in the subtree if found,
                otherwise None.
        """

        if node is None:
            return None

        current_node = node
        while current_node.left is not None:
            current_node = current_node.left

        return current_node
