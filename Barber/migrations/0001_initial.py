# Generated by Django 4.2 on 2023-04-24 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Customer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BarberShop', models.CharField(max_length=255, unique=True)),
                ('Owner', models.CharField(max_length=255)),
                ('Parvaneh', models.CharField(max_length=10, unique=True)),
                ('phone_Number', models.CharField(max_length=11, unique=True)),
                ('area', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('rate', models.FloatField(default=1)),
                ('background', models.ImageField(default='default_profile.png', upload_to='Barber/backg')),
                ('logo', models.ImageField(default='default_profile.png', upload_to='Barber/Logo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(blank=True, max_length=255)),
                ('price', models.FloatField(default=0)),
                ('service_pic', models.ImageField(default='default_profile.png', null=True, upload_to='Barber/Service')),
                ('category', models.CharField(choices=[('hair', 'hair'), ('skin', 'skin'), ('makeup', 'makeup'), ('nail', 'nail')], max_length=20)),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='Barber.barber')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('barbershop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='barbers', to='Barber.barber')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Barber.barber')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors_comments', to='Customer.customer')),
                ('parent_comment', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Barber.comment')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
