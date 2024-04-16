# Generated by Django 4.1.1 on 2022-09-24 16:22

from django.db import migrations
import rest.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_memberdevice_memberdevicemetadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=rest.fields.FormattedField(db_index=True, default=None, max_length=64, null=True),
        ),
    ]
