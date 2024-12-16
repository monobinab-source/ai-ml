"""
Author: Haoyun Luo & Monobina Saha
CIS 22C Lab 2
"""

from abc import ABC, abstractmethod

class Currency(ABC):
    def __init__(self, value: float = 0):
        if value < 0:
                raise ValueError("Currency value must be greater than 0.")
        self.whole_part = int(value)
        self.fractional_part = round((value - self.whole_part)*100)           

    # copy constructor
    def __copy__(self):
        return type(self)(self.whole_part + self.fractional_part/100)
    
    """
    Getter method for the whole_part attribute of the object
    Pre: 
    Post:
    Return: value of whole_part
    """
    def get_whole_part(self):
        return self.whole_part
    
    """
    Getter method for the fractional_part attribute of the object
    Pre:
    Post: 
    Return: value of fractional_part
    """
    def get_fractional_part(self):
        return self.fractional_part
    
    """
    Setter method for the whole_part attribute of the object
    Pre: whole_part - new value for whole_part that is a non-negative integer
    post: self.whole_part is set to the given value of whole_part, or value error is thrown for incorrect value of whole_part
    Return:
    """
    def set_whole_part(self, whole_part: int):
        if whole_part < 0:
            raise ValueError("Whole part cannot be negative.")
        
        if not isinstance(whole_part, int):
            raise ValueError("Whole part must be an integer.")
            
        self.whole_part = whole_part
        
    """
    Setter method for the fractional_part attribute of the object
    Pre: fractional_part - new value for fractional part that is an integer between the range of 0 and 100
    Post: self.fractional_part is set to the given value of fractional_part, or value error is thrown for incorrect value of fractional_part
    Return:
    """
    def set_fractional_part(self, fractional_part: int):
        if fractional_part < 0 or fractional_part > 100:
            raise ValueError("Fractional part cannot be negative or greater than 100.")
        
        if not isinstance(fractional_part, int):
            raise ValueError("Fractional part must be an integer.")
        
        self.fractional_part = fractional_part
        
    """
    Getter method for the name of the currency
    Pre:
    Post:
    Return: name of the currency
    """
    @abstractmethod
    def get_currency_name(self):
        pass
    
    """
    Add the value of another currency object to this instance of the class
    Pre: other - another currency object whose value will be added, must be the same type of currency
    Post: self.whole_part and self.fractional_part are increased after the addition, or type error is thrown for adding another type of currency
    Return:
    """
    def add(self, other):
        if self.get_currency_name() != other.get_currency_name():
            raise TypeError("Invalid addition.")
        
        total_fractional = self.fractional_part + other.fractional_part
        total_whole = self.whole_part + other.whole_part + int(total_fractional/100)
        
        self.whole_part = total_whole
        self.fractional_part = total_fractional%100
        
    """
    Subtract the value of another currency object from this instance of the class
    Pre: other - another currency object whose value will be subtracted from this instance, must be the same type of currency
    Post: self.whole_part and self.fractional_part are decreased after the subtraction, or type error is thrown for subtracting another type of currency, or value error is thrown if the subtraction results in a negative total value
    Return: 
    """
    def subtract(self, other):
        if self.get_currency_name() != other.get_currency_name():
            raise TypeError("Invalid subtraction.")
        
        if not self.is_greater(other) and not self.is_equal(other):
            raise ValueError("Invalid subtraction.")
        
        fractional_difference = self.fractional_part - other.fractional_part
        whole_difference = self.whole_part - other.whole_part
        
        if fractional_difference < 0:
            fractional_difference += 100
            whole_difference -= 1
            
        self.whole_part = whole_difference
        self.fractional_part = fractional_difference
        
    """
    Check if another currency object of the same type has the same value as this instance
    Pre: other - another currency object to compare against
    Post: type error is thrown for comparing different types of currency
    Return: true or false
    """
    def is_equal(self, other):
        if self.get_currency_name() != other.get_currency_name():
            raise TypeError("Cannot compare different currencies.")
        
        return self.whole_part == other.whole_part and self.fractional_part == other.fractional_part
    
    """
    Check if this instance has greater total value than another currency object
    Pre: other - another currency object to compare against
    Post: type error is thrown for comparing different types of currency
    Return: true or false
    """
    def is_greater(self, other):
        if self.get_currency_name() != other.get_currency_name():
            raise TypeError("Cannot compare different currencies.")
        
        return (self.whole_part*100 + self.fractional_part) > (other.whole_part*100 + other.fractional_part)
    
    """
    Give a string representation of this instance of the class
    Pre:
    Post:
    Return: a string representation of this instance of the class
    """
    def to_string(self):
        decimal_str = str(self.fractional_part) if self.fractional_part != 0 else str(self.fractional_part) + "0" 
        return str(self.whole_part) + "." + decimal_str + " " + self.get_currency_name()
    
    """
    Print the string representation of this instance of the class
    Pre:
    Post: the string representation of this instance of the class is printed
    Return: 
    """
    def print(self):
        print(self.to_string(), end=" ")