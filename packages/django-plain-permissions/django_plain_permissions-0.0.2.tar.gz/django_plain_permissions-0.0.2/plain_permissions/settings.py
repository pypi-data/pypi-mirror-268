from __future__ import annotations

from typing import TypedDict

from django.conf import settings


class PermissionsSettingsDefaults(TypedDict):
    PERMISSIONS: list[tuple[str, str]]
    DEFAULT_ERROR_MESSAGE: str
    MONKEYPATCH_USER: bool
    OVERRIDE_GROUP_ADMIN: bool
    OVERRIDE_USER_ADMIN: bool
    SYNC_PERMISSIONS_POST_MIGRATE: bool


DEFAULTS: PermissionsSettingsDefaults = {
    "PERMISSIONS": [],
    "DEFAULT_ERROR_MESSAGE": 'You do not have permission to "%s"',
    "MONKEYPATCH_USER": True,
    "OVERRIDE_GROUP_ADMIN": True,
    "OVERRIDE_USER_ADMIN": False,
    "SYNC_PERMISSIONS_POST_MIGRATE": True,
}


class PermissionsSettings:
    def __init__(self, user_settings=None, defaults=None):
        if user_settings:
            self._user_settings = user_settings
        self.defaults = defaults or DEFAULTS

    @property
    def user_settings(self):
        if not hasattr(self, "_user_settings"):
            self._user_settings = getattr(settings, "PERMISSIONS_SETTINGS", {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid Permissions setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        setattr(self, attr, val)
        return val


permissions_settings = PermissionsSettings(None, DEFAULTS)
