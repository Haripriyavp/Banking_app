# Generated by Django 4.1.7 on 2023-05-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetails',
            name='materials_provided',
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='Cheque Book',
            field=models.BooleanField(default=False, verbose_name='Debit Card'),
        ),
    ]