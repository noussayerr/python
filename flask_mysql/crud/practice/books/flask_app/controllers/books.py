from flask_app.models.book import Book
from flask_app.models.author import Author
from flask import render_template , request, redirect
from flask_app import app


@app.route('/books')
def books():
    books=Book.show()
    return render_template("books.html",books=books)

@app.route('/new_book',methods=['POST'])
def new_book():
    data=request.form
    Book.add_book(data)
    return redirect('/books')

@app.route('/book/<int:id>')
def book_with_id(id):
    data={'id' : id}
    unfavorited_authors=Author.unfavorited_authors(data)
    get_by_id=Book.get_by_id(data)
    return render_template("book.html",unfavorited_authors=unfavorited_authors,get_by_id=get_by_id)
@app.route('/add_favorited/book',methods=['POST'])
def new_fav_author():
    data=request.form
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")

