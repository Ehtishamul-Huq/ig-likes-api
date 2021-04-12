from rest_framework import permissions

class CustomPermission(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method == 'GET' or 'POST' or 'DELETE':
            return obj.user == request.user
