# Generated by Django 3.1 on 2020-08-31 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0004_member_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='Region',
        ),
    ]
