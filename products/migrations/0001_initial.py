# Generated by Django 5.2.3 on 2025-06-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("nm_id", models.BigIntegerField(unique=True)),
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "discounted_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("rating", models.FloatField()),
                ("reviews_count", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
