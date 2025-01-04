from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def main_statistics_page(request):
    return render(request, 'main_statistics.html')

def relevance_page(request):
    return render(request, 'relevance.html')

def geography_page(request):
    return render(request, 'geography.html')

def skills_page(request):
    return render(request, 'skills.html')

def recent_vacancies_page(request):
    return render(request, 'recent_vacancies.html')