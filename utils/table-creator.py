import pandas as pd

csv = pd.read_csv('../data/ТОП-20 навыков по годам для выбранной профессии.csv')
if len(csv.columns)==3:
    HEAD = """<table class="block_style_wrapper">
        <thead class="table-head"">
            <tr>
                <th>Навык</th>
                <th>Упоминания</th>
            </tr>
        </thead>
        <tbody class="table-body">"""

    year = -1
    TABLE = ""
    for i, row in csv.iterrows():
        if year != row.iloc[0]:
            TABLE += """
    </tbody>
</table>"""
            print(TABLE)

            TABLE = HEAD
            year = row.iloc[0]
            print(year)
        TABLE += f"""
            <tr>
                <td>{row.iloc[1]}</td>
                <td>{row.iloc[2]}</td>
            </tr>"""
    else:
        TABLE += """
    </tbody>
</table>"""
        print(TABLE)
else:
    TABLE = """<table class="block_style_wrapper">
        <thead class="table-head"">
            <tr>
                <th>Город</th>
                <th>Доля</th>
            </tr>
        </thead>
        <tbody class="table-body">"""

    for i, row in csv.iterrows():
        TABLE += f"""
            <tr>
                <td>{row.iloc[0]}</td>
                <td>{row.iloc[1]}</td>
            </tr>"""

    TABLE += """
    </tbody>
</table>"""

    print(TABLE)