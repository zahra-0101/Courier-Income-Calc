from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework import generics, viewsets, filters
import django_filters.rest_framework

from courier.filters import WeeklySalaryFilter

# from courier.filters import WeeklySalaryFilter
from .models import (
    Courier,
    Trip,
    IncomeIncrease,
    IncomeDeduction,
    DailySalary,
    WeeklySalary,
)
from .serializers import (
    CourierSerializer,
    CustomWeeklySalarySerializer,
    TripSerializer,
    IncomeIncreaseSerializer,
    IncomeDeductionSerializer,
    DailySalarySerializer,
)


class CourierListCreateView(generics.ListCreateAPIView):
    # TODO: permission_classes
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class TripListCreateView(generics.ListCreateAPIView):
    # TODO: permission_classes
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class IncomeIncreaseListCreateView(generics.ListCreateAPIView):
    # TODO: permission_classes
    queryset = IncomeIncrease.objects.all()
    serializer_class = IncomeIncreaseSerializer


class IncomeDeductionListCreateView(generics.ListCreateAPIView):
    # TODO: permission_classes
    queryset = IncomeDeduction.objects.all()
    serializer_class = IncomeDeductionSerializer


class DailySalaryListCreateView(generics.ListCreateAPIView):
    # TODO: permission_classes
    queryset = DailySalary.objects.all()
    serializer_class = DailySalarySerializer


class WeeklySalaryViewSet(generics.ListAPIView):
    # TODO: permission_classes
    serializer_class = CustomWeeklySalarySerializer
    queryset = WeeklySalary.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = WeeklySalaryFilter