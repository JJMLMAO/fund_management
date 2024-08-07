from django.db import models


class Fund(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    investment_type = models.CharField(max_length=50, null=True)
    current_nav = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ytd_return = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    currency = models.CharField(max_length=50, null=True)
    risk_profile = models.CharField(max_length=50, null=True)
    shariah_compliant = models.CharField(max_length=50, null=True)
    
    
    def __str__(self):
        return self.name