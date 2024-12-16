class Dollar:
    def __init__(self, amount):
        self.whole = int(amount)
        self.fractional = int(round((amount - self.whole) * 100))

    def value(self):
        """Calculate the total monetary value."""
        return self.whole + self.fractional / 100.0

    def __lt__(self, other):
        return self.value() < other.value()

    def __eq__(self, other):
        return self.value() == other.value()

    def __repr__(self):
        return f"${self.whole}.{self.fractional:02d}"

