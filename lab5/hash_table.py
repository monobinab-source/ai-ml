from dollar import Dollar


class HashTable:
    def __init__(self, size=29):
        """
        Initialize the hash table with a given size.
        :param size: Initial size of the hash table.
        """
        self.size = size
        self.table = [None] * size
        self.count = 0  # Tracks the number of elements in the hash table
        self.collisions = 0

    def hash_function(self, dollar):
        """
        Hash function: (m * whole + n * fractional) % size
        :param dollar: Dollar object to hash.
        :return: Index in the hash table.
        """
        m = 2
        n = 3
        w = dollar.whole
        f = dollar.fractional
        return (m * w + n * f) % self.size

    def insert(self, dollar):
        """
        Insert a Dollar object into the hash table using quadratic probing for collision resolution.
        :param dollar: Dollar object to insert.
        """
        index = self.hash_function(dollar)
        original_index = index
        step = 1

        while self.table[index] is not None:
            self.collisions += 1
            index = (original_index + step ** 2) % self.size
            step += 1

        self.table[index] = dollar
        self.count += 1

        # Check and resize if load factor exceeds 0.75
        if self.load_factor() > 0.75:
            self.resize()

    def search(self, dollar):
        """
        Search for a Dollar object in the hash table.
        :param dollar: Dollar object to search for.
        :return: Index where the Dollar is found or -1 if not found.
        """
        index = self.hash_function(dollar)
        original_index = index
        step = 1

        while self.table[index] is not None:
            if self.table[index] == dollar:
                return index
            index = (original_index + step ** 2) % self.size
            step += 1
            if step > self.size:  # Prevent infinite loop
                break

        return -1

    def resize(self):
        """
        Resize the hash table when load factor exceeds 0.75.
        """
        old_table = self.table
        self.size *= 2  # Double the size
        self.table = [None] * self.size
        self.count = 0
        self.collisions = 0

        for item in old_table:
            if item is not None:
                self.insert(item)

    def load_factor(self):
        """
        Calculate the load factor of the hash table.
        :return: Load factor as a float.
        """
        return self.count / self.size

    def __repr__(self):
        """
        String representation of the hash table.
        :return: Formatted string showing the hash table.
        """
        return f"HashTable(size={self.size}, count={self.count}, collisions={self.collisions}, load_factor={self.load_factor():.2f})"

    def print_table(self):
        """
        Print the current state of the hash table.
        """
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")
