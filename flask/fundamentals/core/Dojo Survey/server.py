from flask import Flask,render_template,redirect,request,session

app=Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result',methods=['POST'])
def result():
    data=request.form
    session['name']=data['name']
    session['location']=data['location']
    session['language']=data['language']
    session['comments']=data['comments']
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)