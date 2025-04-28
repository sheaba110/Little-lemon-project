from django.contrib import admin
from django.urls import path, include
from LittlelemonAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('LittlelemonAPI.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
