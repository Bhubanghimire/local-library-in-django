from django.shortcuts import render
from catalog.models import Book,BookInstance,Author,Genre

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
