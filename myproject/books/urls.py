from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView
from .views import chatbot_view
from .views import enquiry_view 
from .views import register_view
urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('add/', BookCreateView.as_view(), name='book-add'),
    path('edit/<int:pk>/', BookUpdateView.as_view(), name='book-edit'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('chatbot/', chatbot_view, name='chatbot'),
    path('enquiry/', enquiry_view, name='enquiry'),
    path('register/', register_view, name='register'),  # Placeholder for register view
]