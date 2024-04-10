from django.urls import path
from .views import company_list, get_company, get_company_vacancy, vacancy_list, get_vacancy, top_ten

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:id>', get_company),
    path('companies/<int:id>/vacancies', get_company_vacancy), 
    path('vacancies/', vacancy_list), 
    path('vacancies/<int:id>', get_vacancy), 
    path('vacancies/top_ten', top_ten),
]
