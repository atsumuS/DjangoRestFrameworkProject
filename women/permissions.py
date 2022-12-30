
from rest_framework import permissions
from django.contrib.auth.models import User


class DeleteAdminGetAllow(permissions.BasePermission): 
    # класс ограничения для удаления данных на сервере 
    def has_permission(self, request, view): 
        # метод позволяет создать свои ограничения пользователя, 
        # в данном случае безопасные запросы для всех а удаление 
        # только для зарегистрированных
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (bool(request.user and request.user.is_staff))
    
    
class ListAloowEditAuth(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
                return True
        
        return (obj.user == request.user)
    
    

        