from django.contrib.auth.models import Permission
from django.db import models


def permission_string_method(self):
    return f"{self.name}"


Permission.__str__ = permission_string_method


class Permission(models.Model):
    """Fake model to attach the permissions to it"""

    class Meta:
        managed = False
        db_table = ""
        default_permissions = []
