from django.shortcuts import render
from catalog.models import Book,BookInstance,Author,Genre
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
@login_required
def index(request):
    num_books =Book.objects.count()
    num_instances =BookInstance.objects.count()

    num_instances_available = BookInstance.objects.filter(status__exact = 'o').count()

    num_author = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books':num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_author' : num_author,
        'num_visits': num_visits,
    }

    return render(request,'index.html', context=context)


class BookListView(LoginRequiredMixin,ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 2

class BookDetailView(LoginRequiredMixin,DetailView):
    model = Book
    template_name = 'book_detail.html'
    # paginate_by = 1

class AuthorListView(LoginRequiredMixin,ListView):
    model = Author
    template_name = 'author_list.html'
    paginate_by = 2

class AuthorDetailView(LoginRequiredMixin,DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'
    # paginate_by = 1

class LoanBookByUserListView(LoginRequiredMixin,ListView):
    model = BookInstance 
    template_name = 'bookinstance_list.html'
    paginate_by = 4

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
