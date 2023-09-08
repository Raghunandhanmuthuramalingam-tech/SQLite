# import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy()
db.init_app(app)

#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(2, 'Harry Potte', 'J. K. Rowlin', '9.3')")
# db.commit()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    # book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    # book_to_update.title = "Harry Potter and the Chamber of Secrets"
    # db.session.commit()
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
    # # or book_to_delete = db.get_or_404(Book, book_id)
    # db.session.delete(book_to_delete)
    # db.session.commit()
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()



# with app.app_context():
#     new_book = Book(id=1, title="Harry Pott", author="JKRowling", rating=9.5)
#     db.session.add(new_book)
#     db.session.commit()



