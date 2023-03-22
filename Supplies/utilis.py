from .models import Purchase,Sales,Customer
from datetime import datetime,timedelta
from django.db.models import Count
from itertools import chain
import re

def get_customer_id():
    currLast_purchase=Customer.objects.all().last()
    #Genrates a Unique customer ID with current PK 
    if currLast_purchase is None:
        id=1
    else:
        id=currLast_purchase.pk+1
    id=10000+id
    currLast_purchase_id="CM"+str(id)
    return currLast_purchase_id

def get_coupon_type(coupon_id):
    regex = r"^(MLK|CRD|TON)[0-9]+"
    if(re.search(regex,coupon_id)):
        if "MLK" in coupon_id:
            type="MILK"
        elif "CRD" in coupon_id:
            type="CURD"
        elif "TON" in coupon_id:
            type="TONED MILK"
        else:
            type=None
    else:
        type=None
    return type


def get_purchase(coupon_id,coupon_type):
    if coupon_type=="MILK":
        try:
            purchase=Purchase.objects.get(coupons__MILK__contains=[{"coupon_id":coupon_id}])
        except Purchase.DoesNotExist:
            purchase=None
    elif coupon_type=="CURD":
        try:
            purchase=Purchase.objects.get(coupons__CURD__contains=[{"coupon_id":coupon_id}])
        except Purchase.DoesNotExist:
            purchase=None
    elif coupon_type=="TONED MILK":
        try:
            purchase=Purchase.objects.get(**{"coupons__TONED MILK__contains":[{"coupon_id":coupon_id}]})
        except Purchase.DoesNotExist:
            purchase=None
    else:
        purchase="INVALID"
    return purchase

def get_total():
    purchases=Purchase.objects
    milk=purchases.values_list('coupons__MILK')
    total_milk,total_curd,total_ton=0,0,0
    curd=purchases.values_list('coupons__CURD')
    tonned_milk=purchases.values_list('coupons__TONED MILK')
    for all_milk in milk:
        total_milk+=len(all_milk[0])
    for all_curd in curd:
        total_curd+=len(all_curd[0])
    for all_ton in tonned_milk:
        total_ton+=len(all_ton[0])
    all=[total_milk,total_curd,total_ton]
    total=sum(all)
    try:
        all=[round(i/total,1)*100 for i in all]
    except ZeroDivisionError:
        all=[0,0,0]
    return [all,total]


def update_sales(coupon_type):
    sales,created=Sales.objects.get_or_create(date=datetime.today().date())
    sales.total_coupons+=1
    if coupon_type=="MILK":
        sales.milk_coupons+=1
    elif coupon_type=="CURD":
        sales.curd_coupons+=1
    elif coupon_type=="TONED MILK":
        sales.ton_coupons+=1
    sales.save()
        