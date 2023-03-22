from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib import messages
import json
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from django.db.models import Q 
from datetime import date


#Decorators for Login
from django.contrib.auth.decorators import login_required

#Internal Imports
from .models import Customer,Purchase,Sales
from .forms import CustomerForm,CustomerUpdateForm
from .utilis import get_customer_id,get_coupon_type,get_purchase,get_total,update_sales

@login_required
def dashboard(request):
    categories,total_coupons,milk_coupons,curd_coupons,ton_coupons=[],[],[],[],[]
    sales=Sales.objects.all()[:12]
    for sale in sales:
        categories.append(str(sale.date.isoformat()))
        total_coupons.append(sale.total_coupons)
        milk_coupons.append(sale.milk_coupons)
        curd_coupons.append(sale.curd_coupons)
        ton_coupons.append(sale.ton_coupons)
    chart_weekly=[categories,total_coupons,milk_coupons,curd_coupons,ton_coupons]
    recent_purchases=Purchase.objects.all().order_by('-dop')
    total_orders=recent_purchases.count()
    total_customers=Customer.objects.all().count()
    context={"total_data":get_total(),"purchases":recent_purchases[:10],"total_customers":total_customers,"total_purchases":total_orders,"chart_weekly":json.dumps(chart_weekly)}
    return render(request,'index.html',context)

@login_required
def customers(request):
    customers=Customer.objects.all()
    customerData=[{"id":customer.customer_id,"user":{"name":customer.get_full_name()},"email":"","phone":str(customer.phone),"address":customer.address,"sex":customer.sex,"label":customer.is_active(),"tab":""} for customer in customers]
    #recent_purchases=Purchase.objects.all().order_by('-dop')
    #recentCustomers=[{"id":purchase.purchase_customer.customer_id,"user":{"name":purchase.purchase_customer.get_full_name()},"email":"","phone":str(purchase.purchase_customer.phone),"address":purchase.purchase_customer.address,"label":purchase.purchase_customer.is_active(),"tab":"frequently"} for purchase in recent_purchases[:4]]
    currLast_purchase_id=get_customer_id()
    context={'cust_json':json.dumps(customerData),'curr_cust_id':currLast_purchase_id}
    return render(request,'customers.html',context)


def add_customers(request):
    context={'curr_cust_id':get_customer_id()}
    return render(request,'addCustomers.html',context)

@login_required
def mapcoupons(request):
    customers=Customer.objects.all()
    customerData=[{"id":customer.customer_id,"user":{"name":customer.get_full_name()},"email":"","phone":str(customer.phone),"address":customer.address,"label":customer.is_active(),"tab":""} for customer in customers]
    context={'cust_json':json.dumps(customerData)}
    return render(request,'mapcoupons.html',context)



def home(request):
    #TESTING- To create global mapped coupons
    
    '''c=MappedCoupons.objects.get(pk=1)
    c.all_coupons["TONED MILK"]=[]
    c.save()'''
    currLast_purchase=Customer.objects.all().last()
    #Genrates a Unique customer ID with current PK 
    if currLast_purchase is None:
        id=1
    else:
        id=currLast_purchase.pk+1
    id=10000+id
    currLast_purchase_id="CM"+str(id)
    #Initial Data for Customer ID/// Input Set as ReadOnly
    initial_Data={'customer_id':currLast_purchase_id}
    c_form=CustomerForm(initial=initial_Data)

    #Customer JSON
    customers=Customer.objects.all()
    cust_list=[{"customer_id":customer.customer_id,"c_name":customer.get_full_name()} for customer in customers]
    c_json=json.dumps(cust_list)
    context={'CustomerForm':c_form,'c_json':c_json,'customers':customers}
    return render(request,'temp.html',context)

#######################################################
# Functionalties Begin Here



@login_required
def CreateCustomer(request):
    if request.POST:
        c_form=CustomerForm(request.POST)
        if c_form.is_valid():
            Customer=c_form.save()
    return redirect("customers")

@login_required
def UpdateCustomer(request):
    
    if request.POST:
        customer=Customer.objects.get(customer_id=request.POST["customer_id"])
        cname=customer.get_full_name()
        c_form=CustomerUpdateForm(request.POST,instance=customer)
        if c_form.is_valid():
            customer=c_form.save()
            messages.success(request,f"Updated customer {cname} successfully!")
    return redirect("customers")

@login_required
def DeleteCustomer(request,c_id):
    customer=Customer.objects.get(customer_id=c_id)
    cname=customer.get_full_name()
    if customer.is_active()=="inactive":
        customer.delete()
        messages.success(request,f"Deleted customer {cname} successfully!")
    else:
        messages.error(request,f"Cannot Delete! The customer has active coupons.")
    return redirect("customers")

@login_required
def MapCouponsCustomers(request,customerID):
    try:
        customer=Customer.objects.get(customer_id=customerID)
    except Customer.DoesNotExist:
        raise Http404("Customer Doesn't Exist")
    if request.POST:
        coupon_id=request.POST["coupon_id"]
        coupon_type=get_coupon_type(coupon_id)
        if not coupon_type:
            messages.error(request,f"Cannot Map Invalid coupon ID")
            return redirect(customer.get_map_url())
        
        purchase=get_purchase(coupon_id,coupon_type)
        #checking to avoid Redundant Coupons
        if purchase:
            messages.error(request,f"Coupon already exists!")
        else:
            currLast_purchase=Purchase.objects.all().last()
            #Genrates a Unique purchase ID with current PK 
            if currLast_purchase is None:
                id=1
            else:
                id=currLast_purchase.pk+1
            id=10000+id
            currLast_purchase_id="PUR"+str(id)
            #customer=Customer.objects.get(pk=2) # testing

            today=date.today()
            try:
                purchase=Purchase.objects.get(purchase_customer=customer,dop__month=today.month,dop__year=today.year)
            except Purchase.DoesNotExist:
                purchase=Purchase(purchase_id=currLast_purchase_id,purchase_customer=customer,coupons={"MILK":[],"CURD":[],"TONED MILK":[]})

            purchase.total_purchase+1
            expiry_date=today+relativedelta(months=+3)
            customer_coupons=purchase.coupons
            customer_coupons[coupon_type].append({"coupon_id":coupon_id,"is_availed":False,"expiry":str(expiry_date),"is_expired":False})
            #purchase.coupons=customer_coupons
            purchase.total_purchase+=1
            purchase.save()
            messages.success(request,f'coupons added Successfully!')
            #add coupons to mapped coupons
            ''' all_coupons.append(coupon_id)
            replace_coupons=global_coupons.all_coupons
            replace_coupons[coupon_type]=all_coupons
            global_coupons.all_coupons=replace_coupons
            global_coupons.save()'''
    else:
        return render(request,'scan-coupons.html',{'customer':customer})
    return redirect(customer.get_map_url())



@login_required
def ValidateCoupons(request):
    if request.POST:
        coupon_id=request.POST["coupon_id"]
        coupon_type=get_coupon_type(coupon_id)
        if not coupon_type:
            messages.error(request,f"Invalid Coupon ID")
            return redirect("validate-coupons")
        purchase=get_purchase(coupon_id,coupon_type)
        if not purchase:
            messages.error(request,f"Coupon Does Not exist")
        else:
            coupons=purchase.coupons
            this_coupon=next(filter(lambda d: d.get("coupon_id") == coupon_id, coupons[coupon_type]), None)
            #coupons[coupon_type].remove(this_coupon)

            #check for expiry date
            if this_coupon["is_expired"]==True:
                messages.error(request,f"Coupon is Expired!")
            elif datetime.today()>=datetime.strptime(this_coupon["expiry"], "%Y-%m-%d"):
                if this_coupon["is_availed"]==True:
                    messages.error(request,f"It seems the Coupon is Expired and Duplicated!")
                else:
                    messages.error(request,f"Coupon is Expired!")
                    purchase.expired_coupons+=1
                    this_coupon["is_expired"]=True
                    purchase.save()
            elif this_coupon["is_availed"]!=True:
                this_coupon["is_availed"]=True
                #coupons[coupon_type].append(this_coupon)
                #purchase.coupons=coupons
                purchase.availed_coupons+=1
                purchase.save()
                update_sales(coupon_type)
                messages.success(request,f"Coupon Validated Successfully!")
            else:
                messages.error(request,f"Coupon already Validated!")
            
    else:
        return render(request,'validate-coupons.html')
    return redirect("validate-coupons")


