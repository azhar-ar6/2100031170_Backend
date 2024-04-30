from django.db import models

# Create your models here.

class Country(models.Model):
    country_id = models.CharField(primary_key=True, max_length=10)
    country_name = models.CharField(max_length=20)
    region_id = models.IntegerField()

    def __str__(self):
        return self.country_name

    class Meta:
        db_table = "countries"


class Location(models.Model):
    location_id = models.IntegerField()
    street_address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name

    class Meta:
        db_table = "locations"