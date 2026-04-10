from django.db import models
from django.contrib.auth.models import User

class ScanReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Change default=list to null=True so we can store "None" when skipped
    open_ports = models.JSONField(null=True, blank=True)
    headers_info = models.JSONField(null=True, blank=True)
    found_directories = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.target} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"