from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Field(models.Model):
    STAGE_CHOICES = [
        ('PLANTED','Planted'),
        ('GROWING','Growing'),
        ('READY','Ready'),
        ('HARVESTED','Harvested'),

    ]

    name = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=50)
    planting_date = models.DateField()
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_fields')
    # season = models.ForeignKey('Season', on_delete=models.CASCADE)

    @property
    def current_stage(self):
        log = self.logs.first()
        return log.growth_stage if log else 'PLANTED'

    
    

    @property
    def status(self):
        latest = self.logs.first()
        if not latest:
            return 'AT_RISK'

        if latest.growth_stage == 'HARVESTED':
            return 'COMPLETED'

        days_since = (timezone.now().date() - latest.date).days
        return 'AT_RISK' if days_since > 14 else 'ACTIVE'    


class CropLog(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField(default=timezone.now)
    growth_stage = models.CharField(max_length=20, choices=Field.STAGE_CHOICES)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-date']

        
        
    
    
    
    
    


# Create your models here.
