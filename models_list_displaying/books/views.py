from django.shortcuts import render, get_object_or_404
from books.models import Book



def books_view(request):
    template = 'books/books_list.html'
    books = list(Book.objects.all())
    context = {
        'books':books
    }
    return render(request, template, context)

def book_show(request, slug):
    template = 'books/book.html'
    book = get_object_or_404(Book, slug=slug)
    context = {
        'book':book
    }
    return render(request, template, context)
