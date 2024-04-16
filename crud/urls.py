from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users', views.users, name='users'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
]
