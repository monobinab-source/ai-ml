from lab3.link_node import link_node

class SinglyLinkedList:
    def __init__(self):
        """
        Initializes an empty singly linked list with private attributes.
        """
        self.__count = 0      # Track the number of nodes
        self.__head = None     # Pointer to the first node
        self.__tail = None     # Pointer to the last node

# getters/setters/constructors/destructors, as needed, for the attributes of the class.
    def get_count(self):
        return self.__count

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def set_head(self, node):
        if not isinstance(node, link_node):
            raise TypeError("Head must be link_node type.")
        self.__head = node

    def set_tail(self, node):
        if not isinstance(node, link_node):
            raise TypeError("Tail must be link_node type.")
        self.__tail = node

    def set_count(self, count):
        """
        Sets the number of nodes in the list.
        :param count: The new count value (must be non-negative).
        """
        if count < 0:
            raise ValueError("Count cannot be negative")
        self.__count = count

    def create_list(self):
        """Optional method to reset the list."""
        self.__init__()

    def destroy_list(self):
        """Optional method to clear the list."""
        while self.__head:
            temp = self.__head
            self.__head = self.__head.next
            del temp
        self.__count = 0
        self.__tail = None

    def add_currency(self, currency, index):
        """
        Adds a Currency object at the specified index.

        :param currency: A Currency object to be added.
        :param index: The position to insert the Currency.
        """
        new_node = link_node(currency)

        if index < 0 or index > self.__count:
            raise IndexError("Index out of bounds")

        if index == 0:  # Insert at the head
            new_node.next = self.__head
            self.__head = new_node
            if self.__count == 0:  # If the list was empty
                self.__tail = new_node
        elif index == self.__count:  # Insert at the tail
            self.__tail.next = new_node
            self.__tail = new_node
        else:  # Insert in the middle
            current = self.__head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.__count += 1

    def remove_currency(self, currency):
        """
        Removes a Currency object from the list, if present, and returns a copy of it.
        """
        current = self.__head
        previous = None

        while current:
            if current._data == currency:
                if previous is None:  # Removing head
                    self.__head = current.next
                    if self.__head is None:  # If list becomes empty
                        self.__tail = None
                else:  # Removing from middle or tail
                    previous.next = current.next
                    if current == self.__tail:
                        self.__tail = previous

                self.__count -= 1
                return current.data  # Return a copy of the removed currency
            previous = current
            current = current.next

        # raise ValueError("Currency not found in the list")
        print("Currency not found in the list")

    def remove_currency_by_index(self, index):
        """
        Removes the Currency object at the specified index and returns a copy of it.
        """
        if index < 0 or index >= self.__count:
            raise IndexError("Index out of bounds")

        current = self.__head
        previous = None

        for _ in range(index):
            previous = current
            current = current.next

        if previous is None:  # Removing the head
            self.__head = current.next
            if self.__head is None:  # If list becomes empty
                self.__tail = None
        else:  # Removing from middle or tail
            previous.next = current.next
            if current == self.__tail:
                self.__tail = previous

        self.__count -= 1
        return current._data  # Return a copy of the removed currency

    def find_currency(self, currency):
        """
        Finds the index of a Currency object in the list.

        :param currency: The Currency object to find.
        :return: The index of the Currency object, or -1 if not found.
        """
        current = self.__head
        index = 0

        while current:
            if current._data == currency:
                return index
            else:
                current = current.next
                index += 1

        return -1  # Not found

    def get_currency(self, index):
        """
        Returns the Currency object at the specified index.

        :param index: The index of the Currency object.
        :return: The Currency object at the specified index.
        """
        if index < 0 or index >= self.__count:
            raise IndexError("Index out of bounds")

        current = self.__head
        for _ in range(index):
            current = current.next

        return current.data

    def print_list(self):
        """
        Returns a string of all the Currency objects in the list, tab-spaced.
        """
        result = []
        current = self.__head

        while current:
            result.append(str(current.data))
            current = current.next

        return "\t".join(result)

    def is_list_empty(self):
        """Checks if the list is empty."""
        if self.__count == 0:
            return True
        else:
            return False

    def count_currency(self):
        """Returns the count of Currency nodes in the list."""
        return self.__count



