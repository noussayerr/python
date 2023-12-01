from flask_app.models.ninja import ninja
from flask import render_template , request, redirect
from flask_app import app

@app.route('/new/ninja',methods=['POST'])
def new_ninja():
    data=request.form
    ninja.add_user(data)
    return redirect('/dojos')
