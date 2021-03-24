from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Checks if the user is the owner
    """
    
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.email == request.user.email