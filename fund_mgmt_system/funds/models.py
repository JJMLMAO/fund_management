from django.db import models


class Fund(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    investment_type = models.CharField(max_length=50)
    current_nav = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name