# Generated by Django 4.2 on 2023-06-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_blog_code_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
