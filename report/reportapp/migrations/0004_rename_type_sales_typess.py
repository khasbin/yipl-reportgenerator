# Generated by Django 3.2.7 on 2021-09-24 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0003_alter_year_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='type',
            new_name='typess',
        ),
    ]
