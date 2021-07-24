from django.contrib import admin
from .models import Stock, Information

class StockAdmin(admin.ModelAdmin):
    search_fields = ['name']

class InformationAdmin(admin.ModelAdmin):
    search_fields = ['stock']

admin.site.register(Stock, StockAdmin)
admin.site.register(Information, InformationAdmin)