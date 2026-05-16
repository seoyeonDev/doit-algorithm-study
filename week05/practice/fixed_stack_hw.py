from typing import Any

class FixedStack:
    # Custom exceptions for stack overflow and underflow
    class StackFullError(Exception):
        pass

    # Custom exception for stack underflow
    class StackEmptyError(Exception):
        pass
    
    # Initialize the stack with a fixed capacity
    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    # Push an item onto the stack
    def __len__(self) -> int:
        return self.ptr

    # Push an item onto the stack
    def is_empty(self) -> bool:
        return self.ptr <= 0

    # Push an item onto the stack
    def is_full(self) -> bool:
        return self.ptr >= self.capacity
   
    # Push an item onto the stack
    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    # Pop an item from the stack
    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    # Peek at the top item of the stack without removing it
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    # Clear the stack
    def clear(self) -> None:
        self.ptr = 0 

    # Find the index of a value in the stack
    def find(self, value: Any) -> int:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    # Count the occurrences of a value in the stack
    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    # Check if the stack contains a value
    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0

    # Dump the contents of the stack
    def dump(self) -> None:
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])