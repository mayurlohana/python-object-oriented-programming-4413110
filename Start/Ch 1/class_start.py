# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK')
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def get_book_types(self):
        return self.BOOK_TYPES

    # TODO: create a static method
    def get_book_list():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print('Book Types: ', Book.get_book_types())

# TODO: Create some book instances
book1 = Book("The Rich Dad, Poor Dad", "HARDCOVER")
book2 = Book('Atomic Habits', "PAPERBACK")

# TODO: Use the static method to access a singleton object
books = Book.get_book_list()
books.append(book1)
books.append(book2)
print(books)