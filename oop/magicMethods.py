# Magic Methods = Dunder methods 
# They are automatically called by many of Python's built-in operations.
# They allow developers to define or customize the behavior of objects.

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self): # instead of return a memory adress when print(book1) you can customize the message.
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other): # it customize the condition when you print a boolean condition.
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other): # less than.
        return self.num_pages < other.num_pages # We're building a new rule here when we're comparing book1.num_pages to book2.num_pages
    def __gt__(self, other): # greater than, you know what to do
        pass

    def __add__(self, other): # what will happen when you add a book to another
        pass

    def __contains__(self, keyword): # it might be useful for search
        return keyword in self.title

    # i would recommend you studying this in more depth later.
    
book1 = Book("test", "me", "3") # It automatically calls the init method.
book2 = Book("test", "me", "3")
print(book1 < book2) # Now it'll print the __str__ customization

