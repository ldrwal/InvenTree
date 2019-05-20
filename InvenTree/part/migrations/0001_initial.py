# Generated by Django 2.2 on 2019-05-20 09:22

import InvenTree.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import part.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BomItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, help_text='BOM quantity for this BOM item', validators=[django.core.validators.MinValueValidator(0)])),
                ('overage', models.CharField(blank=True, help_text='Estimated build wastage quantity (absolute or percentage)', max_length=24, validators=[InvenTree.validators.validate_overage])),
                ('note', models.CharField(blank=True, help_text='BOM item notes', max_length=100)),
            ],
            options={
                'verbose_name': 'BOM Item',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Part name', max_length=100, validators=[InvenTree.validators.validate_part_name])),
                ('variant', models.CharField(blank=True, help_text='Part variant or revision code', max_length=32)),
                ('description', models.CharField(help_text='Part description', max_length=250)),
                ('keywords', models.CharField(blank=True, help_text='Part keywords to improve visibility in search results', max_length=250)),
                ('IPN', models.CharField(blank=True, help_text='Internal Part Number', max_length=100)),
                ('URL', models.URLField(blank=True, help_text='Link to extenal URL')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=part.models.rename_part_image)),
                ('minimum_stock', models.PositiveIntegerField(default=0, help_text='Minimum allowed stock level', validators=[django.core.validators.MinValueValidator(0)])),
                ('units', models.CharField(blank=True, default='pcs', help_text='Stock keeping units for this part', max_length=20)),
                ('buildable', models.BooleanField(default=False, help_text='Can this part be built from other parts?')),
                ('consumable', models.BooleanField(default=True, help_text='Can this part be used to build other parts?')),
                ('trackable', models.BooleanField(default=False, help_text='Does this part have tracking for unique items?')),
                ('purchaseable', models.BooleanField(default=True, help_text='Can this part be purchased from external suppliers?')),
                ('salable', models.BooleanField(default=False, help_text='Can this part be sold to customers?')),
                ('active', models.BooleanField(default=True, help_text='Is this part active?')),
                ('notes', models.TextField(blank=True)),
                ('bom_checksum', models.CharField(blank=True, help_text='Stored BOM checksum', max_length=128)),
                ('bom_checked_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Part',
                'verbose_name_plural': 'Parts',
            },
        ),
        migrations.CreateModel(
            name='PartAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(help_text='Select file to attach', upload_to=part.models.attach_file)),
                ('comment', models.CharField(help_text='File comment', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PartCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('default_keywords', models.CharField(blank=True, help_text='Default keywords for parts in this category', max_length=250)),
            ],
            options={
                'verbose_name': 'Part Category',
                'verbose_name_plural': 'Part Categories',
            },
        ),
        migrations.CreateModel(
            name='PartStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starred_users', to='part.Part')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starred_parts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
