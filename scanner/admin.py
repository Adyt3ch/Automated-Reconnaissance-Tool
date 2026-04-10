from django.contrib import admin
from .models import ScanReport

@admin.register(ScanReport)
class ScanReportAdmin(admin.ModelAdmin):
    list_display = ('target', 'user', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('target',)