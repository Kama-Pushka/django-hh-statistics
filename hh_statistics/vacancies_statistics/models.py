from django.db import models

class Main_Statistics(models.Model):
    salary_img = models.ImageField(blank=True, verbose_name='График Динамика уровня зарплат по годам')
    salary_table = models.TextField(blank=True, verbose_name='Таблица Динамика уровня зарплат по годам')

    vacancy_img = models.ImageField(blank=True, verbose_name='График Динамика количества вакансий по годам ')
    vacancy_table = models.TextField(blank=True, verbose_name='Таблица Динамика количества вакансий по годам ')

    city_salary_img = models.ImageField(blank=True, verbose_name='График Уровень зарплат по городам')
    city_salary_table = models.TextField(blank=True, verbose_name='Таблица Уровень зарплат по городам')

    city_vacancy_share_img = models.ImageField(blank=True, verbose_name='График Доля вакансий по городам')
    city_vacancy_share_table = models.TextField(blank=True, verbose_name='Таблица Доля вакансий по городам')

    top_skills_2015_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2015 год')
    top_skills_2015_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2015 год')

    top_skills_2016_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2016 год')
    top_skills_2016_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2016 год')

    top_skills_2017_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2017 год')
    top_skills_2017_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2017 год')

    top_skills_2018_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2018 год')
    top_skills_2018_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2018 год')

    top_skills_2019_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2019 год')
    top_skills_2019_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2019 год')

    top_skills_2020_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2020 год')
    top_skills_2020_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2020 год')

    top_skills_2021_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2021 год')
    top_skills_2021_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2021 год')

    top_skills_2022_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2022 год')
    top_skills_2022_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2022 год')

    top_skills_2023_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2023 год')
    top_skills_2023_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2023 год')

    top_skills_2024_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2024 год')
    top_skills_2024_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2024 год')

    class Meta:
        verbose_name = 'Общая статистика'

class Relevance_Statistics(models.Model):
    profession_salary_img = models.ImageField(blank=True, verbose_name='График Динамика уровня зарплат по годам для выбранной профессии')
    profession_salary_table = models.TextField(blank=True, verbose_name='Таблица Динамика уровня зарплат по годам для выбранной профессии')

    profession_vacancy_img = models.ImageField(blank=True, verbose_name='График Динамика количества вакансий по годам для выбранной профессии')
    profession_vacancy_table = models.TextField(blank=True, verbose_name='Таблица Динамика количества вакансий по годам для выбранной профессии')

    class Meta:
        verbose_name = 'Востребованность'

class Geography_Statistics(models.Model):
    salary_img = models.ImageField(blank=True, verbose_name='График Уровень зарплат по городам для выбранной профессии')
    salary_table = models.TextField(blank=True, verbose_name='Таблица Уровень зарплат по городам для выбранной профессии')

    vacancy_img = models.ImageField(blank=True, verbose_name='График Доля вакансий по городам для выбранной профессии')
    vacancy_table = models.TextField(blank=True, verbose_name='Таблица Доля вакансий по городам для выбранной профессии')

    class Meta:
        verbose_name = 'География'

class Skills_Statistics(models.Model):
    top_skills_2015_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2015 год')
    top_skills_2015_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2015 год')

    top_skills_2016_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2016 год')
    top_skills_2016_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2016 год')

    top_skills_2017_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2017 год')
    top_skills_2017_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2017 год')

    top_skills_2018_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2018 год')
    top_skills_2018_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2018 год')

    top_skills_2019_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2019 год')
    top_skills_2019_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2019 год')

    top_skills_2020_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2020 год')
    top_skills_2020_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2020 год')

    top_skills_2021_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2021 год')
    top_skills_2021_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2021 год')

    top_skills_2022_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2022 год')
    top_skills_2022_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2022 год')

    top_skills_2023_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2023 год')
    top_skills_2023_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2023 год')

    top_skills_2024_img = models.ImageField(blank=True, verbose_name='График ТОП-20 навыков за 2024 год')
    top_skills_2024_table = models.TextField(blank=True, verbose_name='Таблица ТОП-20 навыков за 2024 год')

    class Meta:
        verbose_name = 'Навыки'