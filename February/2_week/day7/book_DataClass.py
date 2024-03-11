from dataclasses import dataclass
@dataclass
class Book:
    title : str
    author : str
    year_published : int
    price : int

book1 = Book('Python Backend','J.K.Rolling','1912',format(17000,','))
book2 = Book('Java Backend','Rising Sun','2021',format(61000,','))
book3 = Book('C Backend','Charlie','1877',format(8000,','))
book4 = Book('Programming','Lee','1999','라오')

print(book1,'\n',book2,'\n',book3,'\n',book4)