from django.shortcuts import render
from catalog.models import Book,BookInstance,Author,Genre
from django.views.generic import ListView,DetailView


# Create your views here.
def index(request):
    num_books =Book.objects.count()
    num_instances =BookInstance.objects.count()

    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    num_author = Author.objects.count()

    context = {
        'num_books':num_books,
        'num_instances' : num_instances,
        'num_instances_available ' : num_instances_available,
        'num_author' : num_author,
    }

    return render(request,'index.html', context=context)


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 2

class BookDetailView(DetailView):
    model = Author
    template_name = 'book_detail.html'
    # paginate_by = 1

class AuthorListView(ListView):
    model = Book
    template_name = 'author_list.html'
    paginate_by = 2

class AuthorDetailView(DetailView):
    model = Book
    template_name = 'author_detail.html'
    # paginate_by = 1