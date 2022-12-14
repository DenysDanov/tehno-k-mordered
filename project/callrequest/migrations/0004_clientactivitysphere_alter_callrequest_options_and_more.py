# Generated by Django 4.1 on 2022-08-11 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("callrequest", "0003_remove_callrequest_call_page"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClientActivitySphere",
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
                    models.CharField(
                        max_length=50, verbose_name="Сфера деятельности клиента"
                    ),
                ),
            ],
            options={
                "verbose_name": "Сфера деятельности клиента",
                "verbose_name_plural": "Сферы деятельности клиента",
            },
        ),
        migrations.AlterModelOptions(
            name="callrequest",
            options={
                "verbose_name": "Заявка на звонок",
                "verbose_name_plural": "Заявки на звонок",
            },
        ),
        migrations.AlterModelOptions(
            name="callrequestcomment",
            options={
                "verbose_name": "Комментарий к заявке",
                "verbose_name_plural": "Комментарии к заявке",
            },
        ),
        migrations.AddField(
            model_name="callrequest",
            name="textarea",
            field=models.TextField(
                blank=True, null=True, verbose_name="О компании клиента"
            ),
        ),
        migrations.AddField(
            model_name="callrequest",
            name="activity",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="callrequest.clientactivitysphere",
            ),
        ),
    ]
