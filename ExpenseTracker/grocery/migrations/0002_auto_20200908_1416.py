# Generated by Django 3.1.1 on 2020-09-08 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='list',
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
