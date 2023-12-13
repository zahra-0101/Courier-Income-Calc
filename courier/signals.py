from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (
    Trip,
    IncomeIncrease,
    IncomeDeduction,
    DailySalary,
    WeeklySalary,
)

from django.db import transaction
from django.db.transaction import on_commit


@receiver(post_save, sender=Trip)
@receiver(post_save, sender=IncomeIncrease)
@receiver(post_save, sender=IncomeDeduction)
def update_salary(sender, instance, created, **kwargs):
    if created:
        try:
            with transaction.atomic():
                DailySalary.update_total_salary(instance)
                WeeklySalary.update_weekly_salary(instance)
        except Exception as e:
            on_commit(lambda: instance.__class__.delete_instance(instance, str(e)))
