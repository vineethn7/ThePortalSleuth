# Generated by Django 3.0.4 on 2020-03-13 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PortalSleuthMain', '0002_auto_20200313_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='url',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]