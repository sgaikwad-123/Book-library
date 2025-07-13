from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import Book
import openai
from django.shortcuts import render,redirect
from .forms import EnquiryForm
from .forms import RegisterForm
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

@xframe_options_exempt
def chatbot_view(request):
    response_text = ""
    if request.method == "POST":
        user_message = request.POST.get("message", "").lower()
        # Simple rule-based responses
        if "hello" in user_message or "hi" in user_message:
            response_text = "Hello! How can I help you today?"
        elif "book" in user_message:
            response_text = "You can add, edit, or delete books using the menu above."
        elif "bye" in user_message:
            response_text = "Goodbye! Have a nice day."
        else:
            response_text = "Sorry, I can only answer basic questions about books."
    return render(request, "chatbot.html", {"response": response_text})

from .forms import EnquiryForm
def enquiry_view(request):
    submitted = False
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            # Process the data (e.g., send email, save to DB)
            submitted = True
    else:
        form = EnquiryForm()
    return render(request, "enquiry.html", {"form": form, "submitted": submitted})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})