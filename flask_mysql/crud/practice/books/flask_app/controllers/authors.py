from flask_app.models.author import author
from flask import render_template , request, redirect
from flask_app import app

@app.route('/authors')
def index():
    authors_list=author.show()
    return render_template("index.html",authors=authors_list)

@app.route('/new_author',methods=['POST'])
def new_author():
    data=request.form
    author.add_author(data)
    return redirect('/authors')
