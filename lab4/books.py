import os
import django

# Устанавливаем настройки Django для использования моделей
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab4.settings")
django.setup()

from sql.models import Book  

def populate_books():
    # Очищаем все записи из таблицы
    Book.objects.all().delete()
    # Создаем новые книги и сохраняем их в базе данных
    books_data = [
        {"id_book": "1", "title": "book1"},
        {"id_book": "2", "title": "book2"},
        {"id_book": "3", "title": "book3"},
        {"id_book": "4", "title": "book4"},
    ]

    for data in books_data:
        book = Book(**data)
        book.save()

if __name__ == "__main__":
    populate_books()