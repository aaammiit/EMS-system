# Generated by Django 4.2.5 on 2024-03-08 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employe', '0010_alter_employe_dig_alter_employe_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprov', models.BooleanField(default=False)),
                ('lstartdate', models.DateField(null=True)),
                ('lenddate', models.DateField(null=True)),
                ('ltype', models.CharField(max_length=100, null=True)),
                ('purpos', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]