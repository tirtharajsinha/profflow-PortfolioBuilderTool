# Generated by Django 3.1.5 on 2021-01-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_userdetail_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='facebook',
            field=models.CharField(default='https://facebook.com', max_length=112),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='instagram',
            field=models.CharField(default='https://instagram.com', max_length=112),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='twitter',
            field=models.CharField(default='https://twitter.com', max_length=112),
        ),
    ]
