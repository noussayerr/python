from flask import Flask,render_template
app=Flask(__name__)

@app.route('/play')
def play1():
    return render_template("index.html", rep=3,wcolor='blue')
@app.route('/play/<int:x>')
def playx (x):
    return render_template("index.html",rep=x , wcolor='blue')
@app.route('/play/<int:x>/<string:color>')
def play_color(x,color):
    return render_template("index.html", rep=x , wcolor=color)
if __name__=="__main__" :
    app.run(debug=True)