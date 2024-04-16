import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("publish_date", models.DateField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="posts", to="tests.author"
                    ),
                ),
            ],
        ),
    ]
