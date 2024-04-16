from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
