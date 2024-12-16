from binary_search_tree import BinarySearchTree, BSTNode
from dollar import Dollar
# from BST import BST
# from BST import BSTNode
"""
Author: Monobina Saha
CIS 22C Lab 6
"""

class MinHeap(BinarySearchTree):
    def __init__(self):
        """
        Initialize the MinHeap as a derived class of BinarySearchTree.
        """
        super().__init__()
        self.heap = []

    def insert(self, dollar_obj):
        """
        Override the insert method to maintain the MinHeap property.
        Inserts a Dollar object and ensures the min-heap structure is preserved.

        pre: dollar_obj - The Dollar object to insert.
        post: inserts dollar object into heap and then bubbled up to maintain heap
        return:
        """
        node = BSTNode(dollar_obj)
        if not self.root:
            self.root = node
            return

        # Insert into BST normally
        super().insert(dollar_obj)

        # Restore MinHeap property by bubbling up
        self._bubble_up(len(self.heap) - 1)

    def delete(self, value):
        """
        Override the delete method to maintain the MinHeap property after deletion.
        Deletes a node with the given value and ensures the heap property is preserved.

        pre: value which needs to be deleted
        post: deletes the value and then bubbled down to maintain heap
        return:
        """
        super().delete(value)

        # After deletion, ensure MinHeap property
        self._bubble_down(self.root)

    def search(self, value):
        """
        Override the search method to find a node with the given value.
        pre: value: The float value to search.
        post: returns value if found
        :return: The node containing the value, or None if not found.
        """
        return super().search(value)


    def _bubble_up(self, index):
        """
        Moves the element at the given index up the heap until the heap property is restored.

        pre: The index of the element to bubble up
        post: the value is bubbled up to maintain heap
        return:
        """
        while index > 0:
            parent_index = (index - 1) // 2  # Calculate the parent's index
            if self.heap[index].value() < self.heap[parent_index].value():
                # Swap if the child is smaller than the parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index  # Update index to continue bubbling up
            else:
                break  # Stop if the heap property is satisfied


    def _bubble_down(self, index):
        """
        Moves the element at the given index down the heap until the heap property is restored.

        pre: The index of the element to bubble down.
        post: the value is bubbled down to maintain heap
        return:
        """
        while 2 * index + 1 < len(self.heap):  # While there's at least one child
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            # Check left child
            if self.heap[left_child].value() < self.heap[smallest].value():
                smallest = left_child

            # Check right child (if it exists)
            if right_child < len(self.heap) and self.heap[right_child].value() < self.heap[smallest].value():
                smallest = right_child

            if smallest != index:
                # Swap with the smallest child
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest  # Continue bubbling down from the new position
            else:
                break  # Heap property is satisfied

    def _build_min_heap(self, nodes):
        """
        Builds a balanced binary tree with MinHeap property from sorted nodes.

        :param nodes: A sorted list of Dollar objects.
        :return: The root of the balanced tree.
        """
        if not nodes:
            return None

        mid = len(nodes) // 2
        root = BSTNode(nodes[mid])
        root.left = self._build_min_heap(nodes[:mid])
        root.right = self._build_min_heap(nodes[mid + 1:])
        return root
