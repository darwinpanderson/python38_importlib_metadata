from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('packages/', views.listpkg, name='list_packages'),
    path('packages/<str:package>', views.listpkg, name='package_details'),
]