import json
from django.shortcuts import render
from .models import Vacancy, Company
from django.http import JsonResponse
from .serializers import CompanySerializer, VacancySerializer


def company_list(request):
    categories = Company.objects.all()
    serializer = CompanySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_company(request, id):
    try:
        company = Company.objects.get(id=id)
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    

def get_company_vacancy(request, id):
    try:
        vacancy = Vacancy.objects.filter(company_id=id)
        data = {'vacancies': list(vacancy.values())}
        return JsonResponse(data, safe=False)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    serializer = VacancySerializer(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    

def top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)
