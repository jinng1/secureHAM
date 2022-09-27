from django.urls import path

from . import views

urlpatterns = [
    #authentication
    path('', views.dashboardRedirect, name='dashboardRedirect'),
    path("logout/", views.logout_request, name= "logout-request"),
    path("wrong_user/",views.wrong_user,name='wrong_user'),

    #IT paths
    path('it/home/', views.it_home, name='it-home'),
    path("it/accounts/",views.account_management, name = "account-management"),
    path('it/add_assets/', views.add_assets, name='add-assets'),

    #staff paths
    path('staff/home/', views.staff_home, name='staff-home'),
    path('staff/requested_list/',views.requested_list, name = 'requested-list'),

    #manager paths
    path('manager/home/', views.manager_home, name='manager-home'),
    path('manager/request_to/', views.request_to, name='request-to'),
    path('manager/request_from/', views.request_from, name='request-from'),
    path('manager/request_from/approve/', views.approve, name='approve'),
    path('manager/inventory_management', views.inventory_management, name='inventory-management'),
    path('manager/inventory_list', views.inventory_list, name='inventory-list'),
    path('manager/select', views.select, name='select'),
]