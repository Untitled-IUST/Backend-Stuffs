# Generated by Django 4.2.1 on 2023-06-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0087_rename_servicepic_categoryservice_servicepic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoryservice",
            name="servicePic",
            field=models.ImageField(
                default="default_profile.png", null=True, upload_to="Barber/Service"
            ),
        ),
    ]
