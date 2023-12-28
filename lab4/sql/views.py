from django.shortcuts import render, redirect
from .models import Book

def index(request):

    if 'id_book' in request.GET:
        id_book = request.GET['id_book']
        # Перенаправляем на представление для отображения деталей книги
        return redirect('book_detail', id_book=id_book) 
    else:
        books = Book.objects.all()
        # Передаем флаг show_input для отображения поля ввода
        return render(request, 'index.html', {'books': books, 'show_input': True}) 

    
def book_detail(request, id_book):
    book = Book.objects.filter(id_book=id_book).first()  # книга по указанному ID
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books, 'book': book})