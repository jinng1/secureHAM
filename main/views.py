from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import addItemForm, managerItemForm
from .models import Items, CustomUser, Inventory, Requests
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

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
#admin display item list
@login_required(login_url='/auth/login/')
def it_home(request):
    if not request.user.role == "A":
        return redirect("/wrong_user/")

    items = Items.objects.all()
    context = {'items' : items}
    return render(request,'IT/item_management.html', context)

@login_required(login_url='/auth/login/')
def account_management(request):
    if not request.user.role == "A":
        return redirect("/wrong_user/")
    return redirect("/admin/")

#admin add item
@login_required(login_url='auth/login/')
def add_assets(request):
    if not request.user.role == "A":
        return redirect("/wrong_user/")

    form = addItemForm()
    if request.method == 'POST':
        form = addItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('it-home')
    
    context = {'form' : form}
    return render(request,'IT/add_assets.html', context)

#admin Update item
@login_required(login_url='auth/login/')
def update_assets(request, pk):
    if not request.user.role == "A":
        return redirect("/wrong_user/")
    
    item = Items.objects.get(id = pk)
    form = addItemForm(instance=item)

    if request.method == 'POST':
        form = addItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('it-home')

    context = {'form' : form}
    return render(request, 'IT/add_assets.html', context)

#admin Delete item
@login_required(login_url='auth/login/')
def delete_assets(request, pk):
    if not request.user.role == "A":
        return redirect("/wrong_user/")
    
    item = Items.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('it-home')
    return render(request, 'delete.html', {'obj' : item})

#admin views ends



#staff views
#staff Display hospital inventory list
@login_required(login_url='/auth/login/')
def staff_home(request):
    if not request.user.role == "S":
        return redirect("/wrong_user/")

    userHospID = request.user.hospital
    items = Inventory.objects.filter(hospital_id = userHospID)
    context = {'items' : items}
    return render(request,'staff/asset_list.html', context)

#staff Display REQUESTED hospital inventory list
@login_required(login_url='/auth/login/')
def requested_list(request):
    if not request.user.role == "S":
        return redirect("/wrong_user/")

    userHospID = request.user.hospital
    items = Inventory.objects.filter(hospital_id = userHospID).filter(status__in=["Submitted","Pending"])
    context = {'reqs' : items}
    return render(request,'staff/requested_list.html', context)

#staff Change inventory status to SUBMITTED
@login_required(login_url='/auth/login/')
def staff_request(request,pk):
    if not request.user.role == "S":
        return redirect("/wrong_user/")

    inv = Inventory.objects.get(id = pk)
    inv.status = "Submitted"
    inv.save(update_fields=['status'])
    return redirect('staff-home') 

#staff views ends



#mananger views
#mananger Display request management page
@login_required(login_url='/auth/login/')
def manager_home(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    return render(request,'manager/request_management.html')

#mananger Display inventory management page
@login_required(login_url='/auth/login/')
def inventory_management(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    return render(request, 'manager/inventory_management.html')

#mananger Display hospital inventory list
@login_required(login_url='/auth/login/')
def inventory_list(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    
    userHospID = request.user.hospital
    items = Inventory.objects.filter(hospital_id = userHospID)
    context = {'items' : items}
    return render(request, 'manager/inventory_list.html', context)

#mananger Update inventory item
@login_required(login_url='auth/login/')
def manager_update_assets(request, pk):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    
    item = Inventory.objects.get(id = pk)
    form = managerItemForm(instance=item)

    if request.method == 'POST':
        form = managerItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory-list')

    context = {'form' : form}
    return render(request, 'manager/manage_asset.html', context)

#mananger Delete inventory item
@login_required(login_url='auth/login/')
def manager_delete_assets(request, pk):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    
    item = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('inventory-list')
    return render(request, 'delete.html', {'obj' : item})

#mananger view inventory item that can be selected
@login_required(login_url='/auth/login/')
def select_list(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    
    userHospID = request.user.hospital
    inv = Inventory.objects.filter(hospital = userHospID).values_list('item_id')
    items = Items.objects.exclude(id__in = inv )
    context = {'items' : items}
    return render(request, 'manager/select_asset.html', context)

#mananger Select item from Global List
@login_required(login_url='/auth/login/')
def select(request,pk):
    if not request.user.role == "M":
        return redirect("/wrong_user/")
    
    userHospID = request.user.hospital
    item = Items.objects.get(id = pk)
    inv = Inventory(hospital = userHospID , item = item , quantity = 0, status = "None")
    inv.save()
    return redirect('select-list') 

#mananger Request that were made by staff
@login_required(login_url='/auth/login/')
def request_to(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")

    userHospID = request.user.hospital
    items = Inventory.objects.filter(hospital_id = userHospID).filter(status__in=["Submitted","Pending"])
    context = {'items' : items}
    return render(request,'manager/request_to.html', context)

#mananger Update the staff requested item status to PENDING and include in REQUEST TABLE
@login_required(login_url='/auth/login/')
def manager_update_request_to(request,pk):
    if not request.user.role == "M":
        return redirect("/wrong_user/")

    userHospID = request.user.hospital
    inv = Inventory.objects.get(id = pk)
    inv.status = "Pending"
    inv.save(update_fields=['status'])
    req = Requests(inventory= inv, requestBy = userHospID.id, requestAcceptedFrom = 0)
    req.save()

    return redirect('request-to')

#mananger Update the staff requested item status to NONE
@login_required(login_url='/auth/login/')
def manager_delete_request_to(request,pk):
    if not request.user.role == "M":
        return redirect("/wrong_user/")

    req = Inventory.objects.get(id = pk)
    req.status = "None"
    req.save(update_fields=['status'])
    return redirect('request-to')

#mananger Display Requested item from other hospital that has not been accepted
@login_required(login_url='/auth/login/')
def request_from_list(request):
    if not request.user.role == "M":
        return redirect("/wrong_user/")

    userHospID = request.user.hospital
    inv = Inventory.objects.filter(hospital_id = userHospID).values('item_id')
    req = Requests.objects.exclude(inventory_id = userHospID.id).filter(inventory_id__in = inv).filter(requestAcceptedFrom = 0)
    context = {'reqs' : req}
    return render(request,'manager/request_from.html', context)

#mananger Update the REQUEST TABLE field "requestedAcceptedFrom" with the hosp ID and the item inventory status to NONE
@login_required(login_url='/auth/login/')
def manager_request_from(request, pk):
    if not request.user.role == "M":
        return redirect("/wrong_user/")

    userHospID = request.user.hospital
    req = Requests.objects.get(id = pk)
    item = Items.objects.get(id = req.inventory_id)
    inv = Inventory.objects.filter(item_id = item).filter(hospital_id = req.inventory_id).get(item_id = item)
    inv.status = "None"
    inv.save(update_fields=['status'])
    req.requestAcceptedFrom = userHospID.id
    req.save(update_fields=['requestAcceptedFrom'])
    return redirect('request-from')

#mananger APPROVE request by other hospital
@login_required(login_url='/auth/login/')
def approve(request, pk):
    if not request.user.role == "M":
        return redirect("/wrong_user/")

    userHospID = request.user.hospital
    req = Requests.objects.get(id = pk)
    item = Items.objects.get(id = req.inventory_id)
    # inv = Inventory.objects.filter(item_id = item).filter(hospital_id = userHospID)
    inv = Inventory.objects.filter(item_id = item).filter(hospital_id = userHospID).get(item_id = item)
    context = {'reqs' : req, 'invs' : inv}
    return render(request,'manager/approve.html', context)

#mananger views Ends