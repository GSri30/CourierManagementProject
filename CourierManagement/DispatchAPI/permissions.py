from rest_framework import permissions


class IsMappingOwner(permissions.BasePermission):
    """
    Checks if the user is the owner of the mapping
    """
    
    def has_object_permission(self,request,view,obj):
        return obj.ParentMail == request.user.email