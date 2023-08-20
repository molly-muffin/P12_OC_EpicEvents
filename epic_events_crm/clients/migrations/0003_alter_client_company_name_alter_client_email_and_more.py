# Generated by Django 4.2 on 2023-08-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_rename_date_created_client_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='company_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='client',
            name='notes',
            field=models.CharField(max_length=150),
        ),
    ]
