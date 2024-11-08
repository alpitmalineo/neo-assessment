from django.db import models


class StatusType(models.IntegerChoices):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3

