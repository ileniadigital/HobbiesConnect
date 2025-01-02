"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    # User paths
    path('user/', get_all_users, name='get_all_users'),
    path('user/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    # Hobby paths
    path('hobbies/', get_hobby, name='get_hobby'),
    path('hobbies/add/', add_hobby, name='add_hobby'),
    path('hobbies/update/<int:hobby_id>/', update_hobby, name='update_hobby'),
    path('hobbies/delete/<int:hobby_id>/', delete_hobby, name='delete_hobby'),
    # User Hobby paths
    path('user_hobbies/', get_all_user_hobbies, name='get_user_hobby'),
    path('api/user_hobbies/add/', add_user_hobby, name='add_user_hobby'),
    path('user_hobbies/update/<int:user_hobby_id>/', update_user_hobby, name='update_user_hobby'),
    path('user_hobbies/delete/<int:user_hobby_id>/', delete_user_hobby, name='delete_user_hobby'),
    path('user/<int:user_id>/hobbies/', get_user_hobbies, name='get_user_hobbies'),
    # User and Hobby paths
    path('hobbies/add_user_hobby/', add_hobby_and_user_hobby, name='add_hobby_and_user_hobby'),
    # Friendship paths
    path('user/<int:user_id>/friendships/', get_friendship, name='get_friendship'),
    # path('friendship/add/', add_friendship, name='add_friendship'),
    
]
