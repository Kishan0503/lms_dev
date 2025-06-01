from rest_framework import generics, viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, BorrowRequest, BookReview
from .serializers import *
from user.permissions import IsLibrarianRequired, IsStudentRequired

import datetime


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'genres']
    search_fields = ['title', 'ISBN']
    ordering_fields = ['title', 'available_copies', 'total_copies']
    ordering = ['title']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsLibrarianRequired()]
        return [IsAuthenticated()]



class BorrowRequestCreateView(generics.CreateAPIView):
    queryset = BorrowRequest.objects.all()
    serializer_class = BorrowRequestSerializer
    permission_classes = [IsAuthenticated, IsStudentRequired]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BorrowRequestListView(generics.ListAPIView):
    serializer_class = BorrowRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BorrowRequest.objects.filter(user=self.request.user)


class BorrowRequestActionView(generics.UpdateAPIView):
    queryset = BorrowRequest.objects.all()
    serializer_class = BorrowRequestSerializer
    permission_classes = [IsAuthenticated, IsLibrarianRequired]

    def patch(self, request, *args, **kwargs):
        borrow = self.get_object()
        action = self.kwargs['action']

        if action == 'approve':
            borrow.status = 'APPROVED'
            borrow.approved_at = datetime.datetime.now()

        elif action == 'reject':
            borrow.status = 'REJECTED'

        elif action == 'return':
            borrow.status = 'RETURNED'
            borrow.returned_at = datetime.datetime.now()

        borrow.save()
        return Response(BorrowRequestSerializer(borrow).data)



class BookReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = BookReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BookReview.objects.filter(book_id=self.kwargs['book_id'])

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, book_id=self.kwargs['book_id'])