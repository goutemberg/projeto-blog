# Generated by Django 5.1 on 2024-08-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0003_remove_menulink_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m/'),
        ),
    ]
