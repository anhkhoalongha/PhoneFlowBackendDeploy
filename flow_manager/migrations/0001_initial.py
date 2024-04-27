# Generated by Django 5.0.3 on 2024-04-22 04:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FLow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                ("name", models.TextField(unique=True)),
                ("flow_chart", models.JSONField(blank=True, null=True)),
                ("IPScan", models.TextField(blank=True, default="", null=True)),
                ("loop_time", models.IntegerField(blank=True, default=1, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="IP",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                ("ip", models.TextField(default="")),
                (
                    "flow",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flow_manager.flow",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]