# Generated by Django 3.1 on 2020-08-26 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_auto_20200826_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='Place',
        ),
    ]
