from django.db import models
from base.models import BaseModel
from info.models import Markaz

class Donation(BaseModel):
    name = models.CharField(max_length=500, null=True)
    date = models.DateField(null=True)
    amount = models.IntegerField(null=True)
    markaz = models.ForeignKey(Markaz, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = "donation"

    def __str__(self):
        return self.name
