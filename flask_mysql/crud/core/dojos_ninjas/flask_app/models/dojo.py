from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app.models.ninja import ninja
class dojo:
    def __init__(self,data) :
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

        self.ninjas=[]
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
    @classmethod
    def get_dojos_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"      
        results = connectToMySQL(DB).query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            ninjaa = {
                'id': row['id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            dojo.ninjas.append( ninja(ninjaa) )
        return dojo