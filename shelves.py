#shelves on which to store books

class Future_read:
    def __init__(self, to_read_books):
        self.to_read_books = to_read_books

class Now_reading:
    def __init__(self, reading):
        self.reading = reading

class Past_read:
    def __init__(self, book_read):
        #completed doesn't mean the entire book was read, necessarially, just that you won't be reading anymore, ever
        self.book_read = book_read

