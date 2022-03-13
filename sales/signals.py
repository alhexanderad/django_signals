from django.db.models.signals import pre_delete
from django.dispatch import receiver

from sales.models import Sale
from orders.models import Order

@receiver(pre_delete, sender=Sale)
def pre_delete_change_active_order(sender, instance, **kwargs):
  #order es el nombre de la tupla de la tabla Sales por estar en forekey
  obj = instance.order
  obj.active = False
  obj.save()