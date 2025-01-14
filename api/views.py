import heapq
import json
from urllib import response
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.core.paginator import Paginator
from .models import User
from .utils import calculate_age, filter_users_by_age, filter_users_by_non_friends
from .forms import UserForm, UserAuthenticationForm
from api.models import Hobbies, UserHobby, User, Friendship
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.forms.models import model_to_dict
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.contrib.auth.models import auth, AbstractBaseUser
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from typing import Union
from .models import User, Hobbies, UserHobby, Friendship
from .forms import UserForm, UserAuthenticationForm
from django.middleware.csrf import get_token

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def build_max_heap(request, user_id: int) -> JsonResponse:
    '''
    View to get users with the most similar hobbies using a max heap.
    returns paginated results.
    '''
    # checks if user is logged in 
    # if not request.user.is_authenticated:
    #     return JsonResponse({'error': 'User not authenticated'}, status=401)

    # user = request.user
    user = User.objects.get(id=user_id)
    max_heap = []

    # Get age_from and age_to from request parameters, default to 1 and infinity
    age_from = int(request.GET.get('age_from', 1))
    age_to = int(request.GET.get('age_to', 999))

    # Get all users except the current one
    other_users = User.objects.exclude(id=user.id)

    # Filter users by age group and those who are not friends already
    other_users = filter_users_by_age(other_users, age_from, age_to)
    other_users= filter_users_by_non_friends(other_users, user_id)

    for other_user in other_users:
        common_hobbies_count = User.count_common_hobbies(user, other_user)
        if common_hobbies_count > 0:
            heapq.heappush(max_heap, (-common_hobbies_count, other_user.id))

    # Convert heap to a list
    sorted_users = []
    while max_heap:
        common_hobbies_count, other_user_id = heapq.heappop(max_heap)
        other_user = User.objects.get(id=other_user_id)
        hobbies = [user_hobby.hobby for user_hobby in UserHobby.objects.filter(user=other_user)]
        sorted_users.append({
            'id': other_user.id,
            'email': other_user.email,
            'first_name': other_user.first_name,
            'last_name': other_user.last_name,
            'hobbies': [{'id': hobby.id, 'name': hobby.name} for hobby in hobbies],
            'age': calculate_age(other_user.dob),
            'common_hobbies_count': -common_hobbies_count
        })

    # Paginate results limited to 10 users
    paginator = Paginator(sorted_users, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return JsonResponse({
        'users': list(page.object_list),
        'has_next': page.has_next(),
        'has_previous': page.has_previous(),
        'page_number': page.number,
        'total_pages': paginator.num_pages
    })

def signup(request):
    '''
    View for user signing up 
    '''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #save the new user
            user = form.save()
            login(request, user) 
            return redirect('http://localhost:5173/')
    else:
        form = UserForm()
    
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    '''
    View for user to log in
    '''
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('http://localhost:5173/') 
    else:
        form = UserAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    '''
    View for user to log out
    '''
    logout(request)
    return redirect('login') 

def authenticated_view(request):
    '''
    View to check if user is authenticated
    '''
    response_data = {
        "isAuthenticated": request.user.is_authenticated,
        "user": {
            "id": request.user.id if request.user.is_authenticated else None,
            # "username": request.user.username if request.user.is_authenticated else None,
            "email": request.user.email if request.user.is_authenticated else None,
        } if request.user.is_authenticated else None,
    }

    print(f"Response Data: {response_data}")
    return JsonResponse(response_data)


def get_all_users(request: HttpRequest) -> JsonResponse:
    '''
    Get all users
    '''
    users = User.objects.all()
    user_data = []
    for user in users:
        user_data.append({
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'dob': user.dob,
            'age': calculate_age(user.dob),
        })
    return JsonResponse(user_data, safe=False)

def get_user_by_id(request: HttpRequest, user_id: int) -> JsonResponse:
    '''
    Get user by id
    '''
    try:
        user = User.objects.get(id=user_id)
        user_data = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'dob': user.dob,
        }
        return JsonResponse(user_data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
def get_user_id(request: HttpRequest, user_id: int) -> JsonResponse:
    '''
    Get user by id
    '''
    try:
        user = User.objects.get(id=user_id)
        user_data = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'dob': user.dob,
        }
        return JsonResponse(user_data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@ensure_csrf_cookie  
@require_http_methods(["PUT"])
def update_user_password(request: HttpRequest, user_id: int) -> JsonResponse:
    """
    Update user password
    """
    if request.method == 'PUT':
        try:
            user = User.objects.get(id=user_id)
            data = json.loads(request.body)
            current_password = data.get('current_password')
            new_password = data.get('new_password')

            if not user.check_password(current_password):
                return JsonResponse({'error': 'Current password is incorrect'}, status=400)

            if not new_password:
                return JsonResponse({'error': 'New password cannot be empty'}, status=400)

            user.set_password(new_password)
            user.save()
            # Authenticate user again
            update_session_auth_hash(request, user)
            return JsonResponse({'message': 'Password updated successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
@csrf_exempt
def update_user_profile(request: HttpRequest, user_id: int) -> JsonResponse:
    """
    Update user profile by ID
    """
    if request.method == 'PUT':
        try:
            user = User.objects.get(id=user_id)
            data = json.loads(request.body)

            # Validate fields
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            dob = data.get('dob')

            if not first_name or not last_name or not email or not dob:
                return JsonResponse({'error': 'All fields are required and cannot be empty'}, status=400)
            
            # Update user fields
            user.first_name = data.get('first_name', user.first_name)
            user.last_name = data.get('last_name', user.last_name)
            user.email = data.get('email', user.email)
            user.dob = data.get('dob', user.dob)

            user.save()
            return JsonResponse({
                'message': 'Profile updated successfully',
                'user': {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'dob': user.dob
                }
            })
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
    
def get_hobby(request: HttpRequest) -> JsonResponse:
    '''
    Get hobby
    '''
    hobbies = Hobbies.objects.all()
    data = []
    for hobby in hobbies:
        data.append({
            'id': hobby.id,
            'name': hobby.name,
            'description': hobby.description
        })
    return JsonResponse(data, safe=False)

def add_hobby(request: HttpRequest) -> JsonResponse:
    '''
    Add hobby
    '''
    data = json.loads(request.body)
    hobby = Hobbies.objects.create(
        name=data['name'],
        description=data['description']
    )
    return JsonResponse({
        'id': hobby.id,
        'name': hobby.name,
        'description': hobby.description
    })

def update_hobby(request: HttpRequest, hobby_id: int) -> JsonResponse:
    '''
    Update hobby
    '''
    data = json.loads(request.body)
    hobby = Hobbies.objects.get(id=hobby_id)
    hobby.name = data['name']
    hobby.description = data['description']
    hobby.save()
    return JsonResponse({
        'id': hobby.id,
        'name': hobby.name,
        'description': hobby.description
    })

def delete_hobby(request: HttpRequest, hobby_id: int) -> JsonResponse:
    '''
    Delete hobby
    '''
    hobby = Hobbies.objects.get(id=hobby_id)
    hobby.delete()
    return JsonResponse({
        'message': 'Hobby deleted successfully'
    })

def add_hobby_and_user_hobby(request: HttpRequest) -> JsonResponse:
    '''
    Add a new hobby for a user and to the overall hobbies list
    '''
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        hobby_name = data.get('name')
        hobby_description = data.get('description')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        hobby = Hobbies.objects.create(
            name=hobby_name,
            description=hobby_description
        )

        UserHobby.objects.create(
            user=user,
            hobby=hobby
        )

        return JsonResponse({
            'user_id': user.id,
            'hobby_id': hobby.id,
            'name': hobby.name,
            'description': hobby.description
        })
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def get_all_user_hobbies(request: HttpRequest) -> JsonResponse:
    '''
    Get all user hobbies
    '''
    user_hobbies = UserHobby.objects.all()
    return JsonResponse({'user_hobbies': list(user_hobbies.values())})

def get_user_hobbies(request: HttpRequest, user_id: int) -> JsonResponse:
    '''
    Get hobbies for a specific user
    '''
    try:
        user = User.objects.get(id=user_id)
        user_hobbies = UserHobby.objects.filter(user=user)
        hobbies = [user_hobby.hobby for user_hobby in user_hobbies]
        hobbies_data = [{'user_id': user_id, 'user': user.first_name,'hobby_id': hobby.id,'hobby': hobby.name, 'description': hobby.description} for hobby in hobbies]
        return JsonResponse(hobbies_data, safe=False)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)


def add_user_hobby(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        hobby_id = data.get('hobby_id')

        user = get_object_or_404(User, id=user_id)
        hobby = get_object_or_404(Hobbies, id=hobby_id)
        UserHobby.objects.create(user=user, hobby=hobby)

        return JsonResponse({'message': 'Existing hobby added successfully'}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def update_user_hobby(request: HttpRequest, user_hobby_id: int) -> JsonResponse:
    '''
    Update user hobby
    '''
    data = json.loads(request.body)
    user_hobby = UserHobby.objects.get(id=user_hobby_id)
    user_hobby.user_id = data['user_id']
    user_hobby.hobby_id = data['hobby_id']
    user_hobby.save()
    return JsonResponse({
        'user_id': user_hobby.user_id,
        'hobby_id': user_hobby.hobby_id
    })

def delete_user_hobby(request: HttpRequest) -> JsonResponse:
    if request.method == 'DELETE':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        hobby_id = data.get('hobby_id')

        user_hobby = get_object_or_404(UserHobby, user_id=user_id, hobby_id=hobby_id)
        user_hobby.delete()

        return JsonResponse({'message': 'User hobby deleted successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def get_all_friendships(request: HttpRequest) -> JsonResponse:
    '''
    Get all friends
    '''
    friendships = Friendship.objects.all()
    return JsonResponse({'friendships': list(friendships.values())})

def get_friendship(request: HttpRequest, user_id: int) -> JsonResponse:
    '''
    Get user's friends
    '''
    try:
        user = User.objects.get(id=user_id)
        friendships = Friendship.objects.filter(user=user) | Friendship.objects.filter(friend=user)
        friendships_data = [
            {
                'id': friendship.id,
                'user': friendship.user.first_name,
                'friend': friendship.friend.first_name,
                'status': friendship.status,
                'accepted': friendship.accepted,
                'created_at': friendship.created_at
            }
            for friendship in friendships
        ]
        return JsonResponse(friendships_data, safe=False)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def create_friendship(request):
    '''
    Create a new friendship instance when someone sends a friend request.
    '''
    if request.method == 'POST':
        try:
            print(request.body)
            data = json.loads(request.body)
            user_id = data.get('user_id')
            friend_id = data.get('friend_id')

            if not user_id or not friend_id:
                return JsonResponse({'error': 'Missing user_id or friend_id'}, status=400)

            user = get_object_or_404(User, id=user_id)
            friend = get_object_or_404(User, id=friend_id)

            friendship, created = Friendship.objects.get_or_create(user=user, friend=friend)
            if created:
                return JsonResponse({'message': 'Friend request sent successfully'}, status=201)
            else:
                return JsonResponse({'message': 'Friend request already exists'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def update_friendship_status(request):
    '''
    Update friendship status when someone accepts or rejects a friend request.
    '''
    if request.method == 'PUT':
        try:
            user = User.objects.get(id=user_id)
            data = json.loads(request.body)
            current_password = data.get('current_password')
            new_password = data.get('new_password')

            if not user.check_password(current_password):
                return JsonResponse({'error': 'Current password is incorrect'}, status=400)

            if not new_password:
                return JsonResponse({'error': 'New password cannot be empty'}, status=400)

            user.set_password(new_password)
            user.save()
            return JsonResponse({'message': 'Password updated successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
