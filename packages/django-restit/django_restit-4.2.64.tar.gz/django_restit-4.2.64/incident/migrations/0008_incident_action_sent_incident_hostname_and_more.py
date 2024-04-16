# Generated by Django 4.1.4 on 2023-01-23 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0007_event_metadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='action_sent',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='hostname',
            field=models.CharField(db_index=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rule',
            name='action_after',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rule',
            name='bundle_by',
            field=models.IntegerField(default=3),
        ),
    ]
