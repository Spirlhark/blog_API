# Generated by Django 4.0.1 on 2022-01-25 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authoruser',
            new_name='author',
        ),
    ]
