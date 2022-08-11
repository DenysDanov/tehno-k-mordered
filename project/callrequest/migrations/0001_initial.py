# Generated by Django 4.1 on 2022-08-09 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CallRequestStatus",
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
                    "name",
                    models.CharField(max_length=50, verbose_name="Название статуса"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CallRequest",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="Имя заявителя"),
                ),
                ("phone", models.CharField(max_length=20, verbose_name="Телефон")),
                (
                    "call_page",
                    models.CharField(
                        max_length=100, verbose_name="Запрос пришел со страницы:"
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="callrequest.callrequeststatus",
                    ),
                ),
            ],
        ),
    ]
