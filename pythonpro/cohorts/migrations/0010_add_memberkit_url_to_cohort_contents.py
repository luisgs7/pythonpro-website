# Generated by Django 3.2.4 on 2021-06-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0009_increase_webinar_title_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveclass',
            name='memberkit_url',
            field=models.URLField(blank=True, default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='webinar',
            name='memberkit_url',
            field=models.URLField(blank=True, default='', max_length=1024),
        ),
    ]
