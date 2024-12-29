import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from api.models import Hobbies, UserHobby, PageView, User

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

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


def get_user_hobby(request: HttpRequest) -> JsonResponse:
    '''
    Get user hobby
    '''
    user_hobbies = UserHobby.objects.all()
    return JsonResponse({'user_hobbies': list(user_hobbies.values())})

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