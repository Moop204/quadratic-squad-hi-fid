# Generated by Django 2.0.5 on 2018-05-24 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180524_0935'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrolment',
            unique_together={('user', 'course')},
        ),
    ]
