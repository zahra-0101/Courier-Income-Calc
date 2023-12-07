from django.test import TestCase
from django.utils import timezone
from courier.models import Courier, Trip, IncomeIncrease, IncomeDeduction, DailySalary


class DailySalaryTestCase(TestCase):
    def setUp(self):
        self.courier = Courier.objects.create(name="John Doe")
        self.trip = Trip.objects.create(courier=self.courier, income=100)
        self.increase = IncomeIncrease.objects.create(
            courier=self.courier, income=50, reason="Bonus"
        )
        self.deduction = IncomeDeduction.objects.create(
            courier=self.courier, income=-30, reason="Penalty"
        )

    def test_daily_salary_instance_after_trip(self):
        courier = Courier.objects.create(name="Mina")
        trip = Trip.objects.create(courier=courier, income=110)
        self.assertEqual(
            DailySalary.objects.filter(
                courier=self.courier, date=trip.date_created.date()
            ).exists(),
            True,
            "Signal doesn't work(update_daily_salary).",
        )

    def test_daily_salary_instance_after_income_increase(self):
        courier = Courier.objects.create(name="Mina")
        trip = Trip.objects.create(courier=courier, income=110)
        self.assertEqual(
            DailySalary.objects.filter(
                courier=self.courier, date=trip.date_created.date()
            ).exists(),
            True,
            "Signal doesn't work(update_daily_salary).",
        )

    def test_daily_salary_instance_after_income_deduction(self):
        courier = Courier.objects.create(name="Mina")
        trip = Trip.objects.create(courier=courier, income=110)
        self.assertEqual(
            DailySalary.objects.filter(
                courier=self.courier, date=trip.date_created.date()
            ).exists(),
            True,
            "Signal doesn't work(update_daily_salary).",
        )

    def test_create_total_salary_after_trip(self):
        courier = Courier.objects.create(name="Richard")
        trip = Trip.objects.create(courier=courier, income=110)
        total_salary = DailySalary.objects.get(
            courier=courier, date=trip.date_created.date()
        )
        expected_total_salary = 110
        self.assertEqual(
            total_salary.total_salary,
            expected_total_salary,
            f"Expected total salary to be {expected_total_salary}, but got {total_salary.total_salary} when a new instance is created after a trip.",
        )

    def test_create_total_salary_after_income_increase(self):
        courier = Courier.objects.create(name="Richard")
        trip = IncomeIncrease.objects.create(courier=courier, income=50)
        total_salary = DailySalary.objects.get(
            courier=courier, date=trip.date_created.date()
        )
        expected_total_salary = 50
        self.assertEqual(
            total_salary.total_salary,
            expected_total_salary,
            f"Expected total salary to be {expected_total_salary}, but got {total_salary.total_salary} when a new instance is created after income increase.",
        )

    def test_create_total_salary_after_income_deduction(self):
        courier = Courier.objects.create(name="Richard")
        trip = IncomeDeduction.objects.create(courier=courier, income=-120)
        total_salary = DailySalary.objects.get(
            courier=courier, date=trip.date_created.date()
        )
        expected_total_salary = -120
        self.assertEqual(
            total_salary.total_salary,
            expected_total_salary,
            f"Expected total salary to be {expected_total_salary}, but got {total_salary.total_salary} when a new instance is created after income deduction.",
        )

    def test_update_trip_total_salary(self):
        # Check if total salary is updated correctly for a trip
        DailySalary.update_total_salary(self.trip)
        total_salary = DailySalary.objects.get(
            courier=self.courier, date=self.trip.date_created.date()
        )
        expected_total_salary = 220
        self.assertEqual(
            total_salary.total_salary,
            expected_total_salary,
            f"Expected total salary to be {expected_total_salary}, but got {total_salary.total_salary} when a new instance is updated after a trip.",
        )

    def test_update_total_salary_after_income_increase(self):
        # Check if total salary is updated correctly for an income increase
        DailySalary.update_total_salary(self.increase)
        total_salary = DailySalary.objects.get(
            courier=self.courier, date=self.increase.date_created.date()
        )
        expected_total_salary = 170
        self.assertEqual(
            total_salary.total_salary,
            expected_total_salary,
            f"Expected total salary to be {expected_total_salary}, but got {total_salary.total_salary} when a new instance is updated after income increase.",
        )

    def test_update_total_salary_after_income_deduction(self):
        # Check if total salary is updated correctly for an income deduction
        DailySalary.update_total_salary(self.deduction)
        total_salary = DailySalary.objects.get(
            courier=self.courier, date=self.deduction.date_created.date()
        )
        expected_total_salary = 90
        self.assertEqual(
            total_salary.total_salary,
            expected_total_salary,
            f"Expected total salary to be {expected_total_salary}, but got {total_salary.total_salary} when a new instance is updated after income deduction.",
        )
