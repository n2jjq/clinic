# Generated by Django 3.2.8 on 2021-10-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='address',
            field=models.BooleanField(default=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='department',
            field=models.BooleanField(default=True, verbose_name='department'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='friday',
            field=models.BooleanField(default=True, verbose_name='friday'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='holiday',
            field=models.BooleanField(default=True, verbose_name='holiday'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='monday',
            field=models.BooleanField(default=True, verbose_name='monday'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='name',
            field=models.BooleanField(default=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='saturday',
            field=models.BooleanField(default=True, verbose_name='saturday'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='sunday',
            field=models.BooleanField(default=True, verbose_name='sunday'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='thursday',
            field=models.BooleanField(default=True, verbose_name='thursday'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='tuesday',
            field=models.BooleanField(default=True, verbose_name='tuesday'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='wednesday',
            field=models.BooleanField(default=True, verbose_name='wednesday'),
        ),
    ]
