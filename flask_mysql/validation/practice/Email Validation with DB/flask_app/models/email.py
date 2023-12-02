from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class email:
    def __init__(self,data) :
        self.id=data['id']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def create(cls,data):
        query="insert into emails (email) values (%(email)s);"
        results=connectToMySQL(DB).query_db(query, data)
        return results
    @classmethod
    def show(cls):
        query="SELECT * FROM emails;"
        results=connectToMySQL(DB).query_db(query)
        emails=[]
        for row in results:
            email=cls(row)
            emails.append(email)
        return emails 
    @classmethod
    def get_by_email(cls , data):
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query , data)
        if result:
            return cls(result[0])
        return False
    @classmethod
    def delete(cls,data):
        query="delete from emails where id=(%(id)s);"
        results=connectToMySQL(DB).query_db(query, data)
        return results
    @staticmethod
    def validate_email(data):
        is_valid = True 
        email_in_db = email.get_by_email(data)
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if email_in_db:
            flash("A user with the provided email already exists.")
            is_valid = False
        return is_valid