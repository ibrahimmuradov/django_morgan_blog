# Generated by Django 4.2 on 2023-06-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.BooleanField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], default='Deactive'),
        ),
    ]
