from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

from .utils import get_default_error_message, get_permission_full_name


def permission_required(perm: str, login_url=None, raise_exception=True, message=None):
    """
    Decorator for views that checks whether a user has a particular permission
    enabled, redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.

    if the permission is located in `plain_permissions` app, app_name ('plain_permissions') can be omitted

    i.e. if permission in `plain_permissions` app is `activate_account`, the following will work:
    @permission_required('activate_account')
    @permission_required('plain_permissions.activate_account')

    if the permission is located in another app, the app_name must be included
    @permission_required('app_name.permission_name')
    @permission_required('orders.Order.delete_order')

    """

    def check_perms(user):
        if isinstance(perm, str):
            perms = (get_permission_full_name(perm),)
        else:
            perms = perm
        # First check if the user has the permission (even anon users)
        if user.has_perms(perms):
            return True
        # In case the 403 handler should be called raise the exception
        error_message = message
        if error_message is None:
            error_message = get_default_error_message(perm)
        if raise_exception:
            raise PermissionDenied(error_message)
        # As the last resort, show the login form
        return False

    return user_passes_test(check_perms, login_url=login_url)
