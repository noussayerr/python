from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app.models import author

class Book:
    def __init__(self,data) :
        self.id=data['id']
        self.title=data['title']
        self.num_of_pages=data['num_of_pages']
        self.email=data['created_at']
        self.updated_at=data['updated_at']

        self.authors=[]
    @classmethod
    def add_book(cls,data):
        query="insert into books (title ,num_of_pages) values (%(title)s,%(num_of_pages)s);"
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def show(cls):
        query="select * from books ;"
        result= connectToMySQL(DB).query_db(query)
        print("@"*10)
        print(result)
        books=[]
        for row in result:
            book=cls(row)
            books.append(book)
        return books
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL('books').query_db(query,data)

        book = cls(results[0])

        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.authors.append(author.Author(data))
        return book

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL('books').query_db(query,data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books