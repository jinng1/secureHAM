from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


# Create your views here.

#authentication
def wrong_user(request):
    return render(request,"wrong_user.html")

@login_required(login_url='/auth/login/')
def dashboardRedirect(request):
    current_user = request.user
    if current_user.role == "S":
         return redirect('/staff/home/')
    elif current_user.role == "M":
        return redirect('/manager/home/')
    elif current_user.role == "A":
        return redirect('/it/home/')

@login_required(login_url='/auth/login/')
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/auth/login/")




#admin views
@login_required(login_url='/auth/login/')
def it_home(request):
    if not request.user.role == "A":
        return redirect("/wrong_user/")
    return render(request,'IT/item_management.html')

@login_required(login_url='/auth/login/')
def account_management(request):
    if not request.user.role == "A":
        return redirect("/wrong_user/")
    return redirect("/admin/")

@login_required(login_url='auth/login/')
def add_assets(request):
    if not request.user.role == "A":
        return redirect("/wrong_user/")
    return render(request,'IT/add_assets.html')



#staff views
@login_required(login_url='/auth/login/')
def staff_home(request):
    if not request.user.role == "S":
        return redirect("/wrong_user/")
    return render(request,'staff/asset_list.html')

@login_required(login_url='/auth/login/')
def requested_list(request):
    if not request.user.role == "S":
        return redirect("/wrong_user/")
    return render(request,'staff/requested_list.html')



#mananger views
@login_required(login_url='/auth/login/')
def manager_home(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    return render(request,'manager/request_management.html')

@login_required(login_url='/auth/login/')
def inventory_management(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    return render(request, 'manager/inventory_management.html')

@login_required(login_url='/auth/login/')
def inventory_list(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    return render(request, 'manager/inventory_list.html')

@login_required(login_url='/auth/login/')
def select(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    return render(request, 'manager/select_asset.html')

@login_required(login_url='/auth/login/')
def request_to(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    return render(request,'manager/request_to.html')

@login_required(login_url='/auth/login/')
def request_from(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    return render(request,'manager/request_from.html')

@login_required(login_url='/auth/login/')
def approve(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    return render(request,'manager/approve.html')

