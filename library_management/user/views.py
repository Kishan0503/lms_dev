from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import Author, Genre, CustomUser
from .serializers import RegisterSerializer, AuthorSerializer, GenreSerializer
from .permissions import IsLibrarianRequired


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response({"error": "Invalid or expired refresh token."}, status=status.HTTP_400_BAD_REQUEST)
        
        
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