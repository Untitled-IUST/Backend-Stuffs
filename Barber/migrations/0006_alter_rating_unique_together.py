# Generated by Django 4.2 on 2023-04-26 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Barber', '0005_rating'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
    ]