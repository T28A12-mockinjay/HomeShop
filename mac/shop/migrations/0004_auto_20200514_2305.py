# Generated by Django 3.0.5 on 2020-05-14 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200514_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='query',
        ),
    ]