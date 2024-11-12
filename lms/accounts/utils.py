from accounts.enums import RoleType
from accounts.models import User


def is_admin_or_is_hod_or_is_staff(user):
    if user is not None and user.is_authenticated:
        return user.role_type == RoleType.ADMIN or user.role_type == RoleType.STAFF or user.role_type == RoleType.HOD
    return False


def is_staff(user):
    if user is not None and user.is_authenticated:
        return user.role_type == RoleType.STAFF
    return False


def is_hod(user):
    if user is not None and user.is_authenticated:
        return user.role_type == RoleType.HOD
    return False
