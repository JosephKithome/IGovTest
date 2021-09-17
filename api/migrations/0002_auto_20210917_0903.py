# Generated by Django 3.2.7 on 2021-09-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discontinued',
            options={'verbose_name': 'Discontinued', 'verbose_name_plural': 'Discontinued'},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'Vehicle', 'verbose_name_plural': 'Vehicles'},
        ),
        migrations.AddField(
            model_name='discontinued',
            name='period',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
