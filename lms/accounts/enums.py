from django.db import models


class RoleType(models.IntegerChoices):
    ADMIN = 0, "Admin"
    HOD = 1, "Head of Department"
    STAFF = 2, "Staff"


class UserGender(models.IntegerChoices):
    MALE = 1
    FEMALE = 2
    OTHER = 3
