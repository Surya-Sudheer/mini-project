# Generated by Django 4.0.4 on 2023-05-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macares', '0002_rename_place_user_district_user_cmp_user_occupation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='hospital',
        ),
        migrations.AddField(
            model_name='user',
            name='ashaid',
            field=models.IntegerField(default='0'),
        ),
    ]