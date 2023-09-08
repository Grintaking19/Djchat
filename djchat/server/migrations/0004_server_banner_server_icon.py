# Generated by Django 4.2.4 on 2023-08-23 14:17

from django.db import migrations, models
import server.models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0003_category_icon"),
    ]

    operations = [
        migrations.AddField(
            model_name="server",
            name="banner",
            field=models.ImageField(
                blank=True, null=True, upload_to=server.models.server_banner_upload_path
            ),
        ),
        migrations.AddField(
            model_name="server",
            name="icon",
            field=models.ImageField(
                blank=True, null=True, upload_to=server.models.server_icon_upload_path
            ),
        ),
    ]