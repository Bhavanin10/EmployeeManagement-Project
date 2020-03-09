from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('other','OTHER'),
)

MARITALSTATUS_CHOICES=(
    ('single','SINGLE'),
    ('married','MARRIED'),
)
class EmployeeDetails(models.Model):
    EmployeeId=models.CharField(max_length=10)
    EmployeeName=models.CharField(max_length=15)
    FathersName=models.CharField(max_length=15)
    MothersName=models.CharField(max_length=15)
    BloodGroup=models.CharField(max_length=3)
    DateOfBirth=models.DateField()
    gender=models.CharField(max_length=6, choices=GENDER_CHOICES, default='other')
    MaritalStatus=models.CharField(max_length=10, choices=MARITALSTATUS_CHOICES, default='other')
    SpouseName=models.CharField(max_length=15)
    Designation=models.CharField(max_length=25)
    EmergencyContact=models.IntegerField()

    class Meta:
        db_table='Employee_data'
