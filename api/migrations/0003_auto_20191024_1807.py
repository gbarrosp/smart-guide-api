# Generated by Django 2.2.5 on 2019-10-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191015_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_guest',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='knowledge',
            field=models.IntegerField(blank=True, choices=[(1, 'Children'), (2, 'Adult')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='standdescription',
            name='knowledge',
            field=models.IntegerField(blank=True, choices=[(1, 'Children'), (2, 'Adult')], null=True),
        ),
    ]
