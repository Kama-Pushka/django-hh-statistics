from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name='index'),
    path('main_statistics/', main_statistics_page, name='main_statistics'),
    path('relevance/', relevance_page, name='relevance'),
    path('geography/', geography_page, name='geography'),
    path('skills/', skills_page, name='skills'),
    path('recent_vacancies/', recent_vacancies_page, name='recent_vacancies'),
]
