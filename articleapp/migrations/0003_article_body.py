# Generated by Django 4.0.3 on 2022-04-04 02:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0002_delete_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]