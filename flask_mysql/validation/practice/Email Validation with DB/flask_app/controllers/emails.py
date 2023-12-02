from flask_app.models.email import email
from flask import render_template , request, redirect,session
from flask_app import app

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/add',methods=['POST'])
def add():
    data=request.form
    if not email.validate_email(data):
        return redirect('/')
    email.create(data)
    return redirect('/show')

@app.route('/show')
def show():
    emails=email.show()
    return render_template("show.html",emails=emails)
@app.route('/delete/<int:id>')
def delete(id):
    data={'id' : id}
    email.delete(data)
    return redirect('/show')