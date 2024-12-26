import numpy as np
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
import matplotlib.pyplot as plt

def add_missed_year(df_):
    if df_.index.name != "year": return df_
    return df_.reindex(range(2007, 2023), fill_value=0)

def get_salaries(v: DataFrame, column: str) -> dict[str, int]:
    return (v
            .assign(salary=lambda df_: df_[['salary_from', 'salary_to']].mean(axis=1))
            [[column, 'salary']]
            .groupby(column)
            .agg('mean')
            .round()
            .fillna(0)
            .astype(int)
            .pipe(add_missed_year)
            .to_dict('dict')['salary'])

def get_vacancy_count(v: DataFrame, column: str) -> dict[str, int]:
    return (v
            .groupby(column)
            .count()
            .pipe(add_missed_year)
            .to_dict('dict')['name'])

def get_statistics(vacancies: DataFrame, profession: DataFrame) -> (dict[str, int],dict[str, int],
                                                                    dict[str, int],dict[str, int],
                                                                    dict[str, int],dict[str, int]):
    salaries_by_years = get_salaries(vacancies, 'year') # Динамика уровня зарплат по годам
    vacancies_count_by_years = get_vacancy_count(vacancies, 'year') # Динамика количества вакансий по годам
    profession_salaries_by_years = get_salaries(profession, 'year') # Динамика уровня зарплат по годам для выбранной профессии
    profession_vacancies_count_by_years = get_vacancy_count(profession, 'year') # Динамика количества вакансий по годам для выбранной профессии

    temp_vacancies_per_city = get_vacancy_count(vacancies, 'area_name') # получить словарь долей вакансий по городам
    temp_vacancies_count = sum(temp_vacancies_per_city.values())
    temp_vacancies_ratio_by_city = {k: round(float(temp_vacancies_per_city[k]) / temp_vacancies_count, 4) * 100 for k in
                 temp_vacancies_per_city} # %

    temp_salaries_by_cities = dict((k, v) for k,v in get_salaries(vacancies, 'area_name').items()
                                   if temp_vacancies_ratio_by_city[k] > 1) # убираем города в которых <1% вакансий
    salaries_by_cities = dict(sorted(temp_salaries_by_cities.items(), key=lambda i: i[1], reverse=True)[:10]) # Уровень зарплат по городам (в порядке убывания)
    vacancies_count_by_cities = dict(sorted(temp_vacancies_ratio_by_city.items(), key=lambda i:(-i[1], i[0]))[:10]) # Доля вакансий по городам (в порядке убывания)
    other_cities = sum(dict(sorted(temp_vacancies_ratio_by_city.items(), key=lambda i:(-i[1], i[0]))[10:]).values()) # TODO это жестко    Все остальные города кладем в Другие
    vacancies_count_by_cities['Другие'] = other_cities

    return (salaries_by_years,vacancies_count_by_years,
            profession_salaries_by_years,profession_vacancies_count_by_years,
            salaries_by_cities,vacancies_count_by_cities)

def get_statistic(csv: str, vac_name: str):
    vacancies = pd.read_csv(csv) # header=None
    # vacancies.columns = ['name', 'salary_from', 'salary_to', 'salary_currency', 'area_name', 'published_at']
    vacancies = (vacancies
                 .assign(year=vacancies['published_at'].str.split('-').str.get(0).astype(int))
                 .query('2007 <= year <= 2022')
                 )
    profession = vacancies[vacancies['name'].str.contains(vac_name, case=False, na=False)]
    return get_statistics(vacancies, profession)

def salaries_by_years_plot(ax, sy: dict[str, int], psy: dict[str, int], vac: str):
    x = np.arange(len(sy.keys()))
    ax.bar(x=x, height=sy.values(), width=-0.2, align='edge', label='средняя з/п')
    ax.bar(x=x, height=psy.values(), width=0.2, align='edge', label=f'з/п {vac}')
    ax.set_xticks(x, labels=sy.keys())
    ax.tick_params(axis='x', rotation=90, labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_title('Уровень зарплат по годам', fontsize=8)
    ax.legend(loc='upper left', labels=['средняя з/п', f'з/п {vac}'], fontsize=8)
    ax.grid(axis='y')

def vacancies_count_by_years_plot(ax, vcy: dict[str, int], pvcy: dict[str, int], vac: str):
    x = np.arange(len(vcy.keys()))
    ax.bar(x=x, height=vcy.values(), width=-0.2, align='edge', label='Количество вакансий')
    ax.bar(x=x, height=pvcy.values(), width=0.2, align='edge', label=f'Количество вакансий\n{vac}')
    ax.set_xticks(x, labels=vcy.keys())
    ax.tick_params(axis='x', rotation=90, labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_title('Количество вакансий по годам', fontsize=8)
    ax.legend(loc='upper left', labels=['Количество вакансий', f'Количество вакансий\n{vac}'], fontsize=8)
    ax.grid(axis='y')

def salaries_by_cities_plot(ax, sc: dict[str,int]):
    ax.barh(sc.keys(), sc.values())
    ax.invert_yaxis()
    ax.set_title('Уровень зарплат по городам', fontsize=8)
    ax.tick_params(axis='y', labelsize=6)
    ax.tick_params(axis='x', labelsize=8)
    ax.grid(axis='x')
    for label in ax.get_yticklabels():
        label.set_ha('right')
        label.set_va('center')

def vacancies_count_by_cities_plot(ax, vcc: dict[str, int]):
    ax.pie(vcc.values(), labels=vcc.keys(), textprops={'fontsize': 6})
    ax.set_title('Доля вакансий по городам', fontsize=8)

def create_plot():
    csv = '../data/vacancies_2024.csv'
    vac = input()
    sy, vcy, psy, pvcy, sc, vcc = get_statistic(csv, vac)

    fig, sub = plt.subplots(2, 2)
    salaries_by_years_plot(sub[0,0],sy,psy,vac)
    vacancies_count_by_years_plot(sub[0,1],vcy,pvcy,vac)
    salaries_by_cities_plot(sub[1,0],sc)
    vacancies_count_by_cities_plot(sub[1,1],vcc)
    plt.show()

    return sub

create_plot()