# Generated by Django 4.2.2 on 2023-07-08 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Barber', '0004_remove_comment_reply_alter_transaction_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='text_body',
            field=models.TextField(default='comment-reply', max_length=1000),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 8, 17, 6, 30, 69570), null=True),
        ),
    ]
