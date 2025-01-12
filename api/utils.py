from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def filter_users_by_age(users, min_age, max_age):
    filtered_users = []
    for user in users:
        age = calculate_age(user.dob)
        if min_age <= age <= max_age:
            filtered_users.append(user)
    return filtered_users
