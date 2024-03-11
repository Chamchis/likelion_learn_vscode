class CPU:
    def __init__(self,brand) -> None:
        self.brand = brand
class Computer:
    def __init__(self,cpu) -> None:
        self.cpu = cpu

computer1 = Computer(CPU(brand='AMD'))
cpu = CPU(brand='AMD')
computer2 = Computer(CPU)

class Book:
    def __init__(self,title) -> None:
        self.title = title
class Library:
    def __init__(self) -> None:
        self.books = []
    def add_book(self,book):
        self.books.append(book)
book1 = Book('Python Backend')
book2 = Book('Rising Sun')
library = Library()
library.add_book(book1)
Library().add_book(book2)