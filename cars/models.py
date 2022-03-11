from django.db import models
from django.utils.translation import gettext as _
from buyers.models import Buyer
import uuid
class Car(models.Model):
  name = models.CharField(_("Nombres"), max_length=200)
  price= models.PositiveIntegerField(_("Precio"))
  buyer = models.ForeignKey(Buyer, verbose_name=_("Comprador"), on_delete=models.CASCADE)
  code = models.CharField(_("codigo"), max_length=10, blank=True)
  
  def __str__(self):
    return f"{self.name}-{self.price}-{self.buyer}"
  
  def save(self, *args, **kwargs):
    if self.code == "":
      self.code = str(uuid.uuid4()).replace("-","").upper()[:10]
    return super().save(*args, **kwargs)