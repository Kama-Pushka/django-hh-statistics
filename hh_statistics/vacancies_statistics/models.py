from django.db import models

class Main_Statistics(models.Model):
    salary_chart = models.ImageField(blank=True, verbose_name='График Динамика уровня зарплат по годам')
    salary_data = models.TextField(blank=True, verbose_name='Таблица Динамика уровня зарплат по годам')

    vacancy_chart = models.ImageField(blank=True, verbose_name='График Динамика уровня зарплат по годам')
    vacancy_data = models.TextField(blank=True, verbose_name='Таблица Динамика уровня зарплат по годам')

    city_salary_chart = models.ImageField(blank=True, verbose_name='График Уровень зарплат по городам')
    city_salary_data = models.TextField(blank=True, verbose_name='Таблица Уровень зарплат по городам')

    city_vacancy_share_chart = models.ImageField(blank=True, verbose_name='График Доля вакансий по городам')
    city_vacancy_share_data = models.TextField(blank=True, verbose_name='Таблица Доля вакансий по городам')

    top_skills_2015_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2015 год')
    top_skills_2015_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2015 год')

    top_skills_2016_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2016 год')
    top_skills_2016_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2016 год')

    top_skills_2017_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2017 год')
    top_skills_2017_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2017 год')

    top_skills_2018_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2018 год')
    top_skills_2018_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2018 год')

    top_skills_2019_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2019 год')
    top_skills_2019_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2019 год')

    top_skills_2020_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2020 год')
    top_skills_2020_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2020 год')

    top_skills_2021_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2021 год')
    top_skills_2021_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2021 год')

    top_skills_2022_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2022 год')
    top_skills_2022_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2022 год')

    top_skills_2023_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2023 год')
    top_skills_2023_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2023 год')

    top_skills_2024_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2024 год')
    top_skills_2024_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2024 год')

    class Meta:
        verbose_name = 'Общая статистика'

class Relevance_Statistics(models.Model):
    profession_salary_chart = models.ImageField(blank=True, verbose_name='График Динамика уровня зарплат по годам для выбранной профессии')
    profession_salary_data = models.TextField(blank=True, verbose_name='Таблица Динамика уровня зарплат по годам для выбранной профессии')

    profession_vacancy_chart = models.ImageField(blank=True, verbose_name='График Динамика количества вакансий по годам для выбранной профессии')
    profession_vacancy_data = models.TextField(blank=True, verbose_name='Таблица Динамика количества вакансий по годам для выбранной профессии')

    class Meta:
        verbose_name = 'Востребованность'

class Geography_Statistics(models.Model):
    salary_chart = models.ImageField(blank=True, verbose_name='График Уровень зарплат по городам для выбранной профессии')
    salary_data = models.TextField(blank=True, verbose_name='Таблица Уровень зарплат по городам для выбранной профессии')

    vacancy_chart = models.ImageField(blank=True, verbose_name='График Доля вакансий по городам для выбранной профессии')
    vacancy_data = models.TextField(blank=True, verbose_name='Таблица Доля вакансий по городам для выбранной профессии')

    class Meta:
        verbose_name = 'География'

class Skills_Statistics(models.Model):
    top_skills_2015_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2015 год')
    top_skills_2015_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2015 год')

    top_skills_2016_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2016 год')
    top_skills_2016_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2016 год')

    top_skills_2017_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2017 год')
    top_skills_2017_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2017 год')

    top_skills_2018_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2018 год')
    top_skills_2018_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2018 год')

    top_skills_2019_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2019 год')
    top_skills_2019_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2019 год')

    top_skills_2020_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2020 год')
    top_skills_2020_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2020 год')

    top_skills_2021_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2021 год')
    top_skills_2021_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2021 год')

    top_skills_2022_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2022 год')
    top_skills_2022_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2022 год')

    top_skills_2023_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2023 год')
    top_skills_2023_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2023 год')

    top_skills_2024_chart = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2024 год')
    top_skills_2024_data = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2024 год')

    class Meta:
        verbose_name = 'Навыки'