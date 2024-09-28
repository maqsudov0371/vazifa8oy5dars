from rest_framework import serializers
from .models import Genre, Author, Book

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    # Nested serializers for Author and Genre
    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
