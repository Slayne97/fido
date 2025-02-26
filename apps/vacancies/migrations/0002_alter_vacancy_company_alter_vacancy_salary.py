# Generated by Django 5.1.3 on 2025-02-26 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vacancies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vacancy",
            name="company",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="salary",
            field=models.FloatField(null=True),
        ),
    ]
