
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print("Base class constructor called.")

    def display_info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")



class EBook(Book):
    def __init__(self, title, author, file_size):
        
        super().__init__(title, author)
        self.file_size = file_size
        print("Derived class constructor called.")

    
    def display_info(self):
        
        super().display_info()
        print(f"File Size: {self.file_size} MB")



print("Creating a Book object:")
book1 = Book("The Alchemist", "Paulo Coelho")
book1.display_info()

print("\nCreating an EBook object:")
ebook1 = EBook("Python Programming", "John Zelle", 5)
ebook1.display_info()
