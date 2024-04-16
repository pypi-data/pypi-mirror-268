INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "tests",
    "plain_permissions",
)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}
SECRET_KEY = "dummy"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}


DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

USE_TZ = False

PERMISSIONS_SETTINGS = {
    "PERMISSIONS": [
        ("tests.Post.delete_post", "Delete Posts"),  # reuse built-in permission
        ("merge_customers", "Merge Customers"),  # custom permission
        ("give_edit_permission", "Give Permission To Edit Permissions"),
        ("disable_user", "Disable Users"),
    ],
    "DEFAULT_ERROR_MESSAGE": 'You do not have permission to "%s".',
    "MONKEYPATCH_USER": True,
    "OVERRIDE_GROUP_ADMIN": True,
    "OVERRIDE_USER_ADMIN": True,
    "SYNC_PERMISSIONS_POST_MIGRATE": True,
}
