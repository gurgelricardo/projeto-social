# Generated by Django 5.2.4 on 2025-07-19 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_birth_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="Data de nascimento"
            ),
        ),
    ]
