# Generated by Django 4.2 on 2023-04-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0003_customer_first_name_customer_last_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="profile_pic",
            field=models.ImageField(
                default="default_profile.png", upload_to="customer/profile"
            ),
        ),
    ]
