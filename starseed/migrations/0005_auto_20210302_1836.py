# Generated by Django 3.1.7 on 2021-03-02 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starseed', '0004_auto_20210302_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='email',
            field=models.EmailField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='email1',
            field=models.EmailField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='email2',
            field=models.EmailField(default='', max_length=255),
        ),
    ]