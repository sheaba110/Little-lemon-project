from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.menu_items),
    path('menu-items/<int:pk>', views.single_item, name='single_item'),
    # path('menu', views.menu, name='menu-items')
]