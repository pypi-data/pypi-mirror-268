# Generated by Django 4.0.6 on 2022-08-11 21:50

from django.db import migrations, models
import django.db.models.deletion
import rest.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_authtoken_signature_authsession'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('uuid', models.CharField(blank=True, db_index=True, default=None, max_length=128, null=True)),
                ('cm_provider', models.CharField(db_index=True, default='fcm', max_length=64)),
                ('cm_token', models.CharField(default=None, max_length=250, null=True)),
                ('kind', models.CharField(db_index=True, default='unknown', max_length=64)),
                ('state', models.IntegerField(db_index=True, default=1)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='account.member')),
            ],
            bases=(models.Model, rest.models.RestModel, rest.models.MetaDataModel),
        ),
        migrations.CreateModel(
            name='MemberDeviceMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, db_index=True, default=None, max_length=32, null=True)),
                ('key', models.CharField(db_index=True, max_length=80)),
                ('value_format', models.CharField(max_length=16)),
                ('value', models.TextField()),
                ('int_value', models.IntegerField(blank=True, default=None, null=True)),
                ('float_value', models.IntegerField(blank=True, default=None, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='account.memberdevice')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
