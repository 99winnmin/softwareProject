# Generated by Django 4.0.4 on 2022-05-21 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0008_downloadlist_download_user_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='downloadlist',
            table='DownloadList',
        ),
        migrations.AlterModelTable(
            name='likelist',
            table='LikeList',
        ),
    ]
