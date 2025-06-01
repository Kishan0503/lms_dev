from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('book', BookViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),

    path('borrow/', BorrowRequestCreateView.as_view(), name='borrow-create'),
    path('borrow_by_user/', BorrowRequestListView.as_view(), name='borrow-by-user'),
    path('borrow/<int:pk>/<str:action>/', BorrowRequestActionView.as_view(), name='borrow-action'),

    path('book/<int:book_id>/reviews/', BookReviewListCreateView.as_view(), name='book-reviews'),
]