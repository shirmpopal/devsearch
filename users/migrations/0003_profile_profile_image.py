# Generated by Django 4.0 on 2022-01-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='profiles/user-default.png', upload_to='profiles/'),
        ),
    ]
