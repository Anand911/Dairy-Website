from django.urls import path
from . import views

#from .utilis import update_symptoms

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers', views.customers, name='customers'),
    path('Addcustomers', views.add_customers, name='add-customers'),
    path('Updatecustomers', views.UpdateCustomer, name='update-customers'),
    path('DeleteCustomer/<str:c_id>', views.DeleteCustomer, name='delete-customers'),
    path('mapcoupons', views.mapcoupons, name='mapcoupons'),
    path('createCustomer',views.CreateCustomer,name="CreateCustomer"),
    path('mapcoupons/<str:customerID>',views.MapCouponsCustomers,name="map-coupons"),
    path('validateCoupons',views.ValidateCoupons,name="validate-coupons")
]  