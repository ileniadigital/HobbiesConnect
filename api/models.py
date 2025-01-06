from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.


class PageView(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Page view count: {self.count}"
class CustomUserManager(BaseUserManager):
    '''
    Custom manager for User model.
    Creating regular user and superuser.
    '''
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    '''
    Custom User model inheriting Django's AbstractUser with email as the unique identifier.
    '''
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

    USERNAME_FIELD = 'email' #username is email
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dob']
    #method to count hobbies used in the heap view
    @staticmethod
    def count_common_hobbies(user1, user2):
        '''
        Static method to count common hobbies between two users.
        '''
        user1_hobbies = set(UserHobby.objects.filter(user=user1).values_list('hobby', flat=True))
        user2_hobbies = set(UserHobby.objects.filter(user=user2).values_list('hobby', flat=True))
        
        common_hobbies = user1_hobbies.intersection(user2_hobbies)
        return len(common_hobbies)
    
    objects = CustomUserManager()

    def __str__(self):
        return self.first_name

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
        return self.hobby.name


class Friendship(models.Model):
    '''
    Friendship model to store friends and friends requests
    '''

    class FriendshipStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        ACCEPTED = 'ACCEPTED', 'Accepted'
        REJECTED = 'REJECTED', 'Rejected'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_initiated')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_received')
    status = models.CharField(
        max_length=50,
        choices=FriendshipStatus.choices,
        default=FriendshipStatus.PENDING
    )
    accepted= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} is friends with {self.friend.email} - Status: {self.status}"