# Generated by Django 3.2.4 on 2021-06-26 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='conact_date',
            new_name='contact_date',
        ),
    ]
