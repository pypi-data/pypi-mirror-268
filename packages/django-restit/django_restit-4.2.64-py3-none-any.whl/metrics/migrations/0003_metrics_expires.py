# Generated by Django 4.1.4 on 2023-01-27 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0002_metrics_k11_metrics_k12_metrics_k13_metrics_k14_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='metrics',
            name='expires',
            field=models.DateTimeField(db_index=True, default=None, null=True),
        ),
    ]
