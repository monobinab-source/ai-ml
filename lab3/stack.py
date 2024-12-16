from singly_linked_list import SinglyLinkedList
from link_node import link_node

class Stack(SinglyLinkedList):
    def __init__(self):
        """Constructor to initialize an empty stack."""
        super().__init__()  # Call the parent class constructor

    # ----------------- Optional Stack Creation/Destruction Methods ----------------- #
    def create_stack(self):
        """Optional method to reset the stack."""
        self.create_list()

    def destroy_stack(self):
        """Optional method to clear the stack."""
        self.destroy_list()

    # ----------------- Stack Methods ----------------- #
    def push(self, currency):
        """
        Pushes a Currency object onto the top of the stack.

        :param currency: A Currency object to be added.
        """
        new_node = link_node(currency)
        if self.is_list_empty():
            self.set_head(new_node)
            self.set_tail(new_node)
        else:
            new_node.next = self.get_head()
            self.set_head(new_node)
        self.set_count(self.get_count() + 1)

    def pop(self):
        """
        Removes and returns the Currency object from the top of the stack.

        :return: The Currency object from the top of the stack.
        """
        if self.is_list_empty():
            raise IndexError("Pop from empty stack")

        top_node = self.get_head()
        self.set_head(top_node.next)
        if self.get_head() is None:  # If the stack becomes empty
            self.set_tail(None)

        self.set_count(self.get_count() - 1)
        return top_node.data  # Return the removed currency

    def peek(self):
        """
        Returns the Currency object from the top of the stack without removing it.

        :return: A copy of the Currency object at the top of the stack.
        """
        if self.is_list_empty():
            raise IndexError("Peek from empty stack")

        return self.get_head().data

    def print_stack(self):
        """
        Returns a string representation of the stack contents from top to bottom, tab-spaced.
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
        raise NotImplementedError("Use push() to add elements to the stack")

    def remove_currency(self, *args, **kwargs):
        """Disable the remove_currency method."""
        raise NotImplementedError("Use pop() to remove elements from the stack")

    def remove_currency_by_index(self, *args, **kwargs):
        """Disable the remove_currency_by_index method."""
        raise NotImplementedError("Use pop() to remove elements from the stack")

    def find_currency(self, *args, **kwargs):
        """Disable the find_currency method."""
        raise NotImplementedError("This operation is not supported for stacks")

    def get_currency(self, *args, **kwargs):
        """Disable the get_currency method."""
        raise NotImplementedError("This operation is not supported for stacks")
