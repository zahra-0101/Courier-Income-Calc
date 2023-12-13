from rest_framework import serializers
from .models import Courier, Trip, IncomeIncrease, IncomeDeduction, DailySalary, WeeklySalary


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class IncomeIncreaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeIncrease
        fields = '__all__'


class IncomeDeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeDeduction
        fields = '__all__'


class DailySalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySalary
        fields = '__all__'


class CustomWeeklySalarySerializer(serializers.ModelSerializer):
    courier = CourierSerializer()

    class Meta:
        model = WeeklySalary
        fields = '__all__'
