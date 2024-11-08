from django.conf import settings
from django.db import models

from dashboard.enums import StatusType


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


# Create your models here.
class Leave(TimeStamp):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()
    status = models.IntegerField(choices=StatusType.choices, default=StatusType.PENDING, help_text=StatusType.choices)

    def __str__(self):
        return f'{self.user.first_name}'
