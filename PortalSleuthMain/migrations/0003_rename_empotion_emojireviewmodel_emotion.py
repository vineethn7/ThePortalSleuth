# Generated by Django 3.2 on 2021-05-02 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PortalSleuthMain', '0002_emojireviewmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emojireviewmodel',
            old_name='empotion',
            new_name='emotion',
        ),
    ]