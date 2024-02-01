from django.shortcuts import render
from django.http import HttpResponse
from .models import MicroInsuranceReports
from .forms.form import BatchIdForm
import json
from django.http import HttpResponse
from django.core.files import File
import pandas as pd
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from accounts.middleware.permission import user_group_required, group_permission_required


# Create your views here.
@login_required
@user_group_required('underwritting')
def MicroInsurance(request):
    Form = BatchIdForm()
    if request.method == 'POST' and 'action' in request.POST and request.POST['action'] == 'export':
            form = BatchIdForm(request.POST)
            if form.is_valid():
                BatchId = form.cleaned_data['BatchId']
                
                # Assuming PhonePayReports.PhonePayReport returns a JSON string
                data_json = MicroInsuranceReports.MicroInsuranceReport(BatchId)
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
                form = BatchIdForm(request.POST)
                if form.is_valid():
                    BatchId = form.cleaned_data['BatchId']
                    data = MicroInsuranceReports.MicroInsuranceReport(BatchId)
                    print(data)
                    if all(len(element) > 0 for element in data):
                        return render(request,'underwritting/MicroInsurance.html', {'Form': Form,'data':data })
                    else:
                        return render(request,'staticPages/disconnectionPage.html')
                     
    return render(request,'underwritting/MicroInsurance.html',{'Form':Form})
    