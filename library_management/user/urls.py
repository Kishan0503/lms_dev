from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, AuthorListCreateView, GenreListCreateView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
]