from django.db import models
from django.db.models import Sum

# Create your models here.

class NumerosGerados(models.Model):
    numeroGerado = models.IntegerField(verbose_name='numeroGerado',null=False, blank=False)
    dataCriacao = models.DateField(auto_now_add=True, null=False, blank=False)

    class Meta:
        ordering = ['dataCriacao']
