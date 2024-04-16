django-plain-permissions documentation
=======================================

Current State
-------------
Django by default allows you to define permissions related to a model.
as ::

    class Order(models.Model):
        class Meta:
            permissions = [
                ("delete_order", "Can delete order"),
            ]

however once you go beyond simple CRUD operations you will encounter many operations that will span multiple models.
i.e. checkout cart, place order, activate_account, etc...

Django also provides builtin permission for every model. i.e. add, change, delete, view.
This behavior is nice but adds a lot of clutter. and most of the time the business doesn't care about these permissions.

django-plain-permissions
-------------------------

django-plain-permissions allows you to define business-related permissions that don't have to be related to a model.
You can also reuse the builtin permissions, if you want your permission to affect the admin panel as well.
Define your permissions in settings.py file
as ::

    PERMISSIONS_SETTINGS = {
        "PERMISSIONS": [
            ("orders.Order.delete_order", "Delete Orders"), # reuse built-in permission
            ("merge_customers", "Merge Customers"),  # custom permission
            ("give_edit_permission", "Give Permission To Edit Permissions"),
            ("disable_user", "Disable Users"),
        ],

    }

django-plain-permissions plays well with the builtin permission and gives you extra utils to check if a user has a permission or not.
you can write your own permission checkers as well.

User.has_perm
-------------
is a builtin method that checks if the user has the permission or not.
it takes a string as an argument and returns True if the user has the permission, otherwise False.

    user.has_perm("orders.Order.delete_order") # will return True if the user has the permission

If you have ``"MONKEYPATCH_USER": True`` in your ``settings.py`` you can also use the builtin permission with the custom permissions

    user.has_perm("activate_account") # will return True if the user has the permission
if you have ``"MONKEYPATCH_USER": False`` in your ``settings.py``, you can use

    custom_has_perm(user, "activate_account") # will return True if the user has the permission

check_permission
----------------
is a flow control method that will Check if the user has the permission, if not raise PermissionDenied::

    def activate_account(request):
        check_permission(request.user, "activate_account") # will raise PermissionDenied if the user doesn't have the permission
        ActivationService.activate(request.user)
        return HttpResponse("Account Activated")



permission_required
-------------------
you can also use the decorator to check if the user has the permission or not::

    @permission_required("activate_account")
    def activate_account(request):
        ActivationService.activate(request.user)
        return HttpResponse("Account Activated")

Dependencies
============
1. Python >=3.9
2. Django >=3.2



Contents
--------

.. toctree::
   :maxdepth: 2

   installation
   usage


Contribute to django-plain-permissions
---------------------------------

If you discovered a bug or want to improve the code, please submit an issue and/or pull request via GitHub.
Before submitting a new issue, please make sure there is no issue submitted that involves the same problem.

| GitHub repository: https://github.com/hassaanalansary/django-plain-permissions
| Issues: https://github.com/hassaanalansary/django-plain-permissions


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
