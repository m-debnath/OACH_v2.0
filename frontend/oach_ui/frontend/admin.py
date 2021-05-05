from django.contrib import admin
from .models import EnvironmentData, LdapConfig, Department, AppUser, Transaction, TransactionParameter
from .forms import LdapConfigForm

class LdapConfigAdmin(admin.ModelAdmin):
    form = LdapConfigForm

admin.site.site_header = 'OACH v2.0 Frontend Administration'
admin.site.register(EnvironmentData)
admin.site.register(LdapConfig, LdapConfigAdmin)
admin.site.register(Department)
admin.site.register(AppUser)
admin.site.register(Transaction)
admin.site.register(TransactionParameter)