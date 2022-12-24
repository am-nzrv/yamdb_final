from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Пермишн на чтение всем, добавление и удаления - админ."""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_authenticated
            and (request.user.is_admin or request.user.is_superuser)
        )


class IsAdminModerAuthorOrReadOnly(permissions.BasePermission):
    """
    Для анонима безопасные запросы. Для остальных PATCH и DELETE.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and (request.user.is_superuser
                 or request.user.is_admin
                 or request.user.is_moderator
                 or request.user == obj.author)
        )


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)
