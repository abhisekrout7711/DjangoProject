from django.contrib import admin
from MobileStore.models import MobilePhone, EarPhone, SaveBill, Discount


# Register your models here.
admin.site.register(MobilePhone)
admin.site.register(EarPhone)
admin.site.register(SaveBill)
admin.site.register(Discount)