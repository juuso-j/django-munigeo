# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-11 06:15
from __future__ import unicode_literals

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields

from munigeo.utils import get_default_srid
DEFAULT_SRID = get_default_srid()


class Migration(migrations.Migration):

    replaces = [('munigeo', '0001_initial'), ('munigeo', '0002_auto_20150608_1607'), ('munigeo', '0003_add_modified_time_to_address_and_street'), ('munigeo', '0004_building')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, help_text='Building number', max_length=6)),
                ('number_end', models.CharField(blank=True, help_text='Building number end (if range specified)', max_length=6)),
                ('letter', models.CharField(blank=True, help_text='Building letter if applicable', max_length=2)),
                ('location', django.contrib.gis.db.models.fields.PointField(help_text='Coordinates of the address', srid=DEFAULT_SRID)),
            ],
            options={
                'ordering': ['street', 'number'],
            },
        ),
        migrations.CreateModel(
            name='AdministrativeDivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_fi', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_sv', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_en', models.CharField(db_index=True, max_length=100, null=True)),
                ('origin_id', models.CharField(db_index=True, max_length=50)),
                ('ocd_id', models.CharField(db_index=True, help_text='Open Civic Data identifier', max_length=200, null=True, unique=True)),
                ('service_point_id', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('start', models.DateField(null=True)),
                ('end', models.DateField(null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Time when the information was last changed')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='AdministrativeDivisionGeometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boundary', django.contrib.gis.db.models.fields.MultiPolygonField(srid=DEFAULT_SRID)),
                ('division', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='geometry', to='munigeo.AdministrativeDivision')),
            ],
        ),
        migrations.CreateModel(
            name='AdministrativeDivisionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(db_index=True, help_text='Type name of the division (e.g. muni, school_district)', max_length=60, unique=True)),
                ('name', models.CharField(help_text='Human-readable name for the division', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_fi', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_sv', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_en', models.CharField(db_index=True, max_length=100, null=True)),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muni', to='munigeo.AdministrativeDivision', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=DEFAULT_SRID)),
                ('origin_id', models.CharField(max_length=20)),
                ('in_effect', models.BooleanField(default=False)),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='munigeo.Municipality')),
            ],
        ),
        migrations.CreateModel(
            name='POI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=DEFAULT_SRID)),
                ('street_address', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('origin_id', models.CharField(db_index=True, max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='POICategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(db_index=True, max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('name_fi', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_sv', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_en', models.CharField(db_index=True, max_length=100, null=True)),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='munigeo.Municipality')),
                ('modified_at', models.DateTimeField(auto_now=True, default=datetime.datetime(1970, 1, 1, 2, 0, tzinfo=datetime.timezone.utc), help_text='Time when the information was last changed')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='street',
            unique_together=set([('municipality', 'name')]),
        ),
        migrations.AddField(
            model_name='poi',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='munigeo.POICategory'),
        ),
        migrations.AddField(
            model_name='poi',
            name='municipality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='munigeo.Municipality'),
        ),
        migrations.AlterUniqueTogether(
            name='plan',
            unique_together=set([('municipality', 'origin_id')]),
        ),
        migrations.AddField(
            model_name='administrativedivision',
            name='municipality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='munigeo.Municipality'),
        ),
        migrations.AddField(
            model_name='administrativedivision',
            name='parent',
            field=mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='munigeo.AdministrativeDivision'),
        ),
        migrations.AddField(
            model_name='administrativedivision',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='munigeo.AdministrativeDivisionType'),
        ),
        migrations.AlterUniqueTogether(
            name='administrativedivision',
            unique_together=set([('origin_id', 'type', 'parent')]),
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='munigeo.Street'),
        ),
        migrations.AddField(
            model_name='address',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(1970, 1, 1, 2, 0, tzinfo=datetime.timezone.utc), help_text='Time when the information was last changed'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('street', 'number', 'number_end', 'letter')]),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='division',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muni', to='munigeo.AdministrativeDivision'),
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_id', models.CharField(db_index=True, max_length=40)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=DEFAULT_SRID)),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Time when the information was last changed')),
                ('addresses', models.ManyToManyField(blank=True, to='munigeo.Address')),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='munigeo.Municipality')),
            ],
            options={
                'ordering': ['municipality', 'origin_id'],
            },
        ),
    ]
