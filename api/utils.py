from datetime import date
from typing import List
from .models import User, Friendship

def calculate_age(born: date) -> int:
    '''
    Calculate user age
    '''
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def filter_users_by_age(users: List['User'], min_age: int, max_age: int) -> List['User']:
    '''
    Filter users based on user's selected age range
    '''
    filtered_users = []
    for user in users:
        age = calculate_age(user.dob)
        if min_age <= age <= max_age:
            filtered_users.append(user)
    return filtered_users

def filter_users_by_non_friends(users: List['User'], user_id: int) -> List['User']:
    '''
    Filter similar users by those who are not pending or accepted friends
    '''
    # Get the user's friends
    user = User.objects.get(id=user_id)
    friends = Friendship.objects.filter(user=user).values_list('friend', flat=True)
    friends = friends.union(Friendship.objects.filter(friend=user).values_list('user', flat=True))
    return [user for user in users if user.id not in friends]