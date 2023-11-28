from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)

app.secret_key="rahal"
@app.route('/')
def index():
    return render_template("index.html") 
@app.route('/count')
def count():
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=0
    return render_template("index.html")  
@app.route('/destroy_route')
def reset():
    session.pop('count')
    session['count']=0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)