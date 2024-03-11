from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(11,22)
print(p)

Employee = namedtuple('Employee',['name','age','country'])
employee1 = Employee('James',21,'Canada')
print(employee1)

print(employee1._asdict())

from collections import namedtuple

# Book namedtuple 생성
Book = namedtuple('Book', ['title', 'author', 'genre'])

# Book 객체 리스트 생성
books = [
    Book('The Hitchhiker\'s Guide to the Galaxy', 'Douglas Adams', 'Science Fiction'),
    Book('The Lord of the Rings', 'J. R. R. Tolkien', 'Fantasy'),
    Book('Pride and Prejudice', 'Jane Austen', 'Romance')
]

# 특정 장르의 책 찾기
for book in books:
    if book.genre == 'Science Fiction':
        print(book.title)  # The Hitchhiker's Guide to the Galaxy 출력

# 책 정렬
sorted_books = sorted(books, key=lambda book: book.author)

# 정렬된 책 출력
for book in sorted_books:
    print(book)

