from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Элемент")
        verbose_name_plural = _("Элементы")
        ordering = ["id"]

    def __str__(self):
        return self.name
