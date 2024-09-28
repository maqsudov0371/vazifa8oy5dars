from django.urls import path
from .views import GenreAPIView, GenreDetailAPIView, AuthorAPIView, AuthorDetailAPIView, BookAPIView, BookDetailAPIView

urlpatterns = [
    path('genres/', GenreAPIView.as_view(), name='list_genre'),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view(), name='detail_genre'),
    path('authors/', AuthorAPIView.as_view(), name='list_author'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='detail_author'),
    path('books/', BookAPIView.as_view(), name='list_book'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='detail_book'),
]
