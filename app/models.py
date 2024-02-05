from django.db import models

# Create your models here.
class PremiumModel(models.Model):
    RowId = models.AutoField(primary_key=True)
    ProvinceCode = models.CharField(max_length=255)
    BranchCode = models.CharField(max_length=50)
    TodayPremium = models.DecimalField(max_digits=15, decimal_places=2)
    TotalPremium = models.DecimalField(max_digits=15, decimal_places=2)
    EmployeeId = models.CharField(max_length=50)
    CreatedDate = models.DateField()
    EditDate = models.DateField()
    
    
class filesUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    



    
    