# Magic Methods => also known as dunder methods , dunder means two underscores, they are typically found in classes ,They are automatically called by many of the pythons built-in operations, They allow developers to define and customize the behavior of objects


class Book:
    def __init__(self,title,author,num_of_pages):
        self.title=title;
        self.author=author;
        self.num_of_pages=num_of_pages;
    # This gives output or memory addr if this ___str__() is not present
    """_str__ is used to provide a readable string representation of an object, mainly intended for end-users."""
    def __str__(self):
        return f"{self.title} by {self.author}"
    """__repr__  compared to __str is more for developers and is aimed at providing an "official" string representation of the object."""
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', num_of_pages={self.num_of_pages})"
    # To check if book one and other has same name and author
    def __eq__(self,other):
        return self.author == other.author and self.title ==other.title
    # To check if book and other book have less than pages 
    def __lt__(self,other):
        return self.num_of_pages <other.num_of_pages
    # To check if book and other book have lgreater than pages 
    def __gt__(self,other):
        return self.num_of_pages>other.num_of_pages
    # To check if a keyword is in author or title
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    # getting some attribute in this pattern book['title' or 'author' or 'num_of_pages']
    def __getitem__(self,key):
        if key =="title":
            return self.title
        elif key =="author":
            return self.author
        elif key=="num_of_pages":
            return self.num_of_pages
        else:
            return f"'Key {key} was not found'"
    # Adding page numbers of two books
    def __add__(self,other):
        return f"{self.num_of_pages +other.num_of_pages} Pages"
# Instances and callings
book1=Book("Mr Robot","Sheikh Feroz",121)
book2=Book("Robo cop","Imran",221)
book3=Book("Mr Robot","Sheikh Feroz",421)
print(book1)
print(book1==book3)
print(book2<book3)
print(book3>book2)
print("Sheikh"in book1)
print(book1["num_of_pages"])
print(book1+book2)
print(repr(book1))