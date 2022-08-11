# Generated by Django 4.1 on 2022-08-08 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
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
                    models.CharField(max_length=100, verbose_name="Название услуги"),
                ),
                ("slug", models.SlugField(unique=True, verbose_name="SLUG услуги")),
                (
                    "image",
                    models.ImageField(
                        upload_to="main/service/image/",
                        verbose_name="Изображения для услуги",
                    ),
                ),
                (
                    "descr",
                    models.CharField(max_length=350, verbose_name="Описание услуги"),
                ),
            ],
            options={
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
            },
        ),
        migrations.CreateModel(
            name="ServiceCategory",
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
                    models.CharField(max_length=100, verbose_name="Название категории"),
                ),
                ("slug", models.SlugField(unique=True, verbose_name="SLUG категории")),
                ("descr", models.TextField(verbose_name="Описание категории")),
            ],
            options={
                "verbose_name": "Категория услуги",
                "verbose_name_plural": "Категории услуги",
            },
        ),
        migrations.CreateModel(
            name="WhatWeDoInfo",
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
                ("text_main", models.TextField(verbose_name="Главный текст")),
                ("text_second", models.TextField(verbose_name="Второй текст")),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_query_name="whatwedo",
                        to="services.service",
                    ),
                ),
            ],
            options={
                "verbose_name": "Что мы делаем",
            },
        ),
        migrations.CreateModel(
            name="WhatWeDoUlUnits",
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
                ("text", models.CharField(max_length=100, verbose_name="Текст")),
                (
                    "info_block",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_query_name="li",
                        to="services.whatwedoinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WhatWeDoOlUnits",
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
                ("text", models.CharField(max_length=100, verbose_name="Текст")),
                (
                    "info_block",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_query_name="ol",
                        to="services.whatwedoinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TabsSectionInfo",
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
                ("title", models.CharField(max_length=100, verbose_name="Заголовок")),
                (
                    "image",
                    models.ImageField(
                        upload_to="main/service/important/", verbose_name="Изображение"
                    ),
                ),
                ("text", models.TextField(verbose_name="Текст")),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_query_name="tabs",
                        to="services.service",
                    ),
                ),
            ],
            options={
                "verbose_name": "tabs-section",
            },
        ),
        migrations.CreateModel(
            name="ServiceImportantInfo",
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
                ("title", models.CharField(max_length=100, verbose_name="Заголовок")),
                (
                    "image",
                    models.ImageField(
                        upload_to="main/service/important/", verbose_name="Изображение"
                    ),
                ),
                ("text", models.TextField(verbose_name="Текст")),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_query_name="important",
                        to="services.service",
                    ),
                ),
            ],
            options={
                "verbose_name": "Важное",
            },
        ),
        migrations.AddField(
            model_name="service",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_query_name="services",
                to="services.servicecategory",
            ),
        ),
        migrations.CreateModel(
            name="HowServiceWorksInfo",
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
                    "text_block",
                    models.CharField(max_length=256, verbose_name="Краткий блок"),
                ),
                (
                    "text_yellow_block",
                    models.CharField(max_length=256, verbose_name="Краткий блок"),
                ),
                ("text_big_block", models.TextField(verbose_name="Большой блок")),
                (
                    "youtube_video_link",
                    models.URLField(verbose_name="Ссылка на видео с Youtube"),
                ),
                (
                    "service",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_query_name="how_it_works",
                        to="services.service",
                    ),
                ),
            ],
            options={
                "verbose_name": "Как работает?",
            },
        ),
    ]