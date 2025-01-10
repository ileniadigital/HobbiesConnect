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
from django.contrib import admin
from django.urls import include, path
from . import views
from .views import *
from .views import main_spa

urlpatterns = [
    path('', main_spa, name='main_spa'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('similar-users/', build_max_heap, name='similar_users'),
    path('authenticated/', authenticated_view, name='authenticated'),
    path('spa/', main_spa, name='main_spa'),
    # User paths
    path('user/', get_all_users, name='get_all_users'),
    path('user/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    path('user/update/<int:user_id>/', update_user_profile, name='update_user'),
    path('user/update_password/<int:user_id>/', update_user_password, name='update_user_password'),
    path('user/get_user_id', get_user_id, name='get_user_id'),
    # Hobby paths
    path('hobbies/', get_hobby, name='get_hobby'),
    path('hobbies/add/', add_hobby, name='add_hobby'),
    path('hobbies/update/<int:hobby_id>/', update_hobby, name='update_hobby'),
    path('hobbies/delete/<int:hobby_id>/', delete_hobby, name='delete_hobby'),
    # User Hobby paths
    path('user_hobbies/', get_all_user_hobbies, name='get_user_hobby'),
    path('api/user_hobbies/add/', add_user_hobby, name='add_user_hobby'),
    path('user_hobbies/update/<int:user_hobby_id>/', update_user_hobby, name='update_user_hobby'),
    path('user_hobbies/delete/', delete_user_hobby, name='delete_user_hobby'),
    path('user/<int:user_id>/hobbies/', get_user_hobbies, name='get_user_hobbies'),
    # User and Hobby paths
    path('hobbies/add_user_hobby/', add_hobby_and_user_hobby, name='add_hobby_and_user_hobby'),
    # Friendship paths
    path('user/<int:user_id>/friendships/', get_friendship, name='get_friendship'),
    # path('friendship/add/', add_friendship, name='add_friendship'),
    
]
