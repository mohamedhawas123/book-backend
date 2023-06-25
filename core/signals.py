from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.models import Page
from django.db import models

@receiver(pre_save, sender=Page)
def auto_increment_page_number(sender, instance, **kwargs):
    if not instance.number:
        max_page_number = Page.objects.filter(book=instance.book).aggregate(number__max=models.Max('number'))['number__max']
        instance.number = str(int(max_page_number) + 1) if max_page_number is not None else '1'