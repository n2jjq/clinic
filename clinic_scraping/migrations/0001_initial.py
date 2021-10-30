# Generated by Django 3.2.8 on 2021-10-30 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.BooleanField(default=True, verbose_name='')),
                ('address', models.BooleanField(default=True, verbose_name='')),
                ('department', models.BooleanField(default=True, verbose_name='')),
                ('monday', models.BooleanField(default=True, verbose_name='')),
                ('tuesday', models.BooleanField(default=True, verbose_name='')),
                ('wednesday', models.BooleanField(default=True, verbose_name='')),
                ('friday', models.BooleanField(default=True, verbose_name='')),
                ('thursday', models.BooleanField(default=True, verbose_name='')),
                ('sunday', models.BooleanField(default=True, verbose_name='')),
                ('holiday', models.BooleanField(default=True, verbose_name='')),
            ],
        ),
    ]