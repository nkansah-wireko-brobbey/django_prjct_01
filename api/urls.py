from django.urls import path
from .views import get_user,create_user, get_users, user_detail

urlpatterns = [
    path('user/', get_user, name='get_user'),
    path('users/', get_users, name='get_users'),
    path('user-detail/<int:pk>', user_detail, name='user_detail'),
    path('users/create', create_user, name='create_user')
]