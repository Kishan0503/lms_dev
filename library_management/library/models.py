from django.db import models
from user.models import CustomUser, Author, Genre


class Book(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    genres = models.ManyToManyField(Genre)
    ISBN = models.CharField(max_length=13, blank=True, null=True)
    available_copies = models.IntegerField(null=True)
    total_copies = models.IntegerField(null=True)

class BorrowRequest(models.Model):
    STATUS_CHOICES = (('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('RETURNED', 'Returned'))
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING', blank=True, null=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    returned_at = models.DateTimeField(null=True, blank=True)

class BookReview(models.Model):
    RATING_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)