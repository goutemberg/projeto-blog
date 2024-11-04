# Generated by Django 5.1 on 2024-08-27 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0002_sitesetup_menulink_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menulink',
            name='description',
        ),
        migrations.RemoveField(
            model_name='menulink',
            name='show_description',
        ),
        migrations.RemoveField(
            model_name='menulink',
            name='show_footer',
        ),
        migrations.RemoveField(
            model_name='menulink',
            name='show_header',
        ),
        migrations.RemoveField(
            model_name='menulink',
            name='show_menu',
        ),
        migrations.RemoveField(
            model_name='menulink',
            name='show_pagination',
        ),
        migrations.RemoveField(
            model_name='menulink',
            name='show_search',
        ),
        migrations.RemoveField(
            model_name='menulink',
            name='title',
        ),
        migrations.AddField(
            model_name='menulink',
            name='site_setup',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_setup.sitesetup'),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='description',
            field=models.CharField(default='Sem descrição', max_length=255),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='show_description',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='show_footer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='show_header',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='show_menu',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='show_pagination',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='show_search',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='title',
            field=models.CharField(default='Sem Title', max_length=65),
        ),
    ]