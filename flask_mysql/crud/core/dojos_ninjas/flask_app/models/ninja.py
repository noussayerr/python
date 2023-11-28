from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app.models.dojo import dojo
class ninja:
    def __init__(self,data) :
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
        self.dojo=[]
    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id where dojos.name=(%(name)s);"
        results = connectToMySQL(DB).query_db(query,data)
        ninjas = []
        if results != []:
            for row in results:
                ninja = cls(row)

                dojo_data = {
                    'id': row['id'],
                    'name': row['name'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at'],
                }

                ninja.dojo = dojo(dojo_data)
                ninjas.append(ninja)
        return results
        
        
    
    
    @classmethod
    def add_user(cls,data):
        query = "insert into ninjas (first_name,last_name,age,dojo_id) values (%(first_name)s , %(last_name)s , %(age)s,%(dojo_id)s);"
        return connectToMySQL(DB).query_db(query,data)
    