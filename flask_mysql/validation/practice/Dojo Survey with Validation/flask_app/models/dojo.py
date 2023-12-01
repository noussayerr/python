from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask import flash
class dojo:
    def __init__(self,data) :
        self.id=data['id']
        self.name=data['name']
        self.location=data['location']
        self.language=data['language']
        self.comment=data['comment']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def create(cls,data):
        query="insert into dojos (name,location,language,comment) values (%(name)s,%(location)s,%(language)s,%(comment)s);"
        results=connectToMySQL(DB).query_db(query, data)
        return results
    @classmethod
    def show(cls):
        query="SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results=connectToMySQL(DB).query_db(query)
        return dojo (results[0])
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if dojo['location'] == "select location":
            flash("you must choose location.")
            is_valid = False
        if dojo['language'] =="select language":
            flash("you must choose language.")
            is_valid = False
        return is_valid