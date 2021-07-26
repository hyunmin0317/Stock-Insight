from django.contrib import admin
from .models import Stock, Information, Date

class StockAdmin(admin.ModelAdmin):
    search_fields = ['name']

class InformationAdmin(admin.ModelAdmin):
    search_fields = ['stock.name']

class DateAdmin(admin.ModelAdmin):
    search_fields = ['date']

admin.site.register(Stock, StockAdmin)
admin.site.register(Information, InformationAdmin)
admin.site.register(Date, DateAdmin)