class Book:

    def __init__(self, title, author, pages, to_read, currently_reading, have_read, on_shelf = True):
        self.title = title
        self.author = author
        self.pages = pages
        self.on_shelf = on_shelf
        self.to_read = False
        self.currently_reading = False
        self.have_read = False




    def percent_complete(self, pages_done):
        #calculates percent of the book that's done given current pages_done
        percent_through = pages_done/self.pages
        return percent_through

    def add_book(self):
        pass
        #user will be able to add a new book and have it added to the bookshelf list (to read)
    
    def update_book_status(self):
        pass
        #shifting shelving of book