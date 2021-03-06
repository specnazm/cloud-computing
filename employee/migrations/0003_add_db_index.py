# Generated by Django 3.2.9 on 2021-12-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='surname',
            field=models.CharField(db_index=True, max_length=512),
        ),
    ]
