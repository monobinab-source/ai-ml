from collections import deque
from bst_node import BSTNode


class BinarySearchTree:
    """A Binary Search Tree (BST) implementation for storing Dollar objects."""

    def __init__(self):
        """Initialize an empty Binary Search Tree."""
        self.root = None

    def is_empty(self):
        """
        Check if the BST is empty.

        :return: True if the tree is empty, False otherwise.
        """
        return self.root is None

    def insert(self, data):
        """
        Insert a Dollar object into the BST.

        :param data: A Dollar object to be inserted.
        """

        def _insert(node, data):
            if not node:
                return BSTNode(data)
            if data < node.data:
                node.left = _insert(node.left, data)
            elif data > node.data:
                node.right = _insert(node.right, data)
            return node

        self.root = _insert(self.root, data)

    def search(self, value):
        """
        Search for a Dollar object in the BST based on its monetary value.

        :param value: The float value to search for.
        :return: The BSTNode containing the Dollar object if found, otherwise None.
        """

        def _search(node, value):
            if not node:
                return None
            if node.data.value() == value:
                return node
            elif value < node.data.value():
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

    def delete(self, value):
        """
        Delete a node by its Dollar object's monetary value.

        :param value: The float value of the Dollar object to delete.
        """

        def _delete(node, value):
            if not node:
                return node
            if value < node.data.value():
                node.left = _delete(node.left, value)
            elif value > node.data.value():
                node.right = _delete(node.right, value)
            else:
                # Node to be deleted found
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                # Replace with the smallest in the right subtree
                temp = self._min_value_node(node.right)
                node.data = temp.data
                node.right = _delete(node.right, temp.data.value())
            return node

        self.root = _delete(self.root, value)

    def _min_value_node(self, node):
        """
        Find the node with the smallest value in a subtree.

        :param node: The root of the subtree to search.
        :return: The BSTNode with the smallest value.
        """
        current = node
        while current.left:
            current = current.left
        return current

    def count(self):
        """
        Count the number of nodes in the BST.

        :return: The total number of nodes in the BST as an integer.
        """

        def _count(node):
            if not node:
                return 0
            return 1 + _count(node.left) + _count(node.right)

        return _count(self.root)

    def _traverse(self, node, order, result):
        """
        Generic traversal function to visit nodes in a specific order.

        :param node: The current BSTNode being visited.
        :param order: The order of traversal ('in', 'pre', 'post').
        :param result: A list to store the traversal result.
        """
        if not node:
            return
        if order == "pre":
            result.append(node.data)
        self._traverse(node.left, order, result)
        if order == "in":
            result.append(node.data)
        self._traverse(node.right, order, result)
        if order == "post":
            result.append(node.data)

    def in_order(self):
        """
        Perform an in-order traversal of the BST.

        :return: A list of Dollar objects in in-order sequence.
        """
        result = []
        self._traverse(self.root, "in", result)
        return result

    def pre_order(self):
        """
        Perform a pre-order traversal of the BST.

        :return: A list of Dollar objects in pre-order sequence.
        """
        result = []
        self._traverse(self.root, "pre", result)
        return result

    def post_order(self):
        """
        Perform a post-order traversal of the BST.

        :return: A list of Dollar objects in post-order sequence.
        """
        result = []
        self._traverse(self.root, "post", result)
        return result

    def breadth_first(self):
        """
        Perform a breadth-first traversal of the BST.

        :return: A list of Dollar objects in breadth-first sequence.
        """
        if not self.root:
            return []
        result, queue = [], deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def empty(self):
        """
        Remove all nodes from the BST, making it empty.
        """
        self.root = None

# from collections import deque
# from bst_node import BSTNode
#
#
# class BinarySearchTree:
#     def __init__(self):
#         """
#         Initialize an empty Binary Search Tree.
#         """
#         self.root = None
#
#     def is_empty(self):
#         """
#         Check if the BST is empty.
#         :return: True if the tree is empty, False otherwise.
#         """
#         return self.root is None
#
#     def insert(self, value):
#         """
#         Insert a value into the BST.
#
#         :param value: The value to insert.
#         """
#         new_node = BSTNode(value)
#
#         if self.root is None:
#             self.root = new_node
#             return
#
#         current = self.root
#         while True:
#             if value < current.get_data():
#                 if current.get_left() is None:
#                     current.set_left(new_node)
#                     return
#                 current = current.get_left()
#             else:
#                 if current.get_right() is None:
#                     current.set_right(new_node)
#                     return
#                 current = current.get_right()
#
#     def search(self, value):
#         """
#         Search for a node with the given value.
#
#         :param value: The value to search for.
#         :return: The node containing the value, or None if not found.
#         """
#
#         def _search(node, value):
#             if node is None:
#                 return None
#             if node.get_data() == value:
#                 return node
#             elif value < node.get_data():
#                 return _search(node.get_left(), value)
#             else:
#                 return _search(node.get_right(), value)
#
#         return _search(self.root, value)
#
#     def delete(self, value):
#         """
#         Delete a node with the given value from the BST.
#
#         :param value: The value to delete.
#         """
#
#         def _delete(node, value):
#             if node is None:
#                 return node
#
#             if value < node.get_data():
#                 node.set_left(_delete(node.get_left(), value))
#             elif value > node.get_data():
#                 node.set_right(_delete(node.get_right(), value))
#             else:
#                 # Node with only one child or no child
#                 if node.get_left() is None:
#                     return node.get_right()
#                 elif node.get_right() is None:
#                     return node.get_left()
#
#                 # Node with two children
#                 temp = self._min_value_node(node.get_right())
#                 node.set_data(temp.get_data())
#                 node.set_right(_delete(node.get_right(), temp.get_data()))
#
#             return node
#
#         self.root = _delete(self.root, value)
#
#     def _min_value_node(self, node):
#         """
#         Get the node with the smallest value in the subtree.
#
#         :param node: The starting node.
#         :return: The node with the smallest value.
#         """
#         current = node
#         while current.get_left() is not None:
#             current = current.get_left()
#         return current
#
#     def in_order(self, node):
#         """
#         Perform in-order traversal of the BST.
#
#         :param node: The starting node.
#         :return: A list of Dollar objects in in-order traversal order.
#         """
#         result = []
#
#         if node is not None:
#             self.in_order(node.get_left())
#             result.append(node.get_data())
#             print(node.get_data())
#             self.in_order(node.get_right())
#         return result
#
#     def pre_order(self, node):
#         """
#         Perform pre-order traversal of the BST.
#
#         :param node: The starting node.
#         """
#         result = []
#         if node is not None:
#             print(node.get_data())
#             self.pre_order(node.get_left())
#             self.pre_order(node.get_right())
#         return result
#
#     def post_order(self, node):
#         """
#         Perform post-order traversal of the BST.
#
#         :param node: The starting node.
#         """
#         result = []
#         if node is not None:
#             self.post_order(node.get_left())
#             self.post_order(node.get_right())
#             print(node.get_data())
#         return result
#
#     def breadth_first(self):
#         """
#         Perform breadth-first traversal of the BST.
#         """
#         if self.root is None:
#             return
#
#         queue = [self.root]
#         result = []
#
#         while queue:
#             current = queue.pop(0)
#             result.append(current.get_data())
#             print(current.get_data())
#
#             if current.get_left():
#                 queue.append(current.get_left())
#             if current.get_right():
#                 queue.append(current.get_right())
#         return result
#
#     def count(self, node):
#         """
#         Count the total number of nodes in the BST.
#
#         :param node: The starting node.
#         :return: The number of nodes in the subtree.
#         """
#         if node is None:
#             return 0
#         return 1 + self.count(node.get_left()) + self.count(node.get_right())
#
#     def print_traversals(self):
#         """
#         Print all traversal orders (breadth-first, in-order, pre-order, post-order).
#         """
#         print("Breadth-First Traversal:")
#         self.breadth_first()
#         print("\nIn-Order Traversal:")
#         self.in_order(self.root)
#         print("\nPre-Order Traversal:")
#         self.pre_order(self.root)
#         print("\nPost-Order Traversal:")
#         self.post_order(self.root)

