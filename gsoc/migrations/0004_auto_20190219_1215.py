# Generated by Django 2.1.7 on 2019-02-19 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("gsoc", "0003_auto_20190219_0320")]

    operations = [
        migrations.AddField(
            model_name="scheduler",
            name="last_error",
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="scheduler",
            name="success",
            field=models.BooleanField(default=None, null=True),
        ),
    ]
