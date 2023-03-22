from django.contrib import admin
from .models import Customer,Purchase,Sales
# Register your models here.

class CustomerDisplay(admin.ModelAdmin):
    list_display=['customer_id','c_fname']
admin.site.register(Customer,CustomerDisplay)
admin.site.register(Purchase)
admin.site.register(Sales)
