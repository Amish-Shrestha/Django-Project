from django.db import models,connections
from app.admin import SiteConfiguration
from datetime import date
# Create your models here.
class BankState(models.Model):
    RowId = models.AutoField(primary_key=True)
    BankName = models.CharField(max_length=255)
    BankShortName = models.CharField(max_length=50)
    LedgerNo = models.CharField(max_length=20, unique=True, null=True, default='')
    Amount = models.DecimalField(max_digits=15, decimal_places=2)
    LatestDate = models.DateField(default=date.today)
    EditDate = models.DateField(default=date.today)  # auto_now_add=True
    
    
class PhonePayReports(models.Model):
    # RowId = models.AutoField(primary_key=True)  # Add the appropriate type and properties for RowId
    # PolicyNo = models.CharField(max_length=255)
    class Meta:
        # Specify the database for this model
        # app_label = 'accounts'  # Replace 'your_app_name' with the actual name of your app
        managed = False  # Set managed to False to prevent Django from managing the table
    
    def PhonePayReport(Payment_type,startdate,enddate,PaymentStatus):
        site_config = SiteConfiguration.objects.first()
        if site_config.enable_feature == True:
            with connections['TestDb'].cursor() as cursor:
                esewa_query = """
                select Distinct
                    a.LedgerNo,
                    b.PolicyNo,
                    a.VoucherNo,
                    b.Remarks, 
                    c.ProductCode as ProductId,
                    e.pid as pid,
                    b.Premium, 
                    b.PaidAmount, 
                    a.TransactionDate, 
                    CAST(a.TransactionDate AS DATE) as [TransactionDate In AD],
                    e.Status
                    from Account.LITBL_TodaysTransaction a
                    INNER JOIN Policy.LITBL_PremiumPaymentSchedule b ON a.SubLedgerNo = b.PolicyNo
                    INNER JOIN Policy.LITBL_Policy c ON c.PolicyNo = b.PolicyNo
                    INNER JOIN Payment.LITBL_EsewaWebPayment e ON e.ProposalId = c.ProposalId 
                    where (LedgerNo = %s AND a.TransactionDate BETWEEN %s and %s and e.Status = %s)
                """
                phonepay_query = """
                select Distinct
                    a.LedgerNo,
                    b.PolicyNo,
                    a.VoucherNo,
                    b.Remarks, 
                    c.ProductCode as ProductId,
                    e.prn as pid,
                    b.Premium, 
                    b.PaidAmount, 
                    a.TransactionDate, 
                    CAST(a.TransactionDate AS DATE) as [TransactionDate In AD],
                    e.Status
                    from Account.LITBL_TodaysTransaction a
                    INNER JOIN Policy.LITBL_PremiumPaymentSchedule b ON a.SubLedgerNo = b.PolicyNo
                    INNER JOIN Policy.LITBL_Policy c ON c.PolicyNo = b.PolicyNo
                    INNER JOIN Payment.LITBL_FonePayDirect e ON e.ProposalId = c.ProposalId 
                    where (LedgerNo = %s AND a.TransactionDate BETWEEN %s and %s and e.Status = %s)
                """
                # Execute the query
                if Payment_type == '200034':
                    cursor.execute(esewa_query, [Payment_type,startdate,enddate,PaymentStatus])
                elif Payment_type == '200035':
                    cursor.execute(phonepay_query, [Payment_type,startdate,enddate,PaymentStatus])
                # Fetch the data
                columns = [col[0] for col in cursor.description]
                data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                # print(data)
            return data
        else: 
            return None

class BankBalanceReports(models.Model):
    # LedgerNo = models.CharField(max_length=255)
    # SubLedgerNo = models.CharField(max_length=255)
    # LGCode = models.CharField(max_length=255)
    # TransactionDate = models.DateField()
    # Narration = models.CharField(max_length=255)
    # Amount = models.DecimalField()
    # TenderAmount = models.DecimalField()
    # VoucherNo = models.CharField(max_length=255)
    class meta:
        # db_table = '[Account].[LITBL_TodaysTransaction]'
        managed = False # Set managed to False to prevent Django from managing the table
    
    def BankBalance():
        site_config = SiteConfiguration.objects.first()
        if site_config.enable_feature == True:
            with connections['TestDb'].cursor() as cursor:
                query = """
                select LedgerNo,SubLedgerNo,LGCode,TransactionDate,Narration,Amount,TenderAmount,VoucherNo 
                from Account.LITBL_TodaysTransaction where LGCode = '120'
                """
                cursor.execute(query)
                columns = [col[0] for col in cursor.description]
                data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
            return data
        else: 
            return None