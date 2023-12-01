from flask_app.config.mysqlconnection import connectToMySQL, DB

class author:
    def __init__(self,data) :
        self.id=data['id']
        self.first_name=data['name']
        self.email=data['created_at']
        self.updated_at=data['updated_at']

        self.books=None
    @classmethod
    def add_author(cls,data):
        query="insert into authors (name) values (%(name)s);"
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def show(cls):
        query="select * from authors ;"
        result= connectToMySQL(DB).query_db(query)
        print("@"*10)
        print(result)
        authors=[]
        for row in result:
            author=cls(row)
            authors.append(author)
        return authors
    
