from flask_app.models.dojo import dojo
from flask import render_template , request, redirect,session
from flask_app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add',methods=['POST'])
def add():
    data=request.form
    if not dojo.validate_dojo(data):
        return redirect('/')
    dojo.create(data)
    return redirect('/show')

@app.route('/show')
def show():
    dojoo=dojo.show()
    return render_template("show.html",dojoo=dojoo)