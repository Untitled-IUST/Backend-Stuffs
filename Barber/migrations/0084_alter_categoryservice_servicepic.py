# Generated by Django 4.2.1 on 2023-06-01 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0083_alter_barberpremium_expire_date_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoryservice",
            name="servicePic",
            field=models.ImageField(
                default="default_profile.png", upload_to="Barber/Service"
            ),
        ),
    ]
