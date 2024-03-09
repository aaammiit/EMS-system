# Generated by Django 4.2.5 on 2024-03-07 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employe', '0003_employe_dept_employe_gender_employe_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp_Edu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('first_edu', models.CharField(max_length=100, null=True)),
                ('first_p_year', models.CharField(max_length=100, null=True)),
                ('first_col', models.CharField(max_length=100, null=True)),
                ('sec_edu', models.CharField(max_length=100, null=True)),
                ('sec_p_year', models.CharField(max_length=100, null=True)),
                ('sec_col', models.CharField(max_length=100, null=True)),
                ('thrd_edu', models.CharField(max_length=100, null=True)),
                ('thrd_p_year', models.CharField(max_length=100, null=True)),
                ('thrd_col', models.CharField(max_length=100, null=True)),
                ('four_edu', models.CharField(max_length=100, null=True)),
                ('four_p_year', models.CharField(max_length=100, null=True)),
                ('four_col', models.CharField(max_length=100, null=True)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employe.employe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]