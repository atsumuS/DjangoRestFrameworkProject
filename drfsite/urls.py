
from django.contrib import admin
from django.urls import include, path, re_path

from women.views import *
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'women', WomenViewSet)
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')), # адрес для Login/logout
    path('api/v1/women', WomenApiList.as_view()),
    path('api/v1/women/update/<int:pk>', WomenApiUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>', WomenAPIdelete.as_view()), 
    path('api/v1/auth', include('djoser.urls')),
    re_path('^auth/', include('djoser.urls.authtoken'))
    # path('api/v1/', include(router.urls))
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    
]

