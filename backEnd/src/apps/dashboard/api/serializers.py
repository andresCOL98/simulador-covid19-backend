from rest_framework import serializers

from apps.dashboard.models import Country

class CountryDataCovidSerializer(serializers.Serializer):

    id = serializers.IntegerField()

    country = Country

    infected = serializers.IntegerField()
    dead = serializers.IntegerField()
    uci = serializers.IntegerField()

class CountrySerializer(serializers.Serializer):

    id = serializers.IntegerField()

    name = serializers.CharField()

    def create(self, validate_data):
        instance = Country(self)
        instance.id = validate_data.get('id')
        instance.name = validate_data.get('name')
        instance.save()
        return instance
    
    def validate_id(self, data):
        countrys = Country.objects.get(id = data)
        if len(countrys) != 0:
            raise serializers.ValidationError("Ya existe un pais con este id")
        else:
            return data

    def familiar_list(self):
        countrys = Country.objects.all()
        return countrys