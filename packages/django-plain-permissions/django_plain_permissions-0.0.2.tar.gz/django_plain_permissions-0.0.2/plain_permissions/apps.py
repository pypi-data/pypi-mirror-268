from django.apps import AppConfig
from django.db.models.signals import post_migrate


class PermissionsConfig(AppConfig):
    name = "plain_permissions"

    def ready(self):
        from plain_permissions.settings import permissions_settings
        from plain_permissions.signal_handlers import sync_permissions

        if permissions_settings.SYNC_PERMISSIONS_POST_MIGRATE:
            post_migrate.connect(sync_permissions, sender=self)

        if permissions_settings.MONKEYPATCH_USER:
            from django.contrib.auth import get_user_model

            from plain_permissions.utils import custom_has_perm

            User = get_user_model()
            User.has_perm = custom_has_perm
