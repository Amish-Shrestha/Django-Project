from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, get_object_or_404
from accounts.middleware.permission import user_group_required, group_permission_required
from django.contrib.auth.models import User
from .forms.premiumForm import PremiumForm
from .models import PremiumModel
# Create your views here.

@login_required
def dashboard(request):
    request.session.cycle_key()
    return render(request, 'dashboard/dashboard.html')

@login_required
@user_group_required('admin') 
# @user_group_required('superuser')
def users(request):
    request.session.cycle_key()
    users = User.objects.all()
    return render(request, 'users/users.html',{'users': users})

def logout_view(request):
    logout(request)
    # Clear the session cookie immediately
    response = redirect('login')  # Redirect to your login page
    response.delete_cookie('sessionid')
    return response


class PremiumData:
    @login_required
    @user_group_required('admin') 
    def PremimumView(request):
        data = PremiumModel.objects.all()
        Form = PremiumForm()
        total_sum_premium = 0
        def process_data(data):
            nonlocal total_sum_premium
            for todaypremium in data:
                total_sum_premium += todaypremium.TotalPremium
        if data:
            process_data(data)
        return render(request,'required/premium.html',{'Form': Form, 'data':data, 'totalAmount': total_sum_premium})
    
    @login_required
    @user_group_required('admin') 
    def CrestPremium(request):
        if request.method == 'POST':
            form = PremiumForm(request.POST)
            if form.is_valid:
                form.save()
        return redirect('premium')
    
    @login_required
    @user_group_required('admin') 
    def EditPremium(request):
        if request.method == 'POST':
            pk = request.POST.get('RowId')
            instance = get_object_or_404(PremiumModel, pk=pk)
            form = PremiumForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('premium')    # Redirect to a success page or another page
        else:
            form = PremiumForm(instance=instance)
        return redirect('premium')

    @login_required
    @user_group_required('admin') 
    def DeletePremium(request, pk):
        # Delete operation
            instance = get_object_or_404(PremiumModel, pk=pk)
            instance.delete()
            # messages.success(request, 'Deleted successfully')
            return redirect('premium')# Redirect to a success page or another page

# @login_required
# def refresh_session(request):
#     # Save the old session key for comparison
#     old_session_key = request.session.session_key

#     # This line will refresh the session key
#     request.session.cycle_key()

#     # Get the new session key
#     new_session_key = request.session.session_key

#     # Print or log the session keys for comparison
#     print(f"Old Session Key: {old_session_key}")
#     print(f"New Session Key: {new_session_key}")

#     return HttpResponse("Session Refreshed!")

