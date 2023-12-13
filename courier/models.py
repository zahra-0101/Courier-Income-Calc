from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta
from django.contrib.contenttypes.models import ContentType


class Courier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Trip(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    income = models.IntegerField(
        validators=[MinValueValidator(0)]
    )  # TODO: BigintegerField
    # TODO: Add other fields for trip parameters like distance, type of customer, time of day, etc.

    @classmethod
    def delete_instance(cls, instance, error_message):
        # Your deletion logic here
        UnsuccessfulUpdate.create_from_instance(instance, error_message)
        instance.delete()

    def __str__(self):
        return f"Trip for {self.courier.name} - Income: {self.income}"


class IncomeIncrease(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    income = models.IntegerField(
        validators=[MinValueValidator(0)]
    )  # TODO: BigintegerField
    reason = models.TextField()

    @classmethod
    def delete_instance(cls, instance, error_message):
        # Your deletion logic here
        UnsuccessfulUpdate.create_from_instance(instance, error_message)
        instance.delete()

    def __str__(self):
        return f"Income increase for {self.courier.name} - Amount: {self.increase_amount} - Reason: {self.reason}"


class IncomeDeduction(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    income = models.IntegerField(
        validators=[MaxValueValidator(0)]
    )  # TODO: BigintegerField
    reason = models.TextField()

    @classmethod
    def delete_instance(cls, instance, error_message):
        # Your deletion logic here
        UnsuccessfulUpdate.create_from_instance(instance, error_message)
        instance.delete()

    def __str__(self):
        return f"Income deduction for {self.courier.name} - Amount: {self.deduction_amount} - Reason: {self.reason}"


class DailySalary(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    date = models.DateField()
    salary = models.IntegerField(default=0)  # TODO: BigintegerField
    date_updated = models.DateTimeField(auto_now_add=True)

    @classmethod
    def update_total_salary(cls, instance):
        daily_salary, created = cls.objects.get_or_create(
            courier=instance.courier, date=instance.date_created.date()
        )
        daily_salary.salary += instance.income
        daily_salary.save()


class WeeklySalary(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    week_start_date = models.DateField()
    salary = models.IntegerField(default=0)  # TODO: BigintegerField

    @classmethod
    def update_weekly_salary(cls, instance):
        # Calculate the week start date (Saturday) based on the provided date
        week_start_date = instance.date_created - timedelta(
            days=instance.date_created.weekday() + 2
        )

        # Update or create WeeklySalary instance
        weekly_salary, created = cls.objects.get_or_create(
            courier=instance.courier, week_start_date=week_start_date.date()
        )

        # Update the total earnings
        weekly_salary.salary += instance.income
        weekly_salary.save()


class UnsuccessfulUpdate(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    error_message = models.TextField()

    # Fields from models
    courier_name = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    income = models.IntegerField(validators=[MinValueValidator(0)])

    @classmethod
    def create_from_instance(cls, instance, error_message):
        content_type = ContentType.objects.get_for_model(instance)

        # Fields specific to the sender model
        courier_name = instance.courier.name if hasattr(instance, "courier") else None
        date_created = (
            instance.date_created if hasattr(instance, "date_created") else None
        )
        income = instance.income if hasattr(instance, "income") else None
        # Add other fields as needed

        return cls.objects.create(
            content_type=content_type,
            error_message=error_message,
            courier_name=courier_name,
            date_created=date_created,
            income=income,
        )
