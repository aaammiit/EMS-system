# Generated by Django 4.2.5 on 2024-03-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0002_alter_employe_ecode'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='dept',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employe',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employe',
            name='img',
            field=models.ImageField(null=True, upload_to='profile'),
        ),
    ]
