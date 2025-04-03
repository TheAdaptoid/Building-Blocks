from essential_building_blocks.data_structures.trees import BinarySearchTree
from essential_building_blocks.data_structures.types.nodes import BinaryTreeNode
import pytest


class TestBinaryTreeNode:
    def test_init(self):
        node = BinaryTreeNode(1, "value")
        assert node.key == 1
        assert node.value == "value"
        assert node.left is None
        assert node.right is None

        with pytest.raises(TypeError):
            BinaryTreeNode(1, "value", "parent")

        with pytest.raises(TypeError):
            BinaryTreeNode(1, "value", None, "left")

        with pytest.raises(TypeError):
            BinaryTreeNode(1, "value", None, None, "right")


class TestBinarySearchTree:
    def test_init(self):
        tree = BinarySearchTree()
        assert tree.root is None
        assert tree.is_empty() is True
        assert tree.size() == 0

        node = BinaryTreeNode(1, "value")
        tree = BinarySearchTree(node)
        assert tree.root == node
        assert tree.is_empty() is False
        assert tree.size() == 1

        with pytest.raises(TypeError):
            BinarySearchTree("not a node")

    def test_is_empty(self):
        tree = BinarySearchTree()
        assert tree.is_empty() is True

        node = BinaryTreeNode(1, "value")
        tree = BinarySearchTree(node)
        assert tree.is_empty() is False

    def test_size(self):
        tree = BinarySearchTree()
        assert tree.size() == 0

        node = BinaryTreeNode(1, "value")
        tree = BinarySearchTree(node)
        assert tree.size() == 1

    def test_height(self):
        tree = BinarySearchTree()
        assert tree.height() == 0

        node = BinaryTreeNode(1, "value")
        tree = BinarySearchTree(node)
        assert tree.height() == 1

        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")
        node5 = BinaryTreeNode(5, "value")
        tree.insert(node3)
        tree.insert(node4)
        tree.insert(node2)
        tree.insert(node1)
        tree.insert(node5)
        assert tree.height() == 3
        assert tree.height(node1) == 1
        assert tree.height(node4) == 2

        with pytest.raises(TypeError):
            tree.height("not a node")

    def test_insert(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")
        node5 = BinaryTreeNode(5, "value")

        tree.insert(node2)
        assert tree.root == node2
        assert tree.size() == 1
        assert tree.search(node2.key) == node2
        assert tree.traverse_in_order() == [node2]

        tree.insert(node1)
        assert tree.size() == 2
        assert tree.search(node1.key) == node1
        assert tree.traverse_in_order() == [node1, node2]

        tree.insert(node3)
        assert tree.size() == 3
        assert tree.search(node3.key) == node3
        assert tree.traverse_in_order() == [node1, node2, node3]

        tree.insert(node5)
        assert tree.size() == 4
        assert tree.search(node5.key) == node5
        assert tree.traverse_in_order() == [node1, node2, node3, node5]

        tree.insert(node4)
        assert tree.size() == 5
        assert tree.search(node4.key) == node4
        assert tree.traverse_in_order() == [node1, node2, node3, node4, node5]

        with pytest.raises(TypeError):
            tree.insert("not a node")

        with pytest.raises(ValueError):
            tree.insert(node2)

    def test_search(self):
        tree = BinarySearchTree()
        for key in range(-20, 20):
            tree.insert(BinaryTreeNode(key, "value"))

        for key in range(-20, 20):
            assert tree.search(key).key == key

        assert tree.search(100) is None

        with pytest.raises(TypeError):
            tree.search("not a key")

    def test_traverse_in_order(self):
        tree = BinarySearchTree()
        assert tree.traverse_in_order() == []

        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")
        node5 = BinaryTreeNode(5, "value")

        tree.insert(node3)
        tree.insert(node4)
        tree.insert(node2)
        tree.insert(node1)
        tree.insert(node5)
        assert tree.traverse_in_order() == [node1, node2, node3, node4, node5]

        with pytest.raises(TypeError):
            tree.traverse_in_order("not a node")

        assert tree.traverse_in_order(node4) == [node4, node5]

    def test_traverse_pre_order(self):
        tree = BinarySearchTree()
        assert tree.traverse_pre_order() == []

        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")
        node5 = BinaryTreeNode(5, "value")

        tree.insert(node3)
        tree.insert(node4)
        tree.insert(node2)
        tree.insert(node1)
        tree.insert(node5)
        assert tree.traverse_pre_order() == [node3, node2, node1, node4, node5]

        with pytest.raises(TypeError):
            tree.traverse_pre_order("not a node")

        assert tree.traverse_pre_order(node4) == [node4, node5]

    def test_traverse_post_order(self):
        tree = BinarySearchTree()
        assert tree.traverse_post_order() == []

        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")
        node5 = BinaryTreeNode(5, "value")

        tree.insert(node3)
        tree.insert(node4)
        tree.insert(node2)
        tree.insert(node1)
        tree.insert(node5)
        assert tree.traverse_post_order() == [node1, node2, node5, node4, node3]

        with pytest.raises(TypeError):
            tree.traverse_post_order("not a node")

        assert tree.traverse_post_order(node4) == [node5, node4]

    def test_delete_with_no_nodes(self):
        tree = BinarySearchTree()
        assert tree.size() == 0
        assert tree.is_empty() is True
        with pytest.raises(ValueError):
            tree.delete(BinaryTreeNode(1, "value"))

    def test_delete_root_with_no_children(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")

        tree.insert(node1)
        assert tree.root == node1
        assert tree.size() == 1
        tree.delete(node1)
        assert tree.root is None
        assert tree.size() == 0

    def test_delete_root_with_left_child(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")

        tree.insert(node2)
        tree.insert(node1)
        assert tree.root == node2
        assert tree.size() == 2
        tree.delete(node2)
        assert tree.root == node1
        assert tree.size() == 1

    def test_delete_root_with_right_child(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")

        tree.insert(node1)
        tree.insert(node2)
        assert tree.root == node1
        assert tree.size() == 2
        tree.delete(node1)
        assert tree.root == node2
        assert tree.size() == 1

    def test_delete_root_with_two_children(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")

        tree.insert(node2)
        tree.insert(node1)
        tree.insert(node3)
        assert tree.root == node2
        assert tree.root.left == node1
        assert tree.root.right == node3
        assert tree.size() == 3

        tree.delete(node2)
        assert tree.root == node1
        assert tree.size() == 2
        assert tree.root.left is None
        assert tree.root.right == node3

    def test_delete_with_left_child(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")

        tree.insert(node4)
        tree.insert(node3)
        tree.insert(node2)
        tree.insert(node1)
        assert tree.root == node4
        assert tree.size() == 4

        # delete root
        tree.delete(node4)
        assert tree.size() == 3
        assert tree.search(node4.key) is None
        assert tree.traverse_in_order() == [node1, node2, node3]

        # delete 2nd to last left node
        tree.delete(node2)
        assert tree.size() == 2
        assert tree.search(node2.key) is None
        assert tree.traverse_in_order() == [node1, node3]

    def test_delete_with_right_child(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")

        tree.insert(node1)
        tree.insert(node2)
        tree.insert(node3)
        tree.insert(node4)
        assert tree.root == node1
        assert tree.size() == 4

        # delete root
        tree.delete(node1)
        assert tree.size() == 3
        assert tree.search(node1.key) is None
        assert tree.traverse_in_order() == [node2, node3, node4]

        # delete 2nd to last right node
        tree.delete(node4)
        assert tree.size() == 2
        assert tree.search(node4.key) is None
        assert tree.traverse_in_order() == [node2, node3]

    def test_delete_with_two_children(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")

        tree.insert(node1)
        tree.insert(node3)
        tree.insert(node2)
        tree.insert(node4)
        assert tree.root == node1
        assert tree.size() == 4

        tree.delete(node3)
        assert tree.size() == 3
        assert tree.search(node3.key) is None
        assert tree.search(node2.key) == node2
        assert tree.search(node4.key) == node4
        assert tree.traverse_in_order() == [node1, node2, node4]

    def test_delete_with_no_children(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")

        tree.insert(node1)
        tree.insert(node3)
        tree.insert(node2)
        tree.insert(node4)
        assert tree.root == node1
        assert tree.size() == 4

        tree.delete(node4)
        assert tree.size() == 3
        assert tree.search(node4.key) is None
        assert tree.traverse_in_order() == [node1, node2, node3]

    def test_delete_with_left_skew(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")

        tree.insert(node1)
        tree.insert(node2)
        tree.insert(node3)
        tree.insert(node4)
        assert tree.root == node1
        assert tree.size() == 4

        tree.delete(node2)
        assert tree.size() == 3
        assert tree.search(node2.key) is None
        assert tree.traverse_in_order() == [node1, node3, node4]

    def test_delete_with_right_skew(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")

        tree.insert(node4)
        tree.insert(node3)
        tree.insert(node2)
        tree.insert(node1)
        assert tree.root == node4
        assert tree.size() == 4

        tree.delete(node3)
        assert tree.size() == 3
        assert tree.search(node3.key) is None
        assert tree.traverse_in_order() == [node1, node2, node4]

    def test_delete_wrong_type(self):
        tree = BinarySearchTree()
        with pytest.raises(TypeError):
            tree.delete("not a node")
        with pytest.raises(TypeError):
            tree.delete(1)
        with pytest.raises(TypeError):
            tree.delete(None)

    def test_delete_none(self):
        tree = BinarySearchTree()
        node = BinaryTreeNode(1, "value")
        with pytest.raises(ValueError):
            tree.delete(node)

    def test_max_node_right_skew(self):
        tree = BinarySearchTree()
        assert tree.max_node() is None

        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")

        tree.insert(node1)
        tree.insert(node3)
        tree.insert(node2)
        tree.insert(node4)
        assert tree.max_node() == node4

        tree.delete(node4)
        assert tree.max_node() == node3

    def test_max_left_skew(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")

        tree.insert(node4)
        tree.insert(node3)
        tree.insert(node2)
        tree.insert(node1)
        assert tree.max_node() == node4

        tree.delete(node4)
        assert tree.max_node() == node3

    def test_min_node_right_skew(self):
        tree = BinarySearchTree()
        assert tree.min_node() is None

        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")

        tree.insert(node1)
        tree.insert(node3)
        tree.insert(node2)
        tree.insert(node4)
        assert tree.min_node() == node1

        tree.delete(node1)
        assert tree.min_node() == node2

    def test_min_left_skew(self):
        tree = BinarySearchTree()
        node1 = BinaryTreeNode(1, "value")
        node2 = BinaryTreeNode(2, "value")
        node3 = BinaryTreeNode(3, "value")
        node4 = BinaryTreeNode(4, "value")

        tree.insert(node4)
        tree.insert(node3)
        tree.insert(node2)
        tree.insert(node1)
        assert tree.min_node() == node1

        tree.delete(node1)
        assert tree.min_node() == node2
