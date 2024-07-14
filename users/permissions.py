from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """
    Проверяет входит ли пользователь в группу модераторов.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    """
    Проверяет является ли пользователь автором.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
