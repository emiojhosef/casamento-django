# Generated by Django 5.2 on 2025-05-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("casamento", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Convidado",
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
                ("nome", models.CharField(max_length=200)),
                ("telefone", models.CharField(max_length=14)),
                ("senha", models.CharField(max_length=6)),
            ],
        ),
    ]
