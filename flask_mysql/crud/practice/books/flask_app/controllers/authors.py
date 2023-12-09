from flask_app.models.author import Author
from flask_app.models.book import Book
from flask import render_template , request, redirect
from flask_app import app

@app.route('/')
def main():
    return redirect('/authors')

@app.route('/authors')
def index():
    authors_list=Author.show()
    return render_template("index.html",authors=authors_list)

@app.route('/new_author',methods=['POST'])
def new_author():
    data=request.form
    Author.add_author(data)
    return redirect('/authors')

@app.route('/author/<int:id>')
def author_with_id(id):
    data={'id' : id}
    unfavorited_books=Book.unfavorited_books(data)
    get_by_id=Author.get_by_id(data)
    return render_template("author.html",unfavorited_books=unfavorited_books,get_by_id=get_by_id)

@app.route('/add_favorited',methods=['POST'])
def new_fav():
    data=request.form
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")