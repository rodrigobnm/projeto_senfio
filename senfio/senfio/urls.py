from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('entrou/', views.entrou, name='entrou'),
    path('api/login/', views.login_view, name='login'),
]