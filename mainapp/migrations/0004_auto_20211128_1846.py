# Generated by Django 3.2.9 on 2021-11-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20211128_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Availability of sd card'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Max sd memory'),
        ),
    ]