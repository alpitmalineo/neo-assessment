from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from accounts.enums import RoleType


class UserManager(BaseUserManager):
    def create_user(self, username, **kwargs):
        """
        Creates and saves a User with the given username
        """
        if not username:
            raise ValueError(_('The Username must be set'))

        password = kwargs.get('password', None)

        user = self.model(username=username, **kwargs)

        if password:
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **kwargs):
        user = self.create_user(
            username=username,
            **kwargs
        )
        user.set_password(password)
        user.role_type = RoleType.ADMIN
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_normal_detail(self):
        return self.model.objects.only('id', 'name', 'username', 'mobile_number',
                                       'is_active', 'role')

    def get_by_natural_key(self, username):
        return self.get(username=username)

    def active(self):
        return self.model.objects.filter(active=True)
