from django import forms
from django.contrib import admin
from django.contrib.admin import widgets
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from plain_permissions.settings import permissions_settings
from plain_permissions.utils import get_permissions_queryset


class PlainPermissionsGroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    permissions = forms.ModelMultipleChoiceField(
        get_permissions_queryset(), widget=widgets.FilteredSelectMultiple(_("permissions"), False)
    )


class PlainPermissionsGroupAdmin(admin.ModelAdmin):
    form = PlainPermissionsGroupAdminForm
    search_fields = ("name",)
    ordering = ("name",)


class PlainPermissionsUserChangeForm(UserChangeForm):
    user_permissions = forms.ModelMultipleChoiceField(
        get_permissions_queryset(),
        required=False,
        widget=widgets.FilteredSelectMultiple(_("user_permissions"), False),
        help_text='Hold down "Control", or "Command" on a Mac, to select more than one.',
    )


class MyUserAdmin(UserAdmin):
    form = PlainPermissionsUserChangeForm


if permissions_settings.OVERRIDE_GROUP_ADMIN:
    admin.site.unregister(Group)
    admin.site.register(Group, PlainPermissionsGroupAdmin)
if permissions_settings.OVERRIDE_USER_ADMIN:
    admin.site.unregister(get_user_model())
    admin.site.register(get_user_model(), MyUserAdmin)
