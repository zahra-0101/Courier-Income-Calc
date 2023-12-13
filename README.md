# Courier-Income-Calc

## Models

### Courier

Represents a courier with a name.

### Trip

Represents a trip made by a courier, including income and other parameters.

### IncomeIncrease

Represents an increase in income for a courier, independent of trips.

### IncomeDeduction

Represents a deduction from income for a courier, independent of trips.

## Setup

1. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

2. Apply database migrations:
	```bash
	python manage.py makemigrations
	python manage.py migrate
	```

3. Generate Fake Data

    ### Usage
			python generate_fake_data.py

3. Run test
	python manage.py test courier


# Project API Documentation

## Couriers

### List and Create Couriers

- **Endpoint:** `/api/couriers/`
- **Method:** GET, POST
- **Description:** Get a list of couriers or create a new courier.

## Trips

### List and Create Trips

- **Endpoint:** `/api/trips/`
- **Method:** GET, POST
- **Description:** Get a list of trips or create a new trip.

## Income Increases

### List and Create Income Increases

- **Endpoint:** `/api/income-increases/`
- **Method:** GET, POST
- **Description:** Get a list of income increases or create a new income increase.

## Income Deductions

### List and Create Income Deductions

- **Endpoint:** `/api/income-deductions/`
- **Method:** GET, POST
- **Description:** Get a list of income deductions or create a new income deduction.

## Daily Salaries

### List Daily Salaries

- **Endpoint:** `/api/daily-salaries/`
- **Method:** GET
- **Description:** Get a list of daily salaries.

## Weekly Salaries

### List Weekly Salaries

- **Endpoint:** `/api/weekly-salary/`
- **Method:** GET
- **Description:** Get a list of weekly salaries.


# Signal Handler Documentation

## Update Salary Signal Handler

This signal handler is connected to the `post_save` signal for the following models: `Trip`, `IncomeIncrease`, and `IncomeDeduction`. It triggers when a new instance of any of these models is created.

### Purpose

The purpose of this signal handler is to update salary-related information, specifically the `DailySalary` and `WeeklySalary` records associated with the created instance.

### Signal Connections

- **Connected to:** `post_save` signal
- **Models:** `Trip`, `IncomeIncrease`, `IncomeDeduction`

# Models Documentation

## Courier Model

- **Fields:**
  - `name`: CharField with a maximum length of 255 characters.
  - `date_created`: DateTimeField set to auto_now_add.


## Trip Model

- **Fields:**
  - `courier`: ForeignKey relation to the Courier model.
  - `date_created`: DateTimeField set to auto_now_add.
  - `income`: IntegerField with validators for minimum value (0).

### Methods

#### `delete_instance(cls, instance, error_message)`

- Class method to delete the instance, create an UnsuccessfulUpdate record, and delete the instance.

## IncomeIncrease Model

- **Fields:**
  - `courier`: ForeignKey relation to the Courier model.
  - `date_created`: DateTimeField set to auto_now_add.
  - `income`: IntegerField with validators for minimum value (0).
  - `reason`: TextField.

### Methods

#### `delete_instance(cls, instance, error_message)`

- Class method to delete the instance, create an UnsuccessfulUpdate record, and delete the instance.

## IncomeDeduction Model

- **Fields:**
  - `courier`: ForeignKey relation to the Courier model.
  - `date_created`: DateTimeField set to auto_now_add.
  - `income`: IntegerField with validators for maximum value (0).
  - `reason`: TextField.

### Methods

#### `delete_instance(cls, instance, error_message)`

- Class method to delete the instance, create an UnsuccessfulUpdate record, and delete the instance.


# Daily and Weekly Salary Models Documentation

## DailySalary Model

The `DailySalary` model is designed to track the daily earnings of couriers in your system. It provides a way to record and update the total salary for a given day based on related instances such as `Trip`, `IncomeIncrease`, or `IncomeDeduction`.

### Fields:

- `courier`: ForeignKey relation to the `Courier` model, linking the daily salary entry to a specific courier.
- `date`: DateField, representing the date for which the salary is recorded.
- `salary`: IntegerField with a default value of 0, storing the total earnings for the specified day.

### Methods:

#### `update_total_salary(cls, instance)`

A class method that updates the total salary for a given day based on the income from a related instance. It fetches or creates a `DailySalary` instance associated with the courier and date of the provided instance and adds the income to the existing salary.

## WeeklySalary Model

The `WeeklySalary` model is designed to track the weekly earnings of couriers in your system. It allows you to record and update the total salary for a given week based on related instances.

### Fields:

- `courier`: ForeignKey relation to the `Courier` model, linking the weekly salary entry to a specific courier.
- `week_start_date`: DateField, representing the start date of the week for which the salary is recorded.
- `salary`: IntegerField with a default value of 0, storing the total earnings for the specified week.

### Methods:

#### `update_weekly_salary(cls, instance)`

A class method that updates the total salary for a given week based on the income from a related instance. It calculates the start date of the week (assuming the week starts on Saturday) based on the provided instance's date. Then, it fetches or creates a `WeeklySalary` instance associated with the courier and calculated week start date and adds the income to the existing weekly salary.


<!-- pipenv lock -r > requirements.txt -->

