# Generated by Django 3.1.5 on 2021-01-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210122_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='Image',
            field=models.CharField(max_length=112),
        ),
    ]