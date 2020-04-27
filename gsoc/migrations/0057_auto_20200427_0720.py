# Generated by Django 2.2.12 on 2020-04-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsoc', '0056_userprofile_gsoc_invited'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='userprofile',
            constraint=models.UniqueConstraint(fields=('suborg_full_name', 'user', 'gsoc_year'), name='unique_draft_user'),
        ),
    ]