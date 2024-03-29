# Generated by Django 5.0.1 on 2024-02-17 17:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0003_alter_note_author"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="note",
            options={
                "ordering": ["-updated_at"],
                "verbose_name": "Note",
                "verbose_name_plural": "Notes",
            },
        ),
        migrations.AlterField(
            model_name="note",
            name="text",
            field=ckeditor.fields.RichTextField(unique=True, verbose_name="Text"),
        ),
        migrations.AlterField(
            model_name="note",
            name="title",
            field=ckeditor.fields.RichTextField(
                max_length=128, unique=True, verbose_name="Title"
            ),
        ),
    ]
