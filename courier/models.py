from django.db import models
from django.core.validators import MinValueValidator


class Courier(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Trip(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    income = models.IntegerField(validators=[MinValueValidator(0)])
    # TODO Add other fields for trip parameters like distance, type of customer, time of day, etc.

    def __str__(self):
        return f"Trip for {self.courier.name} - Income: {self.income}"


class IncomeIncrease(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    increase_amount = models.IntegerField(validators=[MinValueValidator(0)])
    reason = models.TextField()

    def __str__(self):
        return f"Income increase for {self.courier.name} - Amount: {self.increase_amount} - Reason: {self.reason}"


class IncomeDeduction(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    deduction_amount = models.IntegerField(validators=[MinValueValidator(0)])
    reason = models.TextField()

    def __str__(self):
        return f"Income deduction for {self.courier.name} - Amount: {self.deduction_amount} - Reason: {self.reason}"
