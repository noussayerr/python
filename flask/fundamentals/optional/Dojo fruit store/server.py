from flask import Flask , render_template ,request ,redirect
from datetime import date
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    today = date.today()
    data=request.form
    strawberry=data['strawberry']
    raspberry=data['raspberry']
    apple=data['apple']
    first_name=data['first_name']
    last_name=data['last_name']
    student_id=data['student_id']
    fruits=int(strawberry)+int(raspberry)+int(apple)
    return render_template("checkout.html",strawberry=strawberry,raspberry=raspberry,apple=apple
                           ,first_name=first_name,last_name=last_name,student_id=student_id,today=today,fruits=fruits)

if __name__=="__main__":
    app.run(debug=True)