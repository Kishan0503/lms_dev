from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Author, Genre, CustomUser
from .serializers import RegisterSerializer, AuthorSerializer, GenreSerializer
from .permissions import IsLibrarianRequired


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    
    
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsLibrarianRequired]
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsLibrarianRequired()]
        return [IsAuthenticated()]


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated, IsLibrarianRequired]
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsLibrarianRequired()]
        return [IsAuthenticated()]