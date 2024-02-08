from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms.bankStateForm import BankStateForm
from accounts.forms.phonePayReports import PhonePayReportsForm
from .models import BankState, PhonePayReports
from .middleware.permission import user_group_required, group_permission_required
from .serializers import *
import json
from django.http import HttpResponse
from django.core.files import File
import pandas as pd
import os
from django.conf import settings
from django.db.models import F,Sum
from app.admin import SiteConfiguration

# Create your views here.
class bankStateClass():
    queryset = BankState.objects.all()
    serializer_class = BankStateSerializer
    
    @login_required
    @user_group_required('account')
    @group_permission_required('account', ['accounts.view_bankstate'])
    def view_bankstate(request):
        total_sum_premium = 0
        # Retrieve operation
        data = BankState.objects.all()
        form = BankStateForm()
        SummaryData = BankState.objects.values('BankShortName').annotate(total_amount=Sum('Amount')) # .annotate(BankName=F('BankName'))
        def process_data(data):
            nonlocal total_sum_premium
            for todaypremium in data:
                total_sum_premium += todaypremium.Amount
        if data:
            process_data(data)
        return render(request, 'accounts/BankState.html', {'form': form, 'bankStateData': data, 'totalAmount': total_sum_premium,'SummaryData':SummaryData})
        
    @login_required
    @user_group_required('account')
    @group_permission_required('account', ['accounts.add_bankstate'])
    def create_bankstate(request):
            # Create operation
            if request.method == 'POST':
                form = BankStateForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'added successfully')
            return redirect('bankstate')
        

    @login_required
    @user_group_required('account')
    @group_permission_required('account', ['accounts.change_bankstate'])
    def edit_bankstate(request):
        # Update operation
        if request.method == 'POST':
            pk = request.POST.get('RowId')
            instance = get_object_or_404(BankState, pk=pk)
            form = BankStateForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('bankstate')    # Redirect to a success page or another page
        else:
            form = BankStateForm(instance=instance)
        return redirect('bankstate')


    @login_required
    @user_group_required('account')
    @group_permission_required('account', ['accounts.delete_bankstate'])
    def delete_bankstate(request, pk):
        # Delete operation
            instance = get_object_or_404(BankState, pk=pk)
            instance.delete()
            messages.success(request, 'Deleted successfully')
            return redirect('bankstate')# Redirect to a success page or another page

class PhonePayReportView:
    queryset = PhonePayReports.objects.all()
    serializer_class = PhonePayReportSerializer
    
    @login_required
    @user_group_required('account')
    def phonepay(request):
        Form = PhonePayReportsForm()
        if request.method == 'POST' and 'action' in request.POST and request.POST['action'] == 'export':
                form = PhonePayReportsForm(request.POST)
                if form.is_valid():
                    PaymentStatus = form.cleaned_data['Payment_statues']
                    PaymentType = form.cleaned_data['Payment_type']
                    startdate = form.cleaned_data['StartDate']
                    enddate = form.cleaned_data['EndDate']

                    # Assuming PhonePayReports.PhonePayReport returns a JSON string
                    data_json = PhonePayReports.PhonePayReport(PaymentType, startdate, enddate, PaymentStatus)
                    try:
                        # data_list = json.loads(data_json)
                        df = pd.DataFrame(data_json)

                        # Allow users to choose the directory
                        user_specified_directory = request.POST.get('directory', 'static')  # Default to 'static' if not provided
                        user_specified_filename = request.POST.get('filename', 'exported_data')  # Default to 'exported_data' if not provided
                        
                         # Create the directory if it doesn't exist
                        directory_path = os.path.join(settings.BASE_DIR, user_specified_directory)
                        os.makedirs(directory_path, exist_ok=True)
                        
                        excel_filename = os.path.join(settings.BASE_DIR, user_specified_directory, f'{user_specified_filename}.xlsx')

                        # Save the DataFrame to Excel file
                        df.to_excel(excel_filename, index=False, engine='openpyxl')

                        # Open the file and wrap it with Django File for sending as an attachment
                        with open(excel_filename, 'rb') as file:
                            django_file = File(file)
                            response = HttpResponse(django_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                            response['Content-Disposition'] = f'attachment; filename="{user_specified_filename}.xlsx"'

                        # Clean up - delete the temporary file
                        # os.remove(excel_filename)

                            return response

                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")
        else:        
                form = PhonePayReportsForm(request.POST)
                if form.is_valid():
                    PaymentStatus = form.cleaned_data['Payment_statues']
                    PaymentType = form.cleaned_data['Payment_type']
                    startdate = form.cleaned_data['StartDate']
                    enddate = form.cleaned_data['EndDate']
                    data = PhonePayReports.PhonePayReport(PaymentType,startdate,enddate,PaymentStatus)
                    if data:
                        return render(request,'accounts/PhonePay.html', {'Form': Form, 'data':data })
                    else:
                        return render(request,'staticPages/disconnectionPage.html')
    
        return render(request,'accounts/PhonePay.html', {'Form': Form})
    

class BankBalanceView:
    queryset = BankBalanceReports.objects.all()
    serializer_class = BankBalanceSerializer
    
    @login_required
    @user_group_required('admin')
    def BankBalanceStatements(request):
        Amount = 0
        TenderAmount = 0
        data = BankBalanceReports.BankBalance()
        def process_data(data):
            nonlocal Amount, TenderAmount
            for todaypremium in data:
                Amount += todaypremium['Amount']
                TenderAmount += todaypremium['TenderAmount']
        if data:
            process_data(data)
        else:
            return render(request,'staticPages/disconnectionPage.html')
        
        return render(request,'accounts/BankBalance.html',{'data': data,'TotalAmount': Amount,'TenderAmount':TenderAmount} )
    
    @login_required
    def fileUpload(request):
        if request.method == 'POST':
            value = request.POST.get('my_field')
            print(value)
        a = 'this is acount sections'
        return render(request, 'fileUploads/fileUploads.html', {'name':a})