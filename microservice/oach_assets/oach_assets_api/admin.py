from django.contrib import admin
from .models import Transaction, TransactionParameter

admin.site.site_header = 'OACH Assets API administration'
admin.site.register(Transaction)
admin.site.register(TransactionParameter)
