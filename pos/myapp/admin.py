from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(item)
admin.site.register(invoice)
admin.site.register(invitem)
admin.site.register(invoice_heading)