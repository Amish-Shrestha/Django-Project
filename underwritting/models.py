from django.db import models
from app.admin import SiteConfiguration
# Create your models here.
from django.db import models,connections

# Create your models here.
class MicroInsuranceReports(models.Model):
    class Meta:
        # Specify the database for this model
        # app_label = 'accounts'  # Replace 'your_app_name' with the actual name of your app
        managed = False  # Set managed to False to prevent Django from managing the table
    def MicroInsuranceReport(BatchId):
        site_config = SiteConfiguration.objects.first()
        if site_config.enable_feature == True:
            with connections['TestDb'].cursor() as cursor:
                try: 
                    query = """
                        select PolicyIssueNo as PolicyNumber,InsuredName as AssuredName,LoanCode,Premium,BatchId from MicroInsurance.LITBL_MicroPolicy
                        where BatchId = %s
                        """
                    cursor.execute(query, [BatchId,])
                    columns = [col[0] for col in cursor.description]
                    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                except Exception as e:
                    print(f"Error executing the query: {e}")
                    return e
                finally:
                    cursor.close()
                
            return data
        else:
            return []