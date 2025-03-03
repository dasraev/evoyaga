from rest_framework.permissions import BasePermission

class IsApparatOrIjtimoiyHimoya(BasePermission):
    def has_permission(self, request, view):
        request_code = request.user.groups.all()[0].code
        return request_code in [1,6]