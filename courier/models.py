from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Courier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Trip(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    income = models.IntegerField(validators=[MinValueValidator(0)])  # TODO: BigintegerField
    # TODO: Add other fields for trip parameters like distance, type of customer, time of day, etc.

    def __str__(self):
        return f"Trip for {self.courier.name} - Income: {self.income}"


class IncomeIncrease(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    income = models.IntegerField(validators=[MinValueValidator(0)])  # TODO: BigintegerField
    reason = models.TextField()

    def __str__(self):
        return f"Income increase for {self.courier.name} - Amount: {self.increase_amount} - Reason: {self.reason}"


class IncomeDeduction(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    income = models.IntegerField(validators=[MaxValueValidator(0)])  # TODO: BigintegerField
    reason = models.TextField()

    def __str__(self):
        return f"Income deduction for {self.courier.name} - Amount: {self.deduction_amount} - Reason: {self.reason}"


class DailySalary(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    date = models.DateField()
    total_salary = models.IntegerField(default=0)  # TODO: BigintegerField
    date_updated = models.DateTimeField(auto_now_add=True)

    @classmethod
    def update_total_salary(cls, instance):
        total_salary, created = cls.objects.get_or_create(
            courier=instance.courier, date=instance.date_created.date()
        )
        total_salary.total_salary += instance.income
        total_salary.save()
