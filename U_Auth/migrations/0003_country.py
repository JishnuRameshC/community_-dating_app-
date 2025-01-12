# Generated by Django 5.0.6 on 2024-06-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_Auth', '0002_user_dob_user_gender_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('country_code', models.CharField(max_length=3)),
            ],
        ),
    ]
