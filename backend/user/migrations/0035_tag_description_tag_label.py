# Generated by Django 4.2.7 on 2023-11-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_tag_remove_story_story_tags_story_story_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='label',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
