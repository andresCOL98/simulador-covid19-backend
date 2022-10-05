from django.db import models

class Country(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)

    name = models.CharField(max_length=200)

class CountryDataCovid(models.Model):

    id = models.AutoField(primary_key= True,unique=True)

    country = models.ForeignKey(        
        to=Country,
        verbose_name="country",
        on_delete=models.CASCADE,
        related_name="world_data_covid_id_country",)

    infected = models.BigIntegerField()
    dead = models.BigIntegerField()
    uci = models.BigIntegerField()
    fecha =  models.CharField(max_length=1000)