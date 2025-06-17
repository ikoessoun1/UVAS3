from django.contrib import admin

# Register your models here.
from simple_history.admin import SimpleHistoryAdmin
from .models import Vendor, Contract, Contact, Document # adjust as needed

admin.site.register(Vendor, SimpleHistoryAdmin)
admin.site.register(Contract, SimpleHistoryAdmin)
admin.site.register(Contact, SimpleHistoryAdmin)
admin.site.register(Document, SimpleHistoryAdmin)
