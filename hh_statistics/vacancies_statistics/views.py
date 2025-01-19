import requests
from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import render

import hhru

from vacancies_statistics.models import *

def index_page(request):
    return render(request, 'index.html')

def main_statistics_page(request):
    stats = Main_Statistics.objects.first()
    if stats is None:
        raise Http404

    return render(request, 'main_statistics.html', model_to_dict(stats))

def relevance_page(request):
    stats = Relevance_Statistics.objects.first()
    if stats is None:
        raise Http404

    return render(request, 'relevance.html', model_to_dict(stats))

def geography_page(request):
    stats = Geography_Statistics.objects.first()
    if stats is None:
        raise Http404

    return render(request, 'geography.html', model_to_dict(stats))

def skills_page(request):
    stats = Skills_Statistics.objects.first()
    if stats is None:
        raise Http404

    return render(request, 'skills.html', model_to_dict(stats))

SELECTED_TEXT = 'NAME:("c#" OR "c sharp" OR "шарп" OR "с#")' # 'Системный аналитик'

def recent_vacancies_page(request):
    vacancies = [v for v in hhru.Client().search_vacancies(text=SELECTED_TEXT, period=1, order_by=hhru.consts.VACANCY_SEARCH_ORDER_PUBLICATION_TIME)][:10]
    for v in vacancies:
        data = requests.get(v['url']).json()
        v['desc'] = data['description']
        v['skills'] = data['key_skills']

    return render(request, 'recent_vacancies.html', {'vacancies': vacancies})