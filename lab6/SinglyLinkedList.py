"""
Author: Haoyun Luo & Monobina Saha
CIS 22C Lab 3
"""

from Currency import Currency


class LinkNode:
    def __init__(self, data: Currency):
        self.data = data
        self.next: LinkNode | None = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.count = 0
        self.start: LinkNode | None = None
        self.end: LinkNode | None = None

    """
    Getter method for the number of nodes
    Pre: 
    Post: 
    Return: the number of nodes in the list
    """
    def get_count(self) -> int:
        return self.count

    """
    Getter method for the head node's data
    Pre:
    Post:
    Return: the currency object located at the head node
    """
    def get_start(self):
        return self.start.data

    """
    Getter method for the last node's data
    Pre:
    Post:
    Return: the currency object located at the end node
    """
    def get_end(self):
        return self.end.data

    """
    Destructor for the list
    Pre:
    Post: all of the nodes in the list are dereferenced and deleted
    Return: 
    """
    def __del__(self):
        current_node = self.start
        while current_node is not None:
            next_node = current_node.next
            del current_node
            current_node = next_node
        self.start = None
        self.end = None

    """
    Add a currency object to the list at the given index
    Pre:    currency - reference to a currency object to be added to the list
            index - a valid index to which to add the currency object to 
    Post: the currency object is added to the list at the given index, and all references (next node, head node, and end node) are updated as necessary; or index error is thrown for negative, non-integer, or out of bounds index.
    Return: 
    """
    def add_currency(self, currency: Currency, index: int):
        if index < 0 or not isinstance(index, int):
            raise IndexError("Index must be a positive integer.")

        new_node = LinkNode(currency)

        if index == 0:
            # adding to the head of the linked list
            new_node.next = self.start
            self.start = new_node

            self.count += 1

            # if the list was previously empty
            if self.end is None:
                self.end = new_node

        else:
            # adding to the middle or end of the list
            current_index = 0
            current_node = self.start

            # get to the node before the insertion index
            while current_index < index - 1:
                if current_node is None:
                    # reached end of the list before index
                    raise IndexError("Invalid index.")
                current_node = current_node.next
                current_index += 1

            if current_node is None:
                # trying to add to one index after the end of the list
                raise IndexError("Invalid index.")

            new_node.next = current_node.next
            current_node.next = new_node

            self.count += 1

            # if the insertion was made at the end of the list
            if new_node.next is None:
                self.end = new_node

    """
    Remove the provided currency object from the list or remove the currency object at a certain index (overloaded method)
    Pre: currency_or_index: a currency object to remove from the list or a valid index at which to remove a currency object
    Post: the provided currency object or index is removed from the list, and all references (next node, head node, and end node) are updated as necessary; or value error is thrown if there is no object in the list matching the provided object to remove; or index error is thrown for negative, non-integer, or out of bounds index.
    Return: a copy of the currency object that was removed
    """
    # pseudo method overloading in python using parameter type
    def remove_currency(self, currency_or_index: Currency | int) -> Currency:
        # list is empty
        if self.start is None:
            raise IndexError("The list is empty.")

        current_index = 0
        current_node = self.start
        # for overloading
        if isinstance(currency_or_index, Currency):
            # case 1: the node to remove is the head node
            if current_node.data.is_equal(currency_or_index):
                removed_currency = current_node.data
                self.start = self.start.next

                # if the node removed was also the end node (original length = 1)
                if self.start is None:
                    self.end = None

                self.count -= 1
                return removed_currency

            # case 2: the node to remove is in the middle or at the end
            while current_node.next is not None:
                if current_node.next.data.is_equal(currency_or_index):
                    # found the node to remove
                    removed_currency = current_node.next.data
                    current_node.next = current_node.next.next

                    # the node removed was the end node
                    if current_node.next is None:
                        self.end = current_node

                    self.count -= 1
                    return removed_currency

                current_node = current_node.next

            raise ValueError("Currency object is not in the list.")

        # overloaded method for index
        elif isinstance(currency_or_index, int):
            if currency_or_index < 0:
                raise IndexError("Index must be a positive integer.")
            # case 1: the node to remove is the head node
            if currency_or_index == 0:
                removed_currency = current_node.data
                self.start = self.start.next

                # if the node removed was also the end node (original length = 1)
                if self.start is None:
                    self.end = None

                self.count -= 1
                return removed_currency

            # case 2: the node to remove is in the middle or at the end
            while current_index < currency_or_index - 1:
                if current_node.next is None:
                    raise IndexError("Invalid index.")
                current_node = current_node.next
                current_index += 1

            if current_node.next is None:
                # the node to remove is None
                raise IndexError("Invalid index.")
            removed_currency = current_node.next.data

            # remove the target node
            current_node.next = current_node.next.next

            # the node removed was the end node
            if current_node.next is None:
                self.end = current_node

            self.count -= 1
            return removed_currency

        else:
            raise TypeError(
                "parameter for remove_currency must either be Currency object or integer index to remove."
            )

    """
    Find the index of a given currency object in the list
    Pre:    currency - a currency object to search for 
    Post: 
    Return: the index of the given currency object in the list, or -1 if a matching currency object is not found
    """
    def find_currency(self, currency: Currency) -> int:
        current_node = self.start
        current_index = 0

        while current_node is not None:
            if current_node.data.is_equal(currency):
                return current_index
            current_node = current_node.next
            current_index += 1
        # not found
        return -1

    """
    Get the data of the node at a certain index
    Pre: index - a valid index in the list
    Post: index error is thrown for negative, non-integer, or out of bounds index.
    Return: the currency object located at the node at the given index
    """
    def get_currency(self, index: int) -> Currency:
        if not isinstance(index, int) or index < 0:
            raise IndexError("Invalid index.")
        current_node = self.start
        current_index = 0
        while current_index < index:
            if current_node is None:
                raise IndexError("Invalid index.")
            current_node = current_node.next
            current_index += 1

        if current_node is None:
            raise IndexError("Invalid index.")

        return current_node.data

    """
    Give a string representation of the list of currency objects
    Pre:
    Post:
    Return: a string representation of the list of currency objects, with each one separated by a tab
    """
    def print_list(self) -> str:
        current_node = self.start
        return_string = ""
        while current_node is not None:
            return_string += current_node.data.to_string() + "\t"
            current_node = current_node.next

        return return_string

    """
    Check if the list is empty
    Pre:
    Post:
    Return: true or false for whether the list is empty
    """
    def is_list_empty(self) -> bool:
        return self.count == 0
