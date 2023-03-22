from django.db import models
from datetime import datetime,timedelta
from django.db.models import Sum
import os,json
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
#Some utilis to get file name
def get_month_year_filename(instance,filename):
    months={1:"JAN",2:"FEB",3:"MAR",4:"APR",5:"MAY",6:"JUN"
           ,7:"JUL",8:"AUG",9:"SEP",10:"OCT",11:"NOV",12:"DEC"}
    month=months[datetime.now().month]
    return os.path.join()

# Create your models here.
class Customer(models.Model):
    customer_id=models.CharField(max_length=20,null=False)
    c_fname=models.CharField(max_length=20,null=False)
    c_lname=models.CharField(max_length=20,null=False)
    sex=models.CharField(max_length=10,null=True)
    phone=models.PositiveBigIntegerField(null=False)
    address=models.CharField(max_length=250,null=False)

    def get_full_name(self):
        return self.c_fname+" "+self.c_lname
    def active_coupons(self):
        total=self.purchases.all().aggregate(Sum('total_purchase'))['total_purchase__sum'] or 0
        availed=self.purchases.all().aggregate(Sum('availed_coupons'))['availed_coupons__sum'] or 0
        expired=self.purchases.all().aggregate(Sum('expired_coupons'))['expired_coupons__sum'] or 0
        used=availed+ expired
        if total==used:
            return 0
        else:
            return total-used
    def is_active(self):
        total=self.purchases.all().aggregate(Sum('total_purchase'))['total_purchase__sum'] or 0
        availed=self.purchases.all().aggregate(Sum('availed_coupons'))['availed_coupons__sum'] or 0
        expired=self.purchases.all().aggregate(Sum('expired_coupons'))['expired_coupons__sum'] or 0
        used=availed+ expired
        print(self.c_fname+" "+str(expired))
        if total==used:
            return "inactive"
        elif total-used<=15:
            return "low coupons"
        else:
            return "active"
    def get_map_url(self):
        return reverse('map-coupons',kwargs={'customerID':self.customer_id})
class Purchase(models.Model):
    
    purchase_id=models.CharField(max_length=10,unique=True,null=False)
    purchase_customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="purchases")
    dop=models.DateTimeField(default=datetime.now())
    total_purchase=models.BigIntegerField(default=0)
    availed_coupons=models.IntegerField(default=0)
    expired_coupons=models.IntegerField(default=0)
    coupons=models.JSONField()
    #Derive month from date of purchase so that we can add extra coupons
    #if customer wishes to buy some more coupons in same month

    def get_milk_total(self):
        milk=self.coupons['MILK']
        total_milk=len(milk)
        return total_milk
    def get_curd_total(self):
        curd=self.coupons['CURD']
        total_curd=len(curd)
        return total_curd
    def get_ton_total(self):
        tonned_milk=self.coupons['TONED MILK']
        total_ton=len(tonned_milk)
        return total_ton
    
    

class Sales(models.Model):
    date=models.DateField()
    total_coupons=models.PositiveIntegerField(default=0)
    milk_coupons=models.PositiveIntegerField(default=0)
    curd_coupons=models.PositiveIntegerField(default=0)
    ton_coupons=models.PositiveIntegerField(default=0)

    def get_weekday(self):
        week={1:"Mon",2:"Tue",3:"Wed"}

#signals for Deleting sales data before 12 days
@receiver(post_save,sender=Sales)
def delete_handler(sender, instance, created, **kwargs):
    to_delete=datetime.today().date()-timedelta(days=12)
    if created:
        try:
            sales=Sales.objects.get(date=to_delete)
            sales.delete()
        except Sales.DoesNotExist:
            pass
        
    #if not created:


class Supplier(models.Model):
    #These are just sample areas for test purpose, can be changed later
    areas=(('Ramamurthy Nagar','Ramamurthy Nagar'),
            ('Hormavu','Hormavu'),
            ('Banasawadi','Banaswadi'))
    s_fname=models.CharField(max_length=20,null=False)
    s_lname=models.CharField(max_length=20,null=False)
    phone=models.PositiveBigIntegerField(null=False)
    Adhaar_no=models.PositiveBigIntegerField(null=True)
    supply_area=models.CharField(choices=areas,max_length=20)



'''class milk_coupons(models.Model):
    #One to many field- i.e One milk supplier can deliver and collect 'n' coupons
    main_supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=False)
    coupon_id=models.CharField(unique=True,null=False)
    issue_date=models.DateTimeField(default=datetime.now())
    scan_timestamp=models.DateTimeField(null=True)
    is_checked=models.BooleanField(default=False)
    qr_code=models.ImageField
    #If providing different varities of milk uncomment below
    
    types=(('thick','thick'),
            ('medium','medium'),
            ('light','light'))
    MilkType=models.CharField(choices=types)

    
    ##If Required create customer Database seperate and add fields
    #Directly create One to Many field'''
