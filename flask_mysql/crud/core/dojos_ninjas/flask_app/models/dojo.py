from flask_app.config.mysqlconnection import connectToMySQL, DB

class dojo:
    def __init__(self,data) :
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def new_dojo(cls,data):
        query="insert into dojos (name) values (%(name)s);"
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def show(cls):
        query="select * from dojos ;"
        result= connectToMySQL(DB).query_db(query)
        dojos=[]
        for row in result:
            dojo=cls(row)
            dojos.append(dojo)
        return dojos