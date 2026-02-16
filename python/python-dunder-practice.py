class SmartList(list):
    """
    Learning Project: Customizing list behavior with dunder methods.
    """

    def __repr__(self):
        # Shows 'SmartList' name in the terminal instead of just brackets
        return f"SmartList({super().__repr__()})"

    def __add__(self, other):
        # Check if lists have the same size before adding
        if len(self) != len(other):
            raise ValueError("Error: Lists must have the same length for this operation.")
        return SmartList(x + y for x, y in zip(self, other))

    def __sub__(self, other):
        # Element-wise subtraction
        if len(self) != len(other):
            raise ValueError("Error: Lists must have the same length for this operation.")
        return SmartList(x - y for x, y in zip(self, other))

    def __eq__(self, other):
        # Equality check based on the total sum of elements
        return sum(self) == sum(other)

    def __abs__(self):
        # Converting all negative values to positive
        return SmartList(abs(x) for x in self)

# Testing the logic
if __name__ == "__main__":
    list_a = SmartList([1, 2, -9])
    list_b = SmartList([-4, 5, 6])

    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Sums are equal: {list_a == list_b}")
    print(f"Absolute version of B: {abs(list_b)}")
    
    try:
        result = list_a + list_b
        print(f"Addition result: {result}")
    except ValueError as e:
        print(e)
