from django.contrib import admin

# Register your models here.

# Register your models here.
from models import BacklogItem

class BacklogItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(BacklogItem, BacklogItemAdmin)
