from __future__ import annotations

from functools import reduce
from operator import or_

from django.contrib.auth.models import Permission, _user_has_perm
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from plain_permissions.apps import PermissionsConfig
from plain_permissions.settings import permissions_settings


def check_permission(user, perm: str) -> None:
    """Check if the user has the permission, if not raise PermissionDenied"""
    if not user.has_perm(get_permission_full_name(perm)):
        raise PermissionDenied(get_default_error_message(perm))


def get_default_error_message(perm: str) -> str:
    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType

    from plain_permissions.models import Permission as CustomPermission

    content_type = ContentType.objects.get_for_model(CustomPermission)
    permission_readable_name = Permission.objects.get(content_type=content_type, codename=perm).name
    error_message = permissions_settings.DEFAULT_ERROR_MESSAGE % permission_readable_name
    return error_message


def get_permission_full_name(perm: str) -> str:
    """if app_name is not included in the permission name, it will default to plain_permissions app_name"""
    my_perm = perm
    if "." not in my_perm:
        my_perm = PermissionsConfig.name + "." + perm
    return my_perm


def get_permissions_queryset():
    """return `Permission Queryset` that are defined in settings.PERMISSIONS_SETTINGS and in the database
    ignores the builtin permissions that are not mentioned in settings.PERMISSIONS_SETTINGS
    """
    custom_permissions = Q(content_type__app_label="plain_permissions", content_type__model="permission")
    q_objs = [custom_permissions]
    builtin_permissions = [p[0] for p in get_permissions_tuple() if "." in p[0]]
    for p in builtin_permissions:
        app_label, model_name, permission_name = p.split(".")
        q_objs.append(
            Q(codename=permission_name, content_type__app_label=app_label, content_type__model=model_name.lower())
        )
    query = reduce(or_, q_objs)
    return Permission.objects.filter(query)


def custom_has_perm(user, perm: str, obj=None) -> bool:
    """
    Return True if the user has the specified permission. Query all
    available auth backends, but return immediately if any backend returns
    True. Thus, a user who has permission from a single auth backend is
    assumed to have permission in general. If an object is provided, check
    permissions for that object.
    """
    perm = get_permission_full_name(perm)

    # Active superusers have all permissions.
    if user.is_active and user.is_superuser:
        return True

    # Otherwise we need to check the backends.
    return _user_has_perm(user, perm, obj)


def get_permissions_tuple() -> list[tuple[str, str]]:
    return permissions_settings.PERMISSIONS
