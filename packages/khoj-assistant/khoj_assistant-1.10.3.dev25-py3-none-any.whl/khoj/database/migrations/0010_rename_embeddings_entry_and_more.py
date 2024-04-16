# Generated by Django 4.2.5 on 2023-10-26 23:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0009_khojapiuser"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Embeddings",
            new_name="Entry",
        ),
        migrations.RenameModel(
            old_name="EmbeddingsDates",
            new_name="EntryDates",
        ),
        migrations.RenameField(
            model_name="entrydates",
            old_name="embeddings",
            new_name="entry",
        ),
        migrations.RenameIndex(
            model_name="entrydates",
            new_name="database_en_date_8d823c_idx",
            old_name="database_em_date_a1ba47_idx",
        ),
    ]
