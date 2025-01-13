import heapq
import json
from urllib import response
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
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
import logging

logger = logging.getLogger(__name__)


def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def build_max_heap(request):
    '''
    View to get users with the most similar hobbies using a max heap.
    returns paginated results.
    '''
    # checks if user is logged in 
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    user = request.user
    max_heap = []

    #get all users except the current one
    other_users = User.objects.exclude(id=user.id)

    for other_user in other_users:
        common_hobbies_count = User.count_common_hobbies(user, other_user)
        if common_hobbies_count > 0:
            heapq.heappush(max_heap, (-common_hobbies_count, other_user.id))

    #convert heap to a list
    sorted_users = []
    while max_heap:
        common_hobbies_count, other_user_id = heapq.heappop(max_heap)
        other_user = User.objects.get(id=other_user_id)
        sorted_users.append({
            'id': other_user.id,
            'email': other_user.email,
            'first_name': other_user.first_name,
            'last_name': other_user.last_name,
            'common_hobbies_count': -common_hobbies_count
        })

    #paginate results limited to 10 users
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
            return redirect('http://localhost:5173/')  # redirect to vue page, need to sort out the logic of this as it is hardcoded
            #return redirect('main_spa')  # Redirect to a home page
    else:
        form = UserForm()
    
    return render(request, 'signup.html', {'form': form})

# def login_view(request):
#     '''
#     View for user to log in
#     '''
#     if request.method == 'POST':
#         form = UserAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('http://localhost:5173/') # same as signup
#     else:
#         form = UserAuthenticationForm()
    
#     return render(request, 'login.html', {'form': form})

def login_view(request):
    '''
    View for user to log in
    '''
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"User {user.username} logged in successfully.")
            return redirect('http://localhost:5173/')  # Redirect to the main page
        else:
            logger.warning("Invalid login attempt.")
            logger.warning(form.errors)
    else:
        form = UserAuthenticationForm()
    
    logger.info("Rendering login form.")
    return render(request, 'login.html', {'form': form})

# def login_view(request: WSGIRequest) -> Union[HttpResponseRedirect, HttpResponse]:
#     '''
#     View for user to log in
#     '''
#     if request.method == 'POST':
#         form = UserAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username: str = request.POST.get('username')
#             password: str = request.POST.get('password')
#             authenticated_user: AbstractBaseUser = authenticate(request, username=username, password=password)

#             if authenticated_user is not None:
#                 auth.login(request, authenticated_user)
#                 response: HttpResponseRedirect = HttpResponseRedirect('http://localhost:5173/')
                
#                 #remove for production
#                 response.set_cookie('user_id', str(authenticated_user.id))
#                 response.set_cookie('isAuthenticated', True)
#                 #remove for production
                
#                 return response
#     else:
#         form = UserAuthenticationForm()
    
#     return render(request, 'login.html', {'form': form})

def logout_view(request):
    '''
    View for user to log out
    '''
    logout(request)
    return redirect('login') 

# def authenticated_view(request):
#     '''
#     View to check if user is authenticated
#     '''
#     print(f"User: {request.user.username}, user: {request.user}")
#     if request.user.is_authenticated:
#         return JsonResponse({'isAuthenticated': True, 'user': request.user.username})
#     else:
#         return JsonResponse({'isAuthenticated': False}, status=401)

def authenticated_view(request):
    '''
    View to check if user is authenticated
    '''
    print(f"User: {request.user.email}")
    try:
        if request.user.is_authenticated:
            response_data = {'isAuthenticated': True, 'user': request.user.email}
            print(response_data)
            return JsonResponse(response_data)
        else:
            response_data = {'isAuthenticated': False}
            print(response_data)
            return JsonResponse(response_data, status=401)
    except Exception as e:
        print("error" + str(e))
        return JsonResponse({'error': str(e)}, status=400)

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
            'is_staff': user.is_staff,
            'is_active': user.is_active,
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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
            return JsonResponse({'message': 'Password updated successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
