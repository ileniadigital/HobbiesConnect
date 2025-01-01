import heapq
import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .forms import UserForm, UserAuthenticationFormfrom api.models, Hobbies, UserHobby, PageView, User, Friendship

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def build_max_heap(user):
    
    users = User.objects.exclude(id=user.id)
    max_heap = []
    
    for other_user in users:
        common_hobbies_count = User.count_common_hobbies(user, other_user)
        heapq.heappush(max_heap, (-common_hobbies_count, other_user))
    
    return max_heap
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Save the new user
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('main_spa')  # Redirect to a home page or another page
    else:
        form = UserForm()
    
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_spa')  # Redirect to a home page or another page
    else:
        form = UserAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 

def test_max_heap_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    user = request.user
    max_heap = build_max_heap(user)
    sorted_heap = [(-count, other_user.email) for count, other_user in max_heap]

    return JsonResponse({'max_heap': sorted_heap})

def build_max_heap(user):
    
    users = User.objects.exclude(id=user.id)
    max_heap = []
    
    for other_user in users:
        common_hobbies_count = User.count_common_hobbies(user, other_user)
        heapq.heappush(max_heap, (-common_hobbies_count, other_user))
    
    return max_heap
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Save the new user
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('main_spa')  # Redirect to a home page or another page
    else:
        form = UserForm()
    
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_spa')  # Redirect to a home page or another page
    else:
        form = UserAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 

def test_max_heap_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    user = request.user
    max_heap = build_max_heap(user)
    sorted_heap = [(-count, other_user.email) for count, other_user in max_heap]

    return JsonResponse({'max_heap': sorted_heap})

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


def page_view(request: HttpRequest) -> JsonResponse:
    page_view = PageView.objects.first()
    page_view.count += 1
    page_view.save()
    return JsonResponse({'count': page_view.count})


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
        hobbies_data = [{'user id': user_id, 'user': user.first_name,'hobby id': hobby.id,'hobby': hobby.name, 'description': hobby.description} for hobby in hobbies]
        return JsonResponse(hobbies_data, safe=False)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

def add_user_hobby(request: HttpRequest) -> JsonResponse:
    '''
    Add user hobby
    '''
    data = json.loads(request.body)
    user_hobby = UserHobby.objects.create(
        user_id=data['user_id'],
        hobby_id=data['hobby_id']
    )
    return JsonResponse({
        'user_id': user_hobby.user_id,
        'hobby_id': user_hobby.hobby_id
    })

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

def delete_user_hobby(request: HttpRequest, user_hobby_id: int) -> JsonResponse:
    '''
    Delete user hobby
    '''
    user_hobby = UserHobby.objects.get(id=user_hobby_id)
    user_hobby.delete()
    return JsonResponse({
        'message': 'User hobby deleted successfully'
    })


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