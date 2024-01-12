#shelves on which to store books

from typing import Any


class to_read:
    def __init__(self, to_read_books):
        self.to_read_books = to_read_books

class currently_reading:
    def __init__(self, reading):
        self.reading = reading

class completed_books:
    def __init__(self, book_read):
        #completed doesn't mean the entire book was read, necessarially, just that you won't be reading anymore, ever
        self.book_read = book_read
