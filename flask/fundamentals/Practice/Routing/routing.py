from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
##
@app.route('/dojo')
def dojo():
    return 'dojo'
##
@app.route('/say/<name>')
def say(name):
    return f'Hy {name}! '
@app.route('/repeat/<int:nbr>/<name>')
def repeat(nbr,name):
    res=''
    for i in range(nbr):    
        res +=f'{name}<br>'
    return res
if __name__=="__main__" :
    app.run(debug=True)