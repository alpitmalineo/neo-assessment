from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, **kwargs):
        """
        Creates and saves a User with the given email
        """
        if not email:
            raise ValueError(_('The Email must be set'))

        password = kwargs.get('password', None)

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)

        if password:
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(
            email=email,
            **kwargs
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_normal_detail(self):
        return self.model.objects.only('id', 'name', 'user_image', 'email', 'mobile_number',
                                       'is_active', 'is_verified', 'user_type')

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def active(self):
        return self.model.objects.filter(active=True)
