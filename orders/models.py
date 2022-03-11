from django.db import models
from cars.models import Car
from django.utils.translation import gettext as _

class Order(models.Model):
  name = models.CharField(_("Nombre"), max_length=200)
  cars = models.ManyToManyField(Car, verbose_name=_("Carros"))
  total = models.PositiveIntegerField(_("Total"), blank=True, null=True)
  total_price = models.PositiveIntegerField(_("Precio Total"), blank=True, null=True)
  active = models.BooleanField(_("Actividad"), default=True)
  
  def __str__(self):
    return str(self.name)
