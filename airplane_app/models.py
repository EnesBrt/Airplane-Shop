from django.db import models
from django_countries.fields import CountryField


class MyModel(models.Model):
    country = CountryField(blank_label="(select country)")
