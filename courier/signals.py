from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Trip, IncomeIncrease, IncomeDeduction, DailySalary


@receiver(post_save, sender=Trip)
@receiver(post_save, sender=IncomeIncrease)
@receiver(post_save, sender=IncomeDeduction)
def update_daily_salary(sender, instance, **kwargs):

    DailySalary.update_total_salary(instance)
