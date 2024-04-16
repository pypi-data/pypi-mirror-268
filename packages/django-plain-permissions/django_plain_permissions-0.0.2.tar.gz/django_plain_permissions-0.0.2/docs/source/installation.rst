Installation
============

Installing django-plain-permissions is simple and straightforward. First of all, you need a copy of ``django-plain-permissions`` on your system. The easiest
way to do this is by using the Python Package Index (PyPI). Simply run the following command:

``pip install django-plain-permissions``

Instead of installing ``django-plain-permissions`` via PyPI, you can also clone the Git repository or download the source code via GitHub.
The repository can be found at https://github.com/hassaanalansary/django-plain-permissions/.

**Requirements**

- Python 3.9 or higher
- Django 3.2 or higher

``django-plain-permissions`` is currently tested with Python 3.9+ and Django 3.2 and 4.0+.

Adding django-plain-permissions to your Django application
-----------------------------------------------------

To use django-plain-permissions in your application,
add ``'plain_permissions'`` to your project's ``INSTALLED_APPS`` ``settings.py``

if whenever you change the permissions you need to run the following command to apply the changes to the database

``python manage.py migrate``
