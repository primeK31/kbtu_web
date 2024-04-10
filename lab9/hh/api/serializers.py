from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        instance = Company(name=validated_data.get('name'), description=validated_data.get('description'), city=validated_data.get('city'), address=validated_data.get('address'))
        instance.save()
        return instance


class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.FloatField()
    #company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
