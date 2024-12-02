from django.contrib.auth.models import AbstractUser
from django.db import models
from collections import Counter
# Create your models here.


class PageView(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Page view count: {self.count}"


class User(AbstractUser):
    """
    Custom User model inheriting Django's AbstractUser with email as the unique identifier.
    """
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dob = models.DateField()
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set', 
        blank=True,
        help_text='The groups this user belongs to.',
    )
    #no specific permisions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    USERNAME_FIELD = 'email' #username is emai;
    REQUIRED_FIELDS = ['first_name', 'last_name']
    @staticmethod
    def count_common_hobbies(user1, user2):
        """
        Static method to count common hobbies between two users.
        """
        # Get hobbies for both users
        user1_hobbies = set(UserHobby.objects.filter(user=user1).values_list('hobby', flat=True))
        user2_hobbies = set(UserHobby.objects.filter(user=user2).values_list('hobby', flat=True))

        # Find common hobbies
        common_hobbies = user1_hobbies.intersection(user2_hobbies)
        return len(common_hobbies)
    


class Hobbies(models.Model):
    '''
    Hobbies model to store hobbies
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class UserHobby(models.Model):
    '''
    UserHobby model to store hobbies of users
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hobby = models.ForeignKey(Hobbies, on_delete=models.CASCADE)

    def __str__(self):
        return self.hobby


class Friendship(models.Model):
    '''
    Friendship model to store friends and friends requests
    '''

    class FriendshipStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        ACCEPTED = 'ACCEPTED', 'Accepted'
        REJECTED = 'REJECTED', 'Rejected'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
    status = models.CharField(
        max_length=50,
        choices=FriendshipStatus.choices,
        default=FriendshipStatus.PENDING
    )
    accepted= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.friend