from django.shortcuts import render

import hhru

from vacancies_statistics.models import *

SELECTED_TEXT = 'NAME:("c#" OR "c sharp" OR "шарп" OR "с#")'

def index_page(request):
    return render(request, 'index.html')

def main_statistics_page(request):
    stats = Main_Statistics.objects.first()

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
    stats = Relevance_Statistics.objects.first()

    context = {
        'profession_salary_chart': stats.profession_salary_chart,
        'profession_salary_data': stats.profession_salary_data,
        'profession_vacancy_chart': stats.profession_vacancy_chart,
        'profession_vacancy_data': stats.profession_vacancy_data,
    }

    return render(request, 'relevance.html', context)

def geography_page(request):
    stats = Geography_Statistics.objects.first()

    context = {
        'salary_chart': stats.salary_chart,
        'salary_data': stats.salary_data,
        'vacancy_chart': stats.vacancy_chart,
        'vacancy_data': stats.vacancy_data
    }

    return render(request, 'geography.html', context)

def skills_page(request):
    stats = Skills_Statistics.objects.first()

    context = {
        'top_skills_2015_chart': stats.top_skills_2015_chart.url,
        'top_skills_2015_data': stats.top_skills_2015_data,

        'top_skills_2016_chart': stats.top_skills_2016_chart.url,
        'top_skills_2016_data': stats.top_skills_2016_data,

        'top_skills_2017_chart': stats.top_skills_2017_chart.url,
        'top_skills_2017_data': stats.top_skills_2017_data,

        'top_skills_2018_chart': stats.top_skills_2018_chart.url,
        'top_skills_2018_data': stats.top_skills_2018_data,

        'top_skills_2019_chart': stats.top_skills_2019_chart.url,
        'top_skills_2019_data': stats.top_skills_2019_data,

        'top_skills_2020_chart': stats.top_skills_2020_chart.url,
        'top_skills_2020_data': stats.top_skills_2020_data,

        'top_skills_2021_chart': stats.top_skills_2021_chart.url,
        'top_skills_2021_data': stats.top_skills_2021_data,

        'top_skills_2022_chart': stats.top_skills_2022_chart.url,
        'top_skills_2022_data': stats.top_skills_2022_data,

        'top_skills_2023_chart': stats.top_skills_2023_chart.url,
        'top_skills_2023_data': stats.top_skills_2023_data,

        'top_skills_2024_chart': stats.top_skills_2024_chart.url,
        'top_skills_2024_data': stats.top_skills_2024_data
    }

    return render(request, 'skills.html', context)

def recent_vacancies_page(request):
    vacancies = [v for v in hhru.Client().search_vacancies_over_pages(text=SELECTED_TEXT, period=1, order_by=hhru.consts.VACANCY_SEARCH_ORDER_PUBLICATION_TIME)][:10]
    return render(request, 'recent_vacancies.html', {'vacancies': vacancies})