from lab2_mb.currency_calculator import Currency

# class link_node:
#     def __init__(self, data, next):
#         self._data = data
#         self._next = next

# currency1 = Currency()
# node1=link_node(currency1)

class link_node:
    def __init__(self, currency):
        self._data = currency
        self._next = None
