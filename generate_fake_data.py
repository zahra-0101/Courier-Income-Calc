from courier.models import Courier, Trip, IncomeIncrease, IncomeDeduction
import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "miare.settings")
django.setup()


fake = Faker()


def generate_fake_data(num_couriers=10, num_trips=50, num_increases=20, num_deductions=10):
    # Generate fake couriers
    couriers = [Courier.objects.create(name=fake.name())
                for _ in range(num_couriers)]

    # Generate fake trips
    for _ in range(num_trips):
        courier = random.choice(couriers)
        Trip.objects.create(
            courier=courier,
            income=random.uniform(10, 1000),
        )

    # Generate fake income increases
    for _ in range(num_increases):
        courier = random.choice(couriers)
        IncomeIncrease.objects.create(
            courier=courier,
            income=random.uniform(1, 100),
            reason=fake.text(),
        )

    # Generate fake income deductions
    for _ in range(num_deductions):
        courier = random.choice(couriers)
        IncomeDeduction.objects.create(
            courier=courier,
            income=random.uniform(-50, -1),
            reason=fake.text(),
        )


if __name__ == "__main__":
    generate_fake_data()
