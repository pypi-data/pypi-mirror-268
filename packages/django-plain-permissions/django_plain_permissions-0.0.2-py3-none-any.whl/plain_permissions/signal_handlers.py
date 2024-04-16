from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from plain_permissions.models import Permission as CustomPermission
from plain_permissions.utils import get_permissions_tuple


def sync_permissions(sender, **kwargs):
    populate_permissions()
    delete_missing_permissions()


def populate_permissions():
    """add any permission that is not already in the database and update their name if they exists
    will skip permission that are in other apps.
    permissions that are in other apps have '.' in it i.e. 'app_name.model_name.permission_name'
    """
    for code_name, name in get_permissions_tuple():
        if "." in code_name:
            app_label, model_name, code_name = code_name.split(".")
            content_type = ContentType.objects.get(app_label=app_label, model=model_name.lower())
        else:
            content_type = ContentType.objects.get_for_model(CustomPermission)
        permission, _ = Permission.objects.update_or_create(
            codename=code_name, content_type=content_type, defaults={"name": name}
        )


def delete_missing_permissions():
    """delete all permissions in located in this app, but not in PERMISSIONS"""
    content_type = ContentType.objects.get_for_model(CustomPermission)
    code_names = [code_name for (code_name, name) in get_permissions_tuple() if "." not in code_name]
    Permission.objects.filter(content_type=content_type).exclude(codename__in=code_names).delete()
