import time
import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame

_MIN_YEAR = 2000
_MAX_YEAR = 2024
_df_currency = pd.read_csv('../data/valutes.csv', index_col='date')

def _convert_to_rubles(df_):
    if df_['salary_currency'] != 'RUR' and df_['salary_currency'] is not np.nan:
        date = '-'.join(df_['published_at'].split('-')[:2])
        df_['salary'] = df_['salary'] * _df_currency.loc[date, df_['salary_currency']]
    return df_

def _add_missed_year(df_):
    if df_.index.name != "year": return df_
    return df_.reindex(range(_MIN_YEAR, _MAX_YEAR + 1), fill_value=0)

def _get_salaries(v: DataFrame, column: str) -> Series:
    return (v
            .assign(salary=lambda df_: df_[['salary_from', 'salary_to']].mean(axis=1))
            .apply(_convert_to_rubles, axis=1)
            [[column, 'salary']]
            .query('salary < 10_000_000')
            .groupby(column)
            .agg('mean')
            .round()
            .fillna(0)
            .astype(int)
            .pipe(_add_missed_year)['salary'])

def _get_vacancy_count(v: DataFrame, column: str) -> Series:
    return (v
            .groupby(column)
            .count()
            .pipe(_add_missed_year)['name'])

def get_main_stat(vacancies: DataFrame) -> (Series, Series, Series, Series):
    ## Общая статистика
    salaries_by_years = _get_salaries(vacancies, 'year')  # Динамика уровня зарплат по годам
    vacancies_count_by_years = _get_vacancy_count(vacancies, 'year')  # Динамика количества вакансий по годам

    temp_vacancies_per_city = _get_vacancy_count(vacancies, 'area_name')  # получить словарь долей вакансий по городам
    temp_vacancies_count = temp_vacancies_per_city.sum()
    temp_vacancies_ratio_by_city = round(temp_vacancies_per_city / temp_vacancies_count, 4) * 100 # %
    temp_vacancies_ratio_by_city = temp_vacancies_ratio_by_city[temp_vacancies_ratio_by_city > 1] # убираем города в которых <1% вакансий
    vacancies_count_by_cities = (temp_vacancies_ratio_by_city.sort_values(ascending=False)
                                 .head(10)) # Доля вакансий по городам (в порядке убывания)
    other_cities = 100 - vacancies_count_by_cities.sum()
    vacancies_count_by_cities['Другие'] = other_cities # Все остальные города кладем в Другие

    temp_salaries_by_cities = _get_salaries(vacancies, 'area_name')
    temp_salaries_by_cities = temp_salaries_by_cities[temp_salaries_by_cities.index.isin(temp_vacancies_ratio_by_city.index)]
    salaries_by_cities = (temp_salaries_by_cities.sort_values(ascending=False)
                          .head(10)) # Уровень зарплат по городам (в порядке убывания)

    return (salaries_by_years,vacancies_count_by_years,
            salaries_by_cities, vacancies_count_by_cities)

def get_relevance_of_profession_stat(profession: DataFrame) -> (Series, Series):
    ## Востребованность
    profession_salaries_by_years = _get_salaries(profession,
                                                'year')  # Динамика уровня зарплат по годам для выбранной профессии
    profession_vacancies_count_by_years = _get_vacancy_count(profession,
                                                            'year')  # Динамика количества вакансий по годам для выбранной профессии

    return profession_salaries_by_years, profession_vacancies_count_by_years

def get_geographic_stat(profession: DataFrame) -> (Series, Series):
    ## География
    temp_vacancies_per_city = _get_vacancy_count(profession, 'area_name')  # получить словарь долей вакансий по городам
    temp_vacancies_count = temp_vacancies_per_city.sum()
    temp_vacancies_ratio_by_city = round(temp_vacancies_per_city / temp_vacancies_count, 4) * 100  # %
    temp_vacancies_ratio_by_city = temp_vacancies_ratio_by_city[
        temp_vacancies_ratio_by_city > 1]  # убираем города в которых <1% вакансий
    profession_vacancies_count_by_cities = (temp_vacancies_ratio_by_city.sort_values(ascending=False)
                                 .head(10))  # Доля вакансий по городам для выбранной профессии (в порядке убывания)
    other_cities = 100 - profession_vacancies_count_by_cities.sum()
    profession_vacancies_count_by_cities['Другие'] = other_cities  # Все остальные города кладем в Другие

    temp_salaries_by_cities = _get_salaries(profession, 'area_name')
    temp_salaries_by_cities = temp_salaries_by_cities[
        temp_salaries_by_cities.index.isin(temp_vacancies_ratio_by_city.index)]
    profession_salaries_by_cities = (temp_salaries_by_cities.sort_values(ascending=False)
                          .head(10))  # Уровень зарплат по городам для выбранной профессии (в порядке убывания)

    return profession_salaries_by_cities, profession_vacancies_count_by_cities

def get_top_skills(df_: DataFrame, num: int) -> Series:
    return (df_.assign(key_skills_list=df_['key_skills'].str.split('\n'))
             .explode('key_skills_list')
             .groupby('year')
             ['key_skills_list']
             .value_counts()
             .groupby(level=0, group_keys=False)
             .head(num))

def get_statistics(csv: str, vac_names: list) -> (Series, Series, Series, Series,
                                                  Series, Series,
                                                  Series, Series,
                                                  Series, Series):
    global _MIN_YEAR, _MAX_YEAR
    start_time = time.time()

    vacancies = pd.read_csv(csv) # header=None
    # vacancies.columns = ['name', 'salary_from', 'salary_to', 'salary_currency', 'area_name', 'published_at']
    vacancies = (vacancies
                 .assign(year=vacancies['published_at'].str.split('-').str.get(0).astype(int))
                 # .query('2007 <= year <= 2022')
                 )
    _MIN_YEAR = vacancies['year'].min()
    _MAX_YEAR = vacancies['year'].max()
    print("LOG:", _MIN_YEAR, _MAX_YEAR)
    print("LOG:", vacancies['salary_currency'].unique())

    profession = vacancies[vacancies['name'].str.contains('|'.join(vac_names), case=False, na=False)]

    main_stat = get_main_stat(vacancies)
    main_stat[0].to_csv('Динамика уровня зарплат по годам.csv')
    main_stat[1].to_csv('Динамика количества вакансий по годам.csv')
    main_stat[2].to_csv('Уровень зарплат по городам (в порядке убывания).csv')
    main_stat[3].to_csv('Доля вакансий по городам (в порядке убывания).csv')
    print(main_stat[0], main_stat[1], main_stat[2], main_stat[3], sep='\n')
    ###
    relevance_of_profession_stat = get_relevance_of_profession_stat(profession)
    relevance_of_profession_stat[0].to_csv('Динамика уровня зарплат по годам для выбранной профессии.csv')
    relevance_of_profession_stat[1].to_csv('Динамика количества вакансий по годам для выбранной профессии.csv')
    print(relevance_of_profession_stat[0], relevance_of_profession_stat[1], sep='\n')
    ###
    geographic_stat = get_geographic_stat(profession)
    geographic_stat[0].to_csv('Уровень зарплат по городам для выбранной профессии (в порядке убывания).csv')
    geographic_stat[1].to_csv('Доля вакансий по городам для выбранной профессии (в порядке убывания).csv')
    print(geographic_stat[0], geographic_stat[1], sep='\n')
    ###
    top_skills = get_top_skills(vacancies, 20)
    profession_top_skills = get_top_skills(profession, 20)
    top_skills.to_csv('ТОП-20 навыков по годам.csv') # TODO переписать под отдельные файлы?
    profession_top_skills.to_csv('ТОП-20 навыков по годам для выбранной профессии.csv')
    print(top_skills, profession_top_skills, sep='\n')

    top_skills = pd.read_csv('ТОП-20 навыков по годам.csv')
    profession_top_skills = pd.read_csv('ТОП-20 навыков по годам для выбранной профессии.csv')

    end_time = time.time()
    print(f"Функция {get_statistics.__name__} выполнялась {end_time - start_time:.2f} секунд")

    return (*main_stat,
            *relevance_of_profession_stat,
            *geographic_stat,
            top_skills, profession_top_skills)

if __name__ == "__main__":
    csv = '../data/vacancies_2024.csv'
    vac = input("Введите наименования профессии (через запятую):").split(
        ', ')  # ('c#', 'c sharp', 'шарп', 'с#')  |  c#, c sharp, шарп, с#