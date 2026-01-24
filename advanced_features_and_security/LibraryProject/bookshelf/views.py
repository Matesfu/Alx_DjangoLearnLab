from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    query = request.GET.get('q')
    if query:
        # SECURE: Using Django's ORM filter which parameterizes input
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    #logic for editing the book
    return render(request, 'bookshelf/edit_form.html', {'book':book})

def form_example_view(request):
    """
    Handles the ExampleForm. Validates input to prevent XSS and 
    other malicious data entry.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # As a backend developer, always use cleaned_data as it is sanitized
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            
            # For this example, we might redirect or just show a success message
            return render(request, 'bookshelf/form_success.html', {'name': name})
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})