#скрипт, который заново позволяет создать базу данных и заполнить её
#запускается один раз и больше ничего не делает


from flask import Flask
from models import Book, db
import json

# создаём объект приложения с помощью flask
app = Flask(__name__)
# прописываем некоторые настройки приложения (того, как оно будет работать)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)    # связываем приложение и экземпляр SQLAlchemy



if __name__ == '__main__':      # сработает,если запущен именно этот файл
    with app.app_context():     # вместо полноценного запуска приложения (app.run),чтобы воспользоваться частями приложения, не запуская его целиком
        db.create_all()         # делаем таблицу

        with open('books.json', encoding='utf-8') as f:
            books_data = json.load(f)

        for book_data in books_data:
            book = Book(title=book_data['название'],
                        author=book_data['автор'],
                        year=book_data['год публикации'],
                        description=book_data['описание'],
                        image_url=book_data['фотография'])
            db.session.add(book)

        db.session.commit()
