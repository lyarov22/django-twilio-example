# Generated by Django 5.0.6 on 2024-06-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x000001E1FD1AF1A0>', max_length=200),
        ),
    ]
