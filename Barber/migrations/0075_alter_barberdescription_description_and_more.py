# Generated by Django 4.2.1 on 2023-05-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0074_alter_barber_expire_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="barberdescription",
            name="description",
            field=models.TextField(default="description", max_length=256),
        ),
        migrations.AlterField(
            model_name="barberdescription",
            name="title",
            field=models.CharField(default="title", max_length=40),
        ),
    ]
