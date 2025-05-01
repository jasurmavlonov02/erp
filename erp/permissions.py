from rest_framework import permissions
from datetime import timedelta, datetime




    
        
class CanEditWithinSpecialTime(permissions.BasePermission):
    message = 'User Or Time exception'
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT','PATCH','DELETE']:
            if request.user.username != 'jasur':
                return False
            
            deadline = datetime.now(obj.created_at.tzinfo) - obj.created_at
            print(deadline)
            return deadline < timedelta(hours=2)
    
        return True
    
    
# class EditWithinTwoHours(permissions.BasePermission):
#     """
#     Custom permission to only allow edits within 2 hours of object creation.
#     """
    
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request
#         if request.method in permissions.SAFE_METHODS:
#             return True
            
#         # Write permissions are only allowed within 2 hours of creation
#         time_since_creation = datetime.now(obj.created_at.tzinfo) - obj.created_at
#         return time_since_creation < timedelta(hours=2)