from rest_framework import generics
from .models import Courier, Trip, IncomeIncrease, IncomeDeduction, DailySalary
from .serializers import CourierSerializer, TripSerializer, IncomeIncreaseSerializer, IncomeDeductionSerializer, DailySalarySerializer


class CourierListCreateView(generics.ListCreateAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class TripListCreateView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class IncomeIncreaseListCreateView(generics.ListCreateAPIView):
    queryset = IncomeIncrease.objects.all()
    serializer_class = IncomeIncreaseSerializer


class IncomeDeductionListCreateView(generics.ListCreateAPIView):
    queryset = IncomeDeduction.objects.all()
    serializer_class = IncomeDeductionSerializer


class DailySalaryListCreateView(generics.ListCreateAPIView):
    queryset = DailySalary.objects.all()
    serializer_class = DailySalarySerializer
