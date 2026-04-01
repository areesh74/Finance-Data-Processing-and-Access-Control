from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # APIs
    path('api/', include('records.urls')),
    path('api/', include('dashboard.urls')),
    path('api-auth/', include('rest_framework.urls')),
]