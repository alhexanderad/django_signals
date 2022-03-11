from math import fabs
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Buyer(models.Model):
  user = models.OneToOneField(User, verbose_name=_("Usuario"), on_delete=models.CASCADE)
  from_signal = models.BooleanField(_("Signo"), default=False)
  
  def __str__(self):
    return str(self.user)