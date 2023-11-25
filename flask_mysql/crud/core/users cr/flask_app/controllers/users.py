from flask_app.models.user import user
from flask import render_template , request, redirect
from flask_app import app

@app.route('/users')
def index():
    user_list=user.get_all()
    return render_template("index.html",users=user_list)
@app.route('/user/new')
def adduser():
    return render_template("new_user.html")

@app.route('/new' ,  methods = ["POST"])
def add_user():
    data=request.form
    user.add_user(data)
    return redirect('/users')
