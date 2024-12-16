class BSTNode:
    def __init__(self, data):
        """
        BSTNode ADT with a data attribute and two pointer attributes, one for the left child and the other for the right child.
        :param data:
        """
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"BSTNode({self.data})"


# class BSTNode:
#     def __init__(self, data):
#         """
#         BSTNode ADT with a data attribute and two pointer attributes, one for the left child and the other for the right child.
#         :param data: The value to store in the node.
#         """
#         self._data = data
#         self._left = None
#         self._right = None
#
#     # Getter for data
#     def get_data(self):
#         """
#         Get the data stored in the node.
#         :return: The data value.
#         """
#         return self._data
#
#     # Setter for data
#     def set_data(self, value):
#         """
#         Set the data value for the node.
#         :param value: The new data value.
#         """
#         self._data = value
#
#     # Getter for left child
#     def get_left(self):
#         """
#         Get the left child node.
#         :return: The left child node.
#         """
#         return self._left
#
#     # Setter for left child
#     def set_left(self, node):
#         """
#         Set the left child node.
#         :param node: The new left child node.
#         """
#         self._left = node
#
#     # Getter for right child
#     def get_right(self):
#         """
#         Get the right child node.
#         :return: The right child node.
#         """
#         return self._right
#
#     # Setter for right child
#     def set_right(self, node):
#         """
#         Set the right child node.
#         :param node: The new right child node.
#         """
#         self._right = node
#
#     def __repr__(self):
#         """
#         Represent the BSTNode as a string.
#         :return: A string representation of the node.
#         """
#         return f"BSTNode({self._data})"

