# Generated by Django 3.1.5 on 2021-01-22 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210122_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetail',
            old_name='otherlinks',
            new_name='other',
        ),
    ]
