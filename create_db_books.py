from flask import Flask
from models import Book, db
import json
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def optimize_image(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    # Оптимизация изображения здесь, например, изменение размера, компрессия и т.д.
    return image_url

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        with open('books.json', encoding='utf-8') as f:
            books_data = json.load(f)

        for book_data in books_data:
            optimized_image_url = optimize_image(book_data['фотография'])
            book = Book(title=book_data['название'],
                        author=book_data['автор'],
                        year=book_data['год публикации'],
                        description=book_data['описание'],
                        image_url=optimized_image_url)
            db.session.add(book)

        db.session.commit()
