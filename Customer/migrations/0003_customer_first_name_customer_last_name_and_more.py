# Generated by Django 4.2 on 2023-04-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0002_customer_delete_customerprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="first_name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="last_name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="profile_pic",
            field=models.ImageField(null=True, upload_to="customer/profile"),
        ),
    ]