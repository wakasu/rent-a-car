from django.db import models

class vehicel(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    daily_rent = models.DecimalField(max_digits = 5, decimal_places = 0)
    weekly_rent = models.DecimalField(max_digits = 5, decimal_places = 0)
    fifteen_day_rent = models.DecimalField(max_digits = 5, decimal_places = 0)
    monthly_rent = models.DecimalField(max_digits = 5, decimal_places = 0)

    car = 'cr'
    luxury = 'lx'
    suv = 'suv'
    van = 'vn'

    car_category_choices = (
        (car, 'Cars'),
        (luxury, 'luxury'),
        (suv, 'SUV'),
        (van, 'Vans & Buses'),
    )
    car_category = models.CharField(
        max_length = 2,
        choices = car_category_choices,
        default = car,
    )

    image1 = models.FilePathField(path="/static/img")
    image2 = models.FilePathField(path="/static/img")
    image3 = models.FilePathField(path="/static/img")
    image4 = models.FilePathField(path="/static/img")