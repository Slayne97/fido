# Generated by Django 5.1.3 on 2025-02-26 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("candidates", "0002_alter_candidate_email_alter_candidate_phone"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="candidate",
            name="resume",
        ),
    ]
