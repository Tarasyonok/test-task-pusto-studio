# Generated by Django 5.1.1 on 2024-10-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task2", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="levelprize",
            name="received",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="playerlevel",
            name="completed",
            field=models.DateField(null=True),
        ),
    ]
