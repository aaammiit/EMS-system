# Generated by Django 4.2.5 on 2024-03-07 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0007_alter_emp_exp_fresher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp_edu',
            name='emp',
        ),
        migrations.RemoveField(
            model_name='emp_exp',
            name='emp',
        ),
    ]
