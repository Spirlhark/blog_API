# Generated by Django 4.0.1 on 2022-01-25 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_authoruser_alter_review_parent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
