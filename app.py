from flask import Flask, render_template
from models import Book, db

app = Flask(__name__)           # создаём объект приложения с помощью flask
# прописываем некоторые настройки приложения
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'       # путь к базе данных (все книги)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)

# создаём функции отображения, которые генерируют страницу, которую видит пользователь
@app.route('/')     # декоратор  тут нужен для того, чтобы связать адрес (ссылку) с функцией отображения
def index():        # функцыя отображения главной страницы ( все книги)
    books = Book.query.all()    # получить все книги из базы данных
    return render_template('books.html', books=books)   # заполнить книгами и их атрибутами страницы  html

@app.route('/book/<int:book_id>')
def book_detail(book_id):       # получаем конкретную книгу по её id
    book = Book.query.get_or_404(book_id)
    return render_template('book.html', book=book)

@app.route('/about')
def about():                # страница : о нас
    return render_template('about.html')

@app.route('/contacts')         # контакты
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
