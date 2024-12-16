from singly_linked_list import SinglyLinkedList
from link_node import link_node

class Queue(SinglyLinkedList):
    def __init__(self):
        """Constructor to initialize an empty queue."""
        super().__init__()  # Initialize with the SinglyLinkedList constructor

    # ----------------- Optional Queue Creation/Destruction Methods ----------------- #
    def create_queue(self):
        """Optional method to reset the queue."""
        self.create_list()

    def destroy_queue(self):
        """Optional method to clear the queue."""
        self.destroy_list()

    # ----------------- Queue Methods ----------------- #
    def enqueue(self, currency):
        """
        Adds a Currency object to the end of the queue (rear).

        :param currency: A Currency object to be added.
        """
        new_node = link_node(currency)
        if self.is_list_empty():
            self.set_head(new_node)
            self.set_tail(new_node)
        else:
            self.get_tail().next = new_node
            self.set_tail(new_node)
        self.set_count(self.get_count() + 1)

    def dequeue(self):
        """
        Removes and returns the Currency object from the front of the queue.

        :return: The Currency object at the front of the queue.
        """
        if self.is_list_empty():
            raise IndexError("Dequeue from empty queue")

        front_node = self.get_head()
        self.set_head(front_node.next)
        if self.get_head() is None:  # If the queue becomes empty
            self.set_tail(None)

        self.set_count(self.get_count() - 1)
        return front_node.data  # Return the removed Currency object

    def peek_front(self):
        """
        Returns the Currency object at the front of the queue without removing it.

        :return: The Currency object at the front of the queue.
        """
        if self.is_list_empty():
            raise IndexError("Peek from empty queue")

        return self.get_head().data

    def peek_rear(self):
        """
        Returns the Currency object at the rear of the queue without removing it.

        :return: The Currency object at the end of the queue.
        """
        if self.is_list_empty():
            raise IndexError("Peek from empty queue")

        return self.get_tail().data

    def print_queue(self):
        """
        Returns a string representation of the queue contents from front to rear, tab-spaced.
        """
        result = []
        current = self.get_head()

        while current:
            result.append(str(current.data))
            current = current.next

        return "\t".join(result)

    # ----------------- Overriding Linked List Methods to Disable Them ----------------- #
    def add_currency(self, *args, **kwargs):
        """Disable the add_currency method."""
        raise NotImplementedError("Use enqueue() to add elements to the queue")

    def remove_currency(self, *args, **kwargs):
        """Disable the remove_currency method."""
        raise NotImplementedError("Use dequeue() to remove elements from the queue")

    def remove_currency_by_index(self, *args, **kwargs):
        """Disable the remove_currency_by_index method."""
        raise NotImplementedError("Use dequeue() to remove elements from the queue")

    def find_currency(self, *args, **kwargs):
        """Disable the find_currency method."""
        raise NotImplementedError("This operation is not supported for queues")

    def get_currency(self, *args, **kwargs):
        """Disable the get_currency method."""
        raise NotImplementedError("This operation is not supported for queues")

    # ----------------- Destructor ----------------- #
    def __del__(self):
        """Destructor to clean up the queue."""
        self.destroy_queue()

    def __repr__(self):
        """String representation of the queue."""
        front_data = self.peek_front() if not self.is_list_empty() else None
        rear_data = self.peek_rear() if not self.is_list_empty() else None
        return f"Queue(front={front_data}, rear={rear_data}, size={self.get_count()})"