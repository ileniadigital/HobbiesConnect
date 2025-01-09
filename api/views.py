import heapq
import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from .models import User
from .forms import UserForm, UserAuthenticationForm
from api.models import Hobbies, UserHobby, PageView, User, Friendship
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

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

def login_view(request):
    '''
    View for user to log in
    '''
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('http://localhost:5173/') # same as signup
            #return redirect('main_spa')  # Redirect to a home page or another page
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
    return JsonResponse({'isAuthenticated': request.user.is_authenticated})



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
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
