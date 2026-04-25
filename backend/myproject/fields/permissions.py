from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        return request.user.is_authenticated and request.user.is_staff



class IsAgentOfFieldOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return obj.agent == request.user


class CanCreateLogForAssignedField(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return obj.agent == request.user               