# Generated by Django 4.2 on 2023-06-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_comment_blog_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subject',
            field=models.TextField(null=True),
        ),
    ]
