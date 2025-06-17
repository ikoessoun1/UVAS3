from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Vendor, Service, Contact, Contract, Document
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Vendor, SimpleHistoryAdmin)
admin.site.register(Contract, SimpleHistoryAdmin)
admin.site.register(Contact, SimpleHistoryAdmin)
admin.site.register(Document, SimpleHistoryAdmin)
admin.site.register(Service, SimpleHistoryAdmin)
