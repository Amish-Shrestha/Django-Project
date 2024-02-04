from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from accounts.middleware.permission import user_group_required, group_permission_required
from django.contrib.auth.models import User
from .forms.premiumForm import PremiumForm
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
    
    def PremimumView(request):
        Form = PremiumForm()
        return render(request,'required/premium.html',{'Form': Form})
        

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

