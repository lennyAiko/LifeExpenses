# Generated by Django 3.1.1 on 2020-09-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0004_auto_20200908_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='status',
            field=models.CharField(choices=[(0, 'In progress'), (1, 'Completed')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=70, null=True),
        ),
    ]