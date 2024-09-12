class Stack:
    def __init__(self, items=None, limit=None):
        """
        Initializes a new stack with optional initial items and an optional limit.
        If a limit is provided, the stack cannot exceed that size.
        """
        self.items = items if items else []  # Initialize stack with given items or an empty list
        self.limit = limit  # Optional stack limit

    def push(self, value):
        """
        Pushes a new value onto the stack if it is not full.
        Throws an error if the stack is full.
        """
        if self.limit is not None and len(self.items) >= self.limit:
            raise OverflowError("Stack is full")
        self.items.append(value)

    def pop(self):
        """
        Removes and returns the top element from the stack.
        Returns None if the stack is empty instead of raising an error.
        """
        if self.isEmpty():
            return None  # Return None when the stack is empty
        return self.items.pop()

    def peek(self):
        """
        Returns the top element of the stack without removing it.
        Throws an error if the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def isEmpty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the number of elements currently in the stack.
        """
        return len(self.items)

    def full(self):
        """
        Returns True if the stack is full (only applicable if a limit is set), False otherwise.
        """
        if self.limit is None:
            return False  # If no limit, the stack can never be full
        return len(self.items) >= self.limit

    def search(self, value):
        """
        Returns the distance from the top of the stack to the target element if it's present, 
        otherwise returns -1.
        Distance is 0 if the element is at the top of the stack.
        """
        try:
            # Find the index of the value in the stack
            index = len(self.items) - 1 - self.items[::-1].index(value)
            # Return the distance from the top of the stack
            return len(self.items) - 1 - index
        except ValueError:
            return -1  # Return -1 if the value is not found
