import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from openpyxl.styles import Font, Border, Side

font_settings = Font(name='Calibri', bold=True)

border_settings = Border(
    left=Side(border_style='thin'),
    right=Side(border_style='thin'),
    top=Side(border_style='thin'),
    bottom=Side(border_style='thin'),
)

columns_name = [
    'name',
    'salary_from',
    'salary_to',
    'currency',
    'area_name',
    'published_at'
]

def create_plot():
    vac_name = input()
    df = prepare_dataframe(pd.read_csv('vacancies.csv', names=columns_name))
    fig, sub = plt.subplots(2, 2)
    plot_year_salaries(df, sub[0, 0], vac_name)
    plot_vacancy_counts(df, sub[0, 1], vac_name)
    plot_city_salaries(df, sub[1, 0])
    plot_city_percentages(df, sub[1, 1])
    plt.show()
    return sub

def plot_year_salaries(df, ax, vac_name):
    statistics = calculate_avg_salary_by_year(df)
    filtered_statistics = calculate_avg_salary_by_year(df[df['name'].str.contains(vac_name, case=False)])
    labels = statistics.keys()
    x = np.arange(len(labels))
    width = 0.2
    ax.bar(x, statistics.values(), width, label='Средняя з/п')
    ax.bar(x + width, filtered_statistics.values(), width, label='З/п программистов')
    ax.set_title('Уровень зарплат по годам', fontsize=8)
    ax.set_xticks(x + width / 2, labels=labels, rotation=90, fontsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.legend(loc='upper left', labels=['Средняя з/п', 'З/п программистов'], fontsize=8)
    ax.grid(axis='y')

def plot_vacancy_counts(df, ax, vac_name):
    stat = calculate_vacancies_by_year(df)
    stat_filtered = calculate_vacancies_by_year(df[df['name'].str.contains(vac_name, case=False)])
    labels = stat.keys()
    groups_labels = ['Количество вакансий', 'Количество вакансий\nпрограммистов']
    x = np.arange(len(labels))
    width = 0.2
    ax.bar(x, stat.values(), width, label=groups_labels[0])
    ax.bar(x + width, stat_filtered.values(), width, label=groups_labels[1])
    ax.set_title('Количество вакансий по годам', fontsize=8)
    ax.set_xticks(x + width / 2, labels=labels, rotation=90, fontsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.legend(loc='upper left', labels=groups_labels, fontsize=8)
    ax.grid(axis='y')

def plot_city_salaries(df, ax):
    stat = calculate_avg_salary_by_city(df)
    stat = {k if len(k.split()) == 1 else '\n'.join(k.split()): v for k, v in stat.items()}
    stat = {k if len(k.split('-')) == 1 else '\n'.join(k.split('-')): v for k, v in stat.items()}
    ax.invert_yaxis()
    ax.barh(stat.keys(), stat.values())
    ax.set_title('Уровень зарплат по городам', fontsize=8)
    ax.tick_params(axis='y', labelsize=6)
    ax.tick_params(axis='x', labelsize=8)
    for label in ax.get_yticklabels():
        label.set_ha('right')
        label.set_va('center')

def plot_city_percentages(df, ax):
    stat = calculate_vacancy_percentage_by_city(df)
    stat.update(calculate_vacancy_percentage_by_other_cities(df, stat.keys()))
    ax.pie(stat.values(), labels=stat.keys(), textprops={'fontsize': 6})
    ax.set_title('Доля вакансий по городам', fontsize=8)

def calculate_avg_salary_by_city(df):
    return (
        df.assign(average_salary=lambda x: (x['salary_from'] + x['salary_to']) / 2)
        .assign(percent=lambda x: (100 * x.groupby('area_name')['area_name'].transform('count') / len(x)).astype(int))
        .query('percent >= 1')
        .groupby('area_name')['average_salary']
        .mean()
        .apply(lambda x: round(x))
        .reset_index()
        .sort_values(by=['average_salary', 'area_name'], ascending=[False, True])
        .set_index('area_name')
        .head(10)
        .to_dict()['average_salary']
    )


def calculate_vacancy_percentage_by_other_cities(df, remove_cities):
    filtered = df.assign(percent=lambda x: (100 * x.groupby('area_name')['area_name'].transform('count') / len(x)).astype(int))
    return (
        filtered.loc[lambda x: ~x['area_name'].isin(remove_cities)]
        .assign(city_group='Другие')
        .assign(city_fraction='')
        .groupby('city_group')['city_fraction']
        .count()
        .apply(lambda x: 100 * round(x / len(filtered), 4))
        .to_dict()
    )

def calculate_vacancy_percentage_by_city(df):
    filtered = df.assign(percent=lambda x: (100 * x.groupby('area_name')['area_name'].transform('count') / len(x)).astype(int))
    return (
        filtered
        .assign(city_fraction='')
        .groupby('area_name')['city_fraction']
        .count()
        .apply(lambda x: 100 * round(x / len(filtered), 4))
        .reset_index()
        .sort_values(by=['city_fraction', 'area_name'], ascending=[False, True])
        .set_index('area_name')
        .head(10)
        .to_dict()['city_fraction']
    )

def calculate_avg_salary_by_year(df):
    return (
        df.assign(average_salary=lambda x: (x['salary_from'] + x['salary_to']) / 2)
        .groupby('year')['average_salary']
        .mean()
        .apply(lambda x: round(x))
        .reindex(range(2007, 2023), fill_value=0)
        .to_dict()
    )

def calculate_vacancies_by_year(df):
    return (
        df.assign(count='')
        .groupby('year')['count']
        .count()
        .reindex(range(2007, 2023), fill_value=0)
        .to_dict()
    )

def prepare_dataframe(df):
    return (
        df.assign(published_at=lambda x: pd.to_datetime(x['published_at'], utc=True))
        .assign(year=lambda x: x['published_at'].dt.year)
        .loc[lambda x: x['published_at'].dt.year <= 2022]
        .loc[lambda x: x['published_at'].dt.year >= 2007]
    )

create_plot()