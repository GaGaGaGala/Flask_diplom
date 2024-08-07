python -m pip install -r requirements.txt

[Flask] python app.py
[FastAPI] python -m uvicorn app.main:app
[Django] python manage.py runserver


```
fast_book_json/
│
├── instance/
│   └── books.db
│
├── templates/
│   └──templates/django_book/
│       ├── about.html
│       ├── base.html
│       ├── book.html
│       ├── books.html
│       ├── contacts.html
│       └── style.css
│
├── app.py
├── create_db_books.py
├── models.py
├── views.py
├── manage.py             
├── books.json         # Файл с данными о книгах
└── README.md          # Файл с описанием проекта
```

#### Автор: Галина Косачёва
#### Дата: 07.08.2024