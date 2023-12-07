from django.urls import path
from .views import CourierListCreateView, TripListCreateView, IncomeIncreaseListCreateView, IncomeDeductionListCreateView, DailySalaryListCreateView

urlpatterns = [
    path('couriers/', CourierListCreateView.as_view(), name='courier-list-create'),
    path('trips/', TripListCreateView.as_view(), name='trip-list-create'),
    path('income-increases/', IncomeIncreaseListCreateView.as_view(),
         name='income-increase-list-create'),
    path('income-deductions/', IncomeDeductionListCreateView.as_view(),
         name='income-deduction-list-create'),
    path('daily-salaries/', DailySalaryListCreateView.as_view(),
         name='daily-salary-list-create'),
]
