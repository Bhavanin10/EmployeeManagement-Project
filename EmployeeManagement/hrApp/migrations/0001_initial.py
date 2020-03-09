# Generated by Django 3.0.2 on 2020-03-09 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeId', models.CharField(max_length=10)),
                ('EmployeeName', models.CharField(max_length=15)),
                ('FathersName', models.CharField(max_length=15)),
                ('MothersName', models.CharField(max_length=15)),
                ('BloodGroup', models.CharField(max_length=3)),
                ('DateOfBirth', models.DateField()),
                ('Sex', models.CharField(max_length=5)),
                ('MaritalStatus', models.CharField(max_length=6)),
                ('SpouseName', models.CharField(max_length=15)),
                ('Designation', models.CharField(max_length=10)),
                ('EmergencyContact', models.IntegerField()),
            ],
            options={
                'db_table': 'Employee_data',
            },
        ),
    ]
