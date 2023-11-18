from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)

app.secret_key="rahal"
@app.route('/')
def count():
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=0
    return render_template("index.html")  
@app.route('/reset')
def reset():
    session.pop('count')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)