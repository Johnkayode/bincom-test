# Generated by Django 3.2.7 on 2021-09-20 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_auto_20210921_0054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcedlgaresults',
            options={'managed': False, 'verbose_name_plural': 'announced_lga_results'},
        ),
        migrations.AlterModelOptions(
            name='announcedpuresults',
            options={'managed': False, 'verbose_name_plural': 'announced_pu_results'},
        ),
    ]
