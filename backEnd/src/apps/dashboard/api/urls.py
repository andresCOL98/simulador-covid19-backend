from django.urls import path

from .views import GetCountryDataCovidByCountry, GetCountrys

urlpatterns = [
    path(
        "countrys/",
        GetCountrys.as_view(),
        name="getCountrys",
    ),
    path(
        "<str:id_country>/",
        GetCountryDataCovidByCountry.as_view(),
        name="countryDataCovid_by_country",
    ),
]