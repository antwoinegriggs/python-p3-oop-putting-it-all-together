#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def is_interger(self, page_count):
        if (type(page_count) is not int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count

    def get_pages(self):
        return self._page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(get_pages, is_interger)
