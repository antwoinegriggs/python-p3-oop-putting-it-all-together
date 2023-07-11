#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def is_interger(self, size):
        if (type(size) is int):
            self._size = size
        else:
            print("size must be an integer")

    def get_size(self):
        return self._size

    def cobble(self, condition="new"):
        self.condition = "New"
        print(f"Your shoe is as good as {condition}!")

    size = property(get_size, is_interger)
