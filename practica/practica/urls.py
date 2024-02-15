from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('porfolio/', views.porfolio, name='porfolio'),
    path('', views.index, name='index'),
]
