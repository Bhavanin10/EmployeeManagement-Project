# Generated by Django 3.0.2 on 2020-03-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrApp', '0007_auto_20200309_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='Designation',
            field=models.CharField(max_length=25),
        ),
    ]