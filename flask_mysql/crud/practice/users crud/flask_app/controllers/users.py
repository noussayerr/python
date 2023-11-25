from flask_app.models.user import user
from flask import render_template , request, redirect
from flask_app import app

@app.route('/users')
def index():
    user_list=user.get_all()
    return render_template("index.html",users=user_list)
@app.route('/user/new')
def nuser():
    return render_template("new_user.html")

@app.route('/new',methods=["POST"])
def add_user():
    data=request.form
    user.add_user(data)
    return redirect('/users')
@app.route('/show/<int:id>')
def show(id):
    data = {'id': id}
    show_user=user.get_user_by_id(data)
    return render_template("show_user.html",show_user=show_user)
@app.route('/delete/<int:id>')
def sup(id):
    data = {'id': id}
    user.sup(data)
    return redirect('/users')
@app.route('/update/<int:id>')
def user_update(id):
    data = {'id': id}
    user_update=user.get_user_by_id(data)
    return render_template('update.html',user_update=user_update)

@app.route('/update/user',methods=['POST'])
def update():
    data = request.form
    user.edit(data)
    return redirect('/users')