from django.db import models


class RoleType(models.IntegerChoices):
    ADMIN = 0
    HOD = 1
    STAFF = 2


class UserGender(models.IntegerChoices):
    MALE = 1
    FEMALE = 2
    OTHER = 3
