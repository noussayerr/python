from flask_app.models.user import user
from flask import render_template , request, redirect,session
from flask_app import app

@app.route('/')
def index():
    return render_template("login_registration.html")
@app.route('/register' , methods=['POST'])
def register():
    data = request.form
    if user.validate_register(data):
        user.create(data)
    return redirect('/')
@app.route('/login' , methods = ['POST'])
def login():
    data = request.form
    print(data)
    if user.validate_login(data):
        session['logged_user_email'] = data['email']
        print(session['logged_user_email'])
        return redirect('/dashboard')
    
    return redirect('/')
@app.route('/dashboard')
def dashboard():
    logged_user = user.get_by_email({'email': session['logged_user_email']})
    return render_template('dashboard.html' , logged_user = logged_user)
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')