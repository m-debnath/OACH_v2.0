from django.contrib import admin
from .models import Account, Activity, ServiceRequest, Invoice, Payment, Treatment

admin.site.site_header = 'Singl.eView Backend administration'
admin.site.register(Account)
admin.site.register(Activity)
admin.site.register(ServiceRequest)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(Treatment)
