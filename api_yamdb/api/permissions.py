from rest_framework import permissions


class CommentReviewPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        self.message = 'Нужно авторизоваться.'
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        self.message = 'Вы не автор.'
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.role in ['admin', 'moderator'])


class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated and request.user.is_staff)
        )

