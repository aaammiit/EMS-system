# Generated by Django 4.2.5 on 2024-03-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0005_emp_exp'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_exp',
            name='fresher',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
