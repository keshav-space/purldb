# Generated by Django 4.1.2 on 2023-08-08 23:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("packagedb", "0076_rename_history_json_package_history"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="package",
            name="declared_license_expression_spdx",
        ),
        migrations.RemoveField(
            model_name="package",
            name="other_license_expression_spdx",
        ),
    ]