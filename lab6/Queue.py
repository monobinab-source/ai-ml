"""
Author: Haoyun Luo & Monobina Saha
CIS 22C Lab 3
"""

from Currency import Currency
from SinglyLinkedList import SinglyLinkedList

class Queue(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    """
    Add a currency object to the end of the queue
    Pre: currency - the currency object to add to the end of the queue
    Post: the currency object is added to the end of the queue
    Return: 
    """
    def enqueue(self, currency: Currency):
        super().add_currency(currency, super().get_count())

    """
    Remove the currency object at the from the front of the queue and returns a copy of it 
    Pre:
    Post: the currency object at the front of the queue is removed; or index error is thrown if the queue is previously empty
    Return: a copy of the currency object tat was removed
    """
    def dequeue(self):
        return super().remove_currency(0)

    """
    Get the currency object at the front of the queue
    Pre:
    Post: index error is thrown if the queue is empty
    Return: the currency object located at the front of the queue
    """
    def peek_front(self):
        return super().get_start()

    """
    Get the currency object at the end of the queue
    Pre:
    Post: index error is thrown if the queue is empty
    Return: the currency object located at the end of the queue
    """
    def peek_rear(self):
        return super().get_end()

    """
    Give a string representation of the queue of currency objects
    Pre:
    Post:
    Return: a string representation of the queue from front to end, with each one separated by a tab
    """
    def print_queue(self):
        return super().print_list()

    """
    Destructor for the queue
    Pre:
    Post: all the nodes of the underlying linked list are dereferenced and deleted
    Return:
    """
    def __del__(self):
        super().__del__()

    # to make sure the linked list methods cannot be used inside the Queue
    """
    Overridden methods from SinglyLinkedList to ensure they cannot be used on the Queue object
    Pre:
    Post: attribute error is thrown if the method is invoked
    Return: 
    """
    def get_start(self):
        raise AttributeError("Cannot use get_start on Queue.")

    def get_end(self):
        raise AttributeError("Cannot use get_end on Queue.")

    def add_currency(self):
        raise AttributeError("Cannot use add_currency on Queue.")

    def remove_currency(self):
        raise AttributeError("Cannot use remove_currency on Queue.")

    def find_currency(self):
        raise AttributeError("Cannot use find_currency on Queue.")

    def get_currency(self):
        raise AttributeError("Cannot use get_currency on Queue.")

    def print_list(self):
        raise AttributeError("Cannot use print_list on Queue.")

    def is_list_empty(self):
        raise AttributeError("Cannot use is_list_empty on Queue.")
