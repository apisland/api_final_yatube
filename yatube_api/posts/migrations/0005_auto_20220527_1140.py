# Generated by Django 2.2.16 on 2022-05-27 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220527_1124'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='follow_1_time_no_self_follow',
        ),
    ]
