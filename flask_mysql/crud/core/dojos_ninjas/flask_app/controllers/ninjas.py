from flask_app.models.dojo import dojo
from flask_app.models.ninja import ninja
from flask import render_template , request, redirect
from flask_app import app

@app.route('/dojos')
def index():
    dojos_list=dojo.show()
    return render_template("index.html",dojos=dojos_list)
@app.route('/new_dojo',methods=['POST'])
def new_dojo():
    data=request.form
    dojo.new_dojo(data)
    return redirect('/dojos')
@app.route('/new_ninja')
def add_ninja_page():
    dojos_list=dojo.show()
    return render_template("new_ninja.html",dojos=dojos_list)

@app.route('/new/ninja',methods=['POST'])
def new_ninja():
    data=request.form
    ninja.add_user(data)
    return redirect('/dojos')
@app.route('/ninjas/<dojo>')
def ninjas(dojo):
    data = {'name': dojo}
    ninjas_list=ninja.get_all(data)
    return render_template("dojos.html",ninjas_list=ninjas_list )
