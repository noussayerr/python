from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def Checkerboard_8_8():
    return render_template("index.html",x=8,y=8,color1="black",color2="red")

@app.route('/4')
def Checkerboard_8_4():
    return render_template("index.html",x=8,y=4,color1="black",color2="red")

@app.route('/<int:x>/<int:y>')
def Checkerboard_x_y(x,y):
    return render_template("index.html",x=x,y=y,color1="black",color2="red")

@app.route('/<int:x>')
def Checkerboard_x(x):
    return render_template("index.html",x=x,y=x,color1="black",color2="red")

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def Checkerboard_x_y_color(x,y,color1,color2):
    return render_template("index.html",x=x,y=y,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)