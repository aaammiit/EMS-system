# Generated by Django 4.2.5 on 2024-03-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='Ecode',
            field=models.IntegerField(unique=True),
        ),
    ]
