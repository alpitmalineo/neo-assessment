from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from accounts.enums import UserGender, RoleType
from accounts.manager import UserManager


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Role(TimeStamp):
    role_type = models.IntegerField(choices=RoleType.choices, help_text=RoleType.choices)

    def __str__(self):
        return f'{self.get_role_type_display()}'

class Department(TimeStamp):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class User(AbstractUser, TimeStamp):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(unique=True, max_length=254)
    email = models.EmailField(unique=True)
    mobile_number = PhoneNumberField()
    image = models.ImageField(upload_to='image', null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return f'{self.pk} - {self.username}'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Profile(TimeStamp):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=UserGender.choices, help_text=UserGender.choices, null=True)

    def __str__(self):
        return f'{self.pk} - {self.user.username}'
