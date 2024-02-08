from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime, timedelta
from accounts.middleware.permission import user_group_required, group_permission_required
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
@user_group_required('claim')
def claimsReportView(request):
    # two_years_ago = datetime.now() - timedelta(days=365*2 )
    # data = claimsReports.objects.filter(MaturityDate__range=[two_years_ago, datetime.now()])
    data = claimsReports.objects.all()
    # print(str(data.query))
    return render(request, 'claim/claimReInsurance.html', {'ReinsuranceData':data})