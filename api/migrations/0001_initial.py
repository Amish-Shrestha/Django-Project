# Generated by Django 4.2.9 on 2024-01-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankState',
            fields=[
                ('RowId', models.AutoField(primary_key=True, serialize=False)),
                ('BankName', models.CharField(max_length=255)),
                ('BankShortName', models.CharField(max_length=50)),
                ('AccountNumber', models.CharField(default='', max_length=20, null=True)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('LatestDate', models.DateField()),
            ],
        ),
    ]
