from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from plain_permissions.signal_handlers import sync_permissions
from tests.models import Post


class TestSyncPermissions(TestCase):
    def test_sync_permissions(self):
        # act
        # sync_permissions(None) is called after migration

        # assert
        from plain_permissions.models import Permission as CustomPermission

        content_type = ContentType.objects.get_for_model(CustomPermission)

        for perm in ["merge_customers", "give_edit_permission", "disable_user"]:
            assert Permission.objects.filter(content_type=content_type, codename=perm).exists()

        for perm in ["delete_post"]:
            assert Permission.objects.filter(
                content_type=ContentType.objects.get_for_model(Post), codename=perm
            ).exists()

    def test_removing_permission(self):
        # arrange
        from plain_permissions.settings import permissions_settings

        settings.PERMISSIONS_SETTINGS["PERMISSIONS"] = [
            ("merge_customers", "Merge Customers"),
        ]
        del permissions_settings.PERMISSIONS
        # act
        sync_permissions(None)

        # assert
        from plain_permissions.models import Permission as CustomPermission

        content_type = ContentType.objects.get_for_model(CustomPermission)

        for perm in ["give_edit_permission", "disable_user"]:
            assert False == Permission.objects.filter(content_type=content_type, codename=perm).exists()
