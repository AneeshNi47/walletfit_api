
from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request):
    return Response({
        "users": "/api/users/",
        "accounts": "/api/accounts/",
        "expenses": "/api/expenses/"
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),  # shows up at /api/
    path('api/users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')), 
    # Add other app urls here
]