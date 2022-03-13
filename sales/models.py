from pyexpat import model
from django.db import models
from orders.models import Order
from django.utils.translation import gettext as _
class Sale(models.Model):
  order = models.ForeignKey(Order, verbose_name=_("Ordenes"), on_delete=models.CASCADE)
  amount =  models.PositiveIntegerField(("Monto"), blank=True, null=True )
  
  def __str__(self):
    return str(self.amount)
