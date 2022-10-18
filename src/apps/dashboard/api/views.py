from itertools import count
from rest_framework.response import Response
from .serializers import CountryDataCovidSerializer , CountrySerializer
from rest_framework.views import APIView
from rest_framework import status
from apps.dashboard.models import CountryDataCovid , Country
from sentry_sdk.api import capture_exception
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from .helpers import getDataCovid
from pathlib import Path

class GetCountrys(APIView):
    def get(self, request):
        try:
            countrys = Country.objects.all()
            if(countrys != None):
                serializer = CountrySerializer(countrys, many = True)
                return Response(serializer.data, status = HTTP_200_OK)
            else:
                return Response(data=None, status=HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as _ex:
            capture_exception(_ex)
            return Response(data=str(_ex), status=HTTP_500_INTERNAL_SERVER_ERROR)

class GetCountryDataCovidByCountry(APIView):
    def get(self, request, id_country):
        try:
            country = Country.objects.get(id=id_country)
            data = getDataCovid(country.name)
            uci_data = data[3]
            # , infected=data[0], dead=data[1], uci=uci_data
            country_data = CountryDataCovid.objects.filter(country=id_country)
            if(country_data.count()>0):
                
                country_data.update(country=country, infected=data[0], dead=data[1], uci=uci_data, fecha = data[2])
                countryDataCovid = CountryDataCovid.objects.get(country=id_country)
            else:
                CountryDataCovid.objects.create(country=country, infected=data[0], dead=data[1], uci=uci_data, fecha = data[2])
                countryDataCovid = CountryDataCovid.objects.get(country=id_country)
            if(countryDataCovid):
                serializer = CountryDataCovidSerializer(countryDataCovid, many = False)
                return Response(serializer.data, status= HTTP_200_OK)
            else:    
                return Response(data=str(_ex), status=HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as _ex:
            capture_exception(_ex)
            return Response(data=str(_ex), status=HTTP_500_INTERNAL_SERVER_ERROR)