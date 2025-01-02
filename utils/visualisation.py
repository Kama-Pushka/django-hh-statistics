import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from textwrap import wrap

import statistics

def salaries_by_years_plot(ax, sy: Series, psy: Series, vac: str):
    x = np.arange(len(sy.index))
    ax.bar(x=x, height=sy, label='средняя з/п') #  width=-0.2, align='edge',
    # ax.bar(x=x, height=psy, width=0.2, align='edge', label=f'з/п {vac}')
    ax.set_xticks(x, labels=sy.index)
    ax.tick_params(axis='x', rotation=90, labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_title('Уровень зарплат по годам', fontsize=8)
    ax.legend(loc='upper left', labels=['средняя з/п'], fontsize=8) # f'з/п {vac}'
    ax.grid(axis='y')

def vacancies_count_by_years_plot(ax, vcy: Series, pvcy: Series, vac: str):
    x = np.arange(len(vcy.index))
    ax.bar(x=x, height=vcy, label='Количество вакансий') # width=-0.2, align='edge',
    # ax.bar(x=x, height=pvcy, width=0.2, align='edge', label=f'Количество вакансий\n{vac}')
    ax.set_xticks(x, labels=vcy.index)
    ax.tick_params(axis='x', rotation=90, labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_title('Количество вакансий по годам', fontsize=8)
    ax.legend(loc='upper left', labels=['Количество вакансий'], fontsize=8) # f'Количество вакансий\n{vac}'
    ax.grid(axis='y')

def salaries_by_cities_plot(ax, sc: Series):
    ax.barh(sc.index, sc)
    ax.invert_yaxis()
    ax.set_title('Уровень зарплат по городам', fontsize=8)
    ax.tick_params(axis='y', labelsize=6)
    ax.tick_params(axis='x', labelsize=8)
    ax.grid(axis='x')
    for label in ax.get_yticklabels():
        label.set_ha('right')
        label.set_va('center')

def vacancies_count_by_cities_plot(ax, vcc: Series):
    ax.pie(vcc, labels=vcc.index, textprops={'fontsize': 6})
    ax.set_title('Доля вакансий по городам', fontsize=8)

def top_skills_plot(ts: DataFrame, name: str):
    # ts.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral'])
    # plt.title('Distribution of Categories')
    # plt.ylabel('')
    # plt.show()

    years = ts['year'].unique()
    for year in years:
        test = ts[ts['year'] == year]
        # test['key_skills_list'] = ['\n'.join(wrap(l, 15)) for l in test['key_skills_list']]

        fig, ax = plt.subplots(1, 1)
        ax.barh(y=test['key_skills_list'], width=test['count'])
        ax.invert_yaxis()
        ax.set_title(f'ТОП-20 навыков в {year} году', fontsize=8)
        ax.tick_params(axis='y', labelsize=6, )
        ax.tick_params(axis='x', labelsize=8)
        ax.grid(axis='x')
        for label in ax.get_yticklabels():
            label.set_ha('right')
            label.set_va('center')

        fig.savefig(f'{name} {year}.png')
        plt.show()

def create_plots():
    csv = '../data/vacancies_2024.csv'
    vac = input("Введите наименования профессии (через запятую):").split(', ') # ('c#', 'c sharp', 'шарп', 'с#')  |  c#, c sharp, шарп, с#
    sy, vcy, sc, vcc, psy, pvcy, psc, pvcc, ts, pts = statistics.get_statistics(csv, vac)

    ## Общая статистика
    fig, sub = plt.subplots(1, 1)
    salaries_by_years_plot(sub,sy,psy,vac[0]) # TODO vac[0]?
    plt.show()

    fig, sub = plt.subplots(1, 1)
    vacancies_count_by_years_plot(sub,vcy,pvcy,vac[0]) # TODO vac[0]?
    plt.show()

    fig, sub = plt.subplots(1, 1)
    salaries_by_cities_plot(sub,sc)
    plt.show()

    fig, sub = plt.subplots(1, 1)
    vacancies_count_by_cities_plot(sub,vcc)
    plt.show()

    ## Востребованность
    fig, sub = plt.subplots(1, 1)
    salaries_by_years_plot(sub, psy, sy, vac[0])  # TODO vac[0]?
    plt.show()

    fig, sub = plt.subplots(1, 1)
    vacancies_count_by_years_plot(sub, pvcy, vcy, vac[0])  # TODO vac[0]?
    plt.show()

    ## География
    fig, sub = plt.subplots(1, 1)
    salaries_by_cities_plot(sub,psc)
    plt.show()

    fig, sub = plt.subplots(1, 1)
    vacancies_count_by_cities_plot(sub,pvcc)
    plt.show()

    ## Навыки
    print(ts.columns)
    top_skills_plot(ts, 'ТОП-20 навыков по годам')
    top_skills_plot(pts, 'ТОП-20 навыков по годам для выбранной профессии')

if __name__ == "__main__":
    create_plots()