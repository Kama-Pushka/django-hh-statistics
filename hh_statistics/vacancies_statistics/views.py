import requests
from django.shortcuts import render, get_object_or_404

import hhru

from vacancies_statistics.models import *

SELECTED_TEXT = 'NAME:("c#" OR "c sharp" OR "шарп" OR "с#")'

def index_page(request):
    return render(request, 'index.html')

def main_statistics_page(request):
    stats = get_object_or_404(Main_Statistics, pk=1) # Main_Statistics.objects.first()

    context = {
        'salary_chart': stats.salary_chart,
        'salary_data': stats.salary_data,
        'vacancy_chart': stats.vacancy_chart,
        'vacancy_data': stats.vacancy_data,
        'city_salary_chart': stats.city_salary_chart,
        'city_salary_data': stats.city_salary_data,
        'city_vacancy_share_chart': stats.city_vacancy_share_chart,
        'city_vacancy_share_data': stats.city_vacancy_share_data,

        'top_skills_2015_chart': stats.top_skills_2015_chart,
        'top_skills_2015_data': stats.top_skills_2015_data,

        'top_skills_2016_chart': stats.top_skills_2016_chart,
        'top_skills_2016_data': stats.top_skills_2016_data,

        'top_skills_2017_chart': stats.top_skills_2017_chart,
        'top_skills_2017_data': stats.top_skills_2017_data,

        'top_skills_2018_chart': stats.top_skills_2018_chart,
        'top_skills_2018_data': stats.top_skills_2018_data,

        'top_skills_2019_chart': stats.top_skills_2019_chart,
        'top_skills_2019_data': stats.top_skills_2019_data,

        'top_skills_2020_chart': stats.top_skills_2020_chart,
        'top_skills_2020_data': stats.top_skills_2020_data,

        'top_skills_2021_chart': stats.top_skills_2021_chart,
        'top_skills_2021_data': stats.top_skills_2021_data,

        'top_skills_2022_chart': stats.top_skills_2022_chart,
        'top_skills_2022_data': stats.top_skills_2022_data,

        'top_skills_2023_chart': stats.top_skills_2023_chart,
        'top_skills_2023_data': stats.top_skills_2023_data,

        'top_skills_2024_chart': stats.top_skills_2024_chart,
        'top_skills_2024_data': stats.top_skills_2024_data
    }
    return render(request, 'main_statistics.html', context)

def relevance_page(request):
    stats = get_object_or_404(Relevance_Statistics, pk=1) # Relevance_Statistics.objects.first()

    context = {
        'profession_salary_chart': stats.profession_salary_chart,
        'profession_salary_data': stats.profession_salary_data,
        'profession_vacancy_chart': stats.profession_vacancy_chart,
        'profession_vacancy_data': stats.profession_vacancy_data,
    }

    return render(request, 'relevance.html', context)

def geography_page(request):
    stats = get_object_or_404(Geography_Statistics, pk=1) # Geography_Statistics.objects.first()

    context = {
        'salary_chart': stats.salary_chart,
        'salary_data': stats.salary_data,
        'vacancy_chart': stats.vacancy_chart,
        'vacancy_data': stats.vacancy_data
    }

    return render(request, 'geography.html', context)

def skills_page(request):
    stats = get_object_or_404(Skills_Statistics, pk=1) # Skills_Statistics.objects.first()

    context = {
        'top_skills_2015_chart': stats.top_skills_2015_chart,
        'top_skills_2015_data': stats.top_skills_2015_data,

        'top_skills_2016_chart': stats.top_skills_2016_chart,
        'top_skills_2016_data': stats.top_skills_2016_data,

        'top_skills_2017_chart': stats.top_skills_2017_chart,
        'top_skills_2017_data': stats.top_skills_2017_data,

        'top_skills_2018_chart': stats.top_skills_2018_chart,
        'top_skills_2018_data': stats.top_skills_2018_data,

        'top_skills_2019_chart': stats.top_skills_2019_chart,
        'top_skills_2019_data': stats.top_skills_2019_data,

        'top_skills_2020_chart': stats.top_skills_2020_chart,
        'top_skills_2020_data': stats.top_skills_2020_data,

        'top_skills_2021_chart': stats.top_skills_2021_chart,
        'top_skills_2021_data': stats.top_skills_2021_data,

        'top_skills_2022_chart': stats.top_skills_2022_chart,
        'top_skills_2022_data': stats.top_skills_2022_data,

        'top_skills_2023_chart': stats.top_skills_2023_chart,
        'top_skills_2023_data': stats.top_skills_2023_data,

        'top_skills_2024_chart': stats.top_skills_2024_chart,
        'top_skills_2024_data': stats.top_skills_2024_data
    }

    return render(request, 'skills.html', context)

def recent_vacancies_page(request):
    vacancies = [v for v in hhru.Client().search_vacancies(text=SELECTED_TEXT, period=1, order_by=hhru.consts.VACANCY_SEARCH_ORDER_PUBLICATION_TIME)][:10]
    for v in vacancies:
        data = requests.get(v['url']).json()
        v['desc'] = data['description']
        v['skills'] = data['key_skills']

    return render(request, 'recent_vacancies.html', {'vacancies': vacancies})