from django.db import models

# Create your models here.
class claimsReports(models.Model):
    RowId = models.AutoField(primary_key=True)
    ReinsurerName = models.CharField(max_length=255)
    Period = models.CharField(max_length=255)
    OrganisationName = models.CharField(max_length=255)
    PolicyNo = models.CharField(max_length=50)
    InsuredFullName = models.CharField(max_length=255)
    InsuredDOB = models.DateField()
    Plantype = models.CharField(max_length=50)
    DOC = models.DateField()
    MOP = models.CharField(max_length=50)
    Term = models.IntegerField()
    MaturityDate = models.DateField()
    InsuredAge = models.IntegerField()
    SecFullName = models.CharField(max_length=255)
    SecDOB = models.DateField()
    SecGender = models.CharField(max_length=10)
    SecAge = models.IntegerField()
    RiAge = models.IntegerField()
    BasicSumAssured = models.DecimalField(max_digits=10, decimal_places=2)
    ADBSA = models.DecimalField(max_digits=10, decimal_places=2)
    PTDSA = models.DecimalField(max_digits=10, decimal_places=2)
    PWBSA = models.DecimalField(max_digits=10, decimal_places=2)
    FESA = models.DecimalField(max_digits=10, decimal_places=2)
    dc_sumFE = models.DecimalField(max_digits=10, decimal_places=2)
    dc_adb = models.DecimalField(max_digits=10, decimal_places=2)
    dc_ptd = models.DecimalField(max_digits=10, decimal_places=2)
    dc_pwb = models.DecimalField(max_digits=10, decimal_places=2)
    ret_sumFE = models.DecimalField(max_digits=10, decimal_places=2)
    st_sumFE = models.DecimalField(max_digits=10, decimal_places=2)
    st_adb = models.DecimalField(max_digits=10, decimal_places=2)
    st_ptd = models.DecimalField(max_digits=10, decimal_places=2)
    st_pwb = models.DecimalField(max_digits=10, decimal_places=2)
    Rimaturity = models.DecimalField(max_digits=10, decimal_places=2)
    Remarks = models.TextField()

    class Meta:
        managed = False
        db_table = '[dbo].[reinsurance]'