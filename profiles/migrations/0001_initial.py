# Generated by Django 3.2.11 on 2022-01-24 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=13)),
                ('country', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profiles',
            },
        ),
    ]
