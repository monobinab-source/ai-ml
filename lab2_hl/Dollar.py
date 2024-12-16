"""
Author: Haoyun Luo & Monobina Saha
CIS 22C Lab 2
"""

from Currency import Currency


class Dollar(Currency):
    def __init__(self, value: float = 0):
        super().__init__(value)
        self.name = "Dollar"
        
    """
    Getter method for the name of the currency
    Pre:
    Post:
    Return: name of the currency
    """
    def get_currency_name(self):
        return self.name
    