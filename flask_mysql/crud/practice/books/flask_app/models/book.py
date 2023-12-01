from flask_app.config.mysqlconnection import connectToMySQL, DB

class book:
    def __init__(self,data) :
        self.id=data['id']
        self.first_name=data['title']
        self.last_name=data['num_of_pages']
        self.email=data['created_at']
        self.updated_at=data['updated_at']

    """@classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        results=connectToMySQL(DB).query_db(query)
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    @classmethod
    def add_user(cls,data):
        query = "insert into user (first_name,last_name,email) values (%(first_name)s , %(last_name)s , %(email)s);"
        results=connectToMySQL(DB).query_db(query,data)
        return results
    @classmethod
    def get_user_by_id(cls,data):
        query="select * from user where id = %(id)s;"
        results=connectToMySQL(DB).query_db(query,data)
        user = None
        if results != []:
            user = cls(results[0])
        return user
    @classmethod
    def edit(cls,data):
        query="UPDATE user SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s ,updated_at=Now() WHERE id = (%(id)s);"
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def sup(cls,data):
        query="delete from user where id= %(id)s;"
        return connectToMySQL(DB).query_db(query,data) 