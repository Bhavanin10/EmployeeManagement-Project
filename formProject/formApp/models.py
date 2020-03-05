from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=20)
    rollno=models.IntegerField()
    email=models.EmailField(max_length=50)
    feedback=models.CharField(max_length=150,default='not available')

    class Meta:
        db_table='student'
