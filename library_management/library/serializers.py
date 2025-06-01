from rest_framework import serializers

from .models import Book, BorrowRequest, BookReview
from user.models import Author, Genre
from user.serializers import AuthorSerializer, GenreSerializer

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), write_only=True, source='author')
    genre_ids = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, write_only=True, source='genres')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_id', 'genres', 'genre_ids',
                  'ISBN', 'available_copies', 'total_copies']

    def create(self, validated_data):
        genres = validated_data.pop('genres')
        book = Book.objects.create(**validated_data)
        book.genres.set(genres)
        
        return book

    def update(self, instance, validated_data):
        genres = validated_data.pop('genres', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        instance.save()
        if genres:
            instance.genres.set(genres)
        
        return instance


class BorrowRequestSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), required=True)

    class Meta:
        model = BorrowRequest
        fields = '__all__'
        read_only_fields = ['user', 'status', 'requested_at', 'approved_at', 'returned_at']


class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = '__all__'
        read_only_fields = ['user', 'book', 'created_at']