from django.contrib.auth.models import Permission, User
from django.core.exceptions import PermissionDenied
from django.test import TestCase

from plain_permissions.utils import check_permission


class TestUtils(TestCase):
    def test_check_permission_should_not_raise_if_user_has_permission(self):
        user = User.objects.create_user(username="test", password="test")
        perm = Permission.objects.get(
            content_type__app_label="plain_permissions", content_type__model="permission", codename="disable_user"
        )
        user.user_permissions.add(perm)
        check_permission(user, "disable_user")

    def test_check_permission_should_raise_if_user_does_not_have_permission(self):
        user = User.objects.create_user(username="test", password="test")
        with self.assertRaises(PermissionDenied):
            check_permission(user, "disable_user")

    def test_has_perm_should_return_true_if_user_has_permission(self):
        user = User.objects.create_user(username="test", password="test")
        perm = Permission.objects.get(
            content_type__app_label="plain_permissions", content_type__model="permission", codename="disable_user"
        )
        user.user_permissions.add(perm)
        self.assertTrue(user.has_perm("plain_permissions.disable_user"))

    def test_has_perm_should_return_false_if_user_does_not_have_permission(self):
        user = User.objects.create_user(username="test", password="test")
        self.assertFalse(user.has_perm("plain_permissions.disable_user"))
