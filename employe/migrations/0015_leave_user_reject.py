# Generated by Django 4.2.5 on 2024-03-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0014_leave_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_user',
            name='reject',
            field=models.BooleanField(default=False),
        ),
    ]
