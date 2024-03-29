# Generated by Django 4.2 on 2023-04-30 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Barber", "0056_alter_orderservices_service_delete_service"),
    ]

    operations = [
        migrations.AlterField(
            model_name="barber",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
