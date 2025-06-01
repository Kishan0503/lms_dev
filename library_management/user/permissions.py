from rest_framework.permissions import BasePermission

class IsLibrarianRequired(BasePermission):
    """
    Allows only librarians to create.
    Read-only for everyone else.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'LIBRARIAN'
    
class IsStudentRequired(BasePermission):
    """
    Allows only students to create.
    Read-only for everyone else.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'STUDENT'