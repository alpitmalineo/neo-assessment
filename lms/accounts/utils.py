from accounts.enums import RoleType
from accounts.models import Role, User


def is_admin_or_is_hod_or_is_staff(user):
    if user.is_authenticated:
        roles = [0, 1, 2]
        return user.role.role_type in roles
    return False


def is_staff(user):
    if user.is_authenticated:
        roles = [0, 2]
        return user.role.role_type in roles
    return False


def is_hod(user):
    if user.is_authenticated:
        roles = [0, 1]
        return user.role.role_type in roles
    return False
