# Generated by Django 3.1 on 2023-07-31 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20230731_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.FloatField(),
        ),
    ]
