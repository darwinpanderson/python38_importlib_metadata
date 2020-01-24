from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.listpkg, name='list'),
    path('list/<str:package>', views.listpkg, name='list_package'),
]