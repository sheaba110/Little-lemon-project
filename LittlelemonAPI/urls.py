from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items', views.MenuItemsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('menu-items/<int:pk>', views.MenuItemsViewSet.as_view({'get': 'retrieve'})),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token)
]