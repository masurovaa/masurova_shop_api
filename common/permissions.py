from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """Разрешает владельцу создавать, видеть, изменять и удалять свои продукты"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsAnonymousReadOnly(BasePermission):
    """Разрешает анонимным пользователям только чтение"""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsStaff(BasePermission):
    """Разрешает модератору/работнику изменять и удалять чужие продукты
    но не может создавать свои"""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_staff
            and request.method != "POST"
        )


class IsSuperuser(BasePermission):
    """Разрешает только суперпользователю"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_superuser
