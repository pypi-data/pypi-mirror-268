Usage
=====
in your ``settings.py``::

    PERMISSIONS_SETTINGS = {
    "PERMISSIONS": [
        ("orders.Order.delete_order", "Delete Orders"), # reuse built-in permission
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
