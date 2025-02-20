# Generated by Django 5.1.4 on 2025-01-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies_statistics', '0003_alter_geography_statistics_salary_chart_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geography_statistics',
            old_name='salary_chart',
            new_name='salary_img',
        ),
        migrations.RenameField(
            model_name='geography_statistics',
            old_name='salary_data',
            new_name='salary_table',
        ),
        migrations.RenameField(
            model_name='geography_statistics',
            old_name='vacancy_chart',
            new_name='vacancy_img',
        ),
        migrations.RenameField(
            model_name='geography_statistics',
            old_name='vacancy_data',
            new_name='vacancy_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='city_salary_chart',
            new_name='city_salary_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='city_salary_data',
            new_name='city_salary_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='city_vacancy_share_chart',
            new_name='city_vacancy_share_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='city_vacancy_share_data',
            new_name='city_vacancy_share_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='salary_chart',
            new_name='salary_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='salary_data',
            new_name='salary_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2015_chart',
            new_name='top_skills_2015_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2015_data',
            new_name='top_skills_2015_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2016_chart',
            new_name='top_skills_2016_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2016_data',
            new_name='top_skills_2016_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2017_chart',
            new_name='top_skills_2017_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2017_data',
            new_name='top_skills_2017_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2018_chart',
            new_name='top_skills_2018_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2018_data',
            new_name='top_skills_2018_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2019_chart',
            new_name='top_skills_2019_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2019_data',
            new_name='top_skills_2019_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2020_chart',
            new_name='top_skills_2020_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2020_data',
            new_name='top_skills_2020_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2021_chart',
            new_name='top_skills_2021_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2021_data',
            new_name='top_skills_2021_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2022_chart',
            new_name='top_skills_2022_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2022_data',
            new_name='top_skills_2022_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2023_chart',
            new_name='top_skills_2023_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2023_data',
            new_name='top_skills_2023_table',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2024_chart',
            new_name='top_skills_2024_img',
        ),
        migrations.RenameField(
            model_name='main_statistics',
            old_name='top_skills_2024_data',
            new_name='top_skills_2024_table',
        ),
        migrations.RenameField(
            model_name='relevance_statistics',
            old_name='profession_salary_chart',
            new_name='profession_salary_img',
        ),
        migrations.RenameField(
            model_name='relevance_statistics',
            old_name='profession_salary_data',
            new_name='profession_salary_table',
        ),
        migrations.RenameField(
            model_name='relevance_statistics',
            old_name='profession_vacancy_chart',
            new_name='profession_vacancy_img',
        ),
        migrations.RenameField(
            model_name='relevance_statistics',
            old_name='profession_vacancy_data',
            new_name='profession_vacancy_table',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2015_chart',
            new_name='top_skills_2015_img',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2015_data',
            new_name='top_skills_2015_table',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2016_chart',
            new_name='top_skills_2016_img',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2016_data',
            new_name='top_skills_2016_table',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2017_chart',
            new_name='top_skills_2017_img',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2017_data',
            new_name='top_skills_2017_table',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2018_chart',
            new_name='top_skills_2018_img',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2018_data',
            new_name='top_skills_2018_table',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2019_chart',
            new_name='top_skills_2019_img',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2019_data',
            new_name='top_skills_2019_table',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2020_chart',
            new_name='top_skills_2020_img',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2020_data',
            new_name='top_skills_2020_table',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2021_chart',
            new_name='top_skills_2021_img',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2021_data',
            new_name='top_skills_2021_table',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2022_chart',
            new_name='top_skills_2022_img',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2022_data',
            new_name='top_skills_2022_table',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2023_chart',
            new_name='top_skills_2023_img',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2023_data',
            new_name='top_skills_2023_table',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2024_chart',
            new_name='top_skills_2024_img',
        ),
        migrations.RenameField(
            model_name='skills_statistics',
            old_name='top_skills_2024_data',
            new_name='top_skills_2024_table',
        ),
        migrations.RemoveField(
            model_name='main_statistics',
            name='vacancy_chart',
        ),
        migrations.RemoveField(
            model_name='main_statistics',
            name='vacancy_data',
        ),
        migrations.AddField(
            model_name='main_statistics',
            name='vacancy_img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='График Динамика количества вакансий по годам '),
        ),
        migrations.AddField(
            model_name='main_statistics',
            name='vacancy_table',
            field=models.TextField(blank=True, verbose_name='Таблица Динамика количества вакансий по годам '),
        ),
    ]
