# Generated by Django 4.1.7 on 2023-04-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_story_date_type_story_season_name_story_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='location_id',
        ),
        migrations.AddField(
            model_name='story',
            name='locations',
            field=models.ManyToManyField(blank=True, to='user.location'),
        ),
    ]