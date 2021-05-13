from pyexcel import *
from pathlib import Path
path = Path('..', 'app', 'files', 'dit', 'file.xlsx')
records = get_records(file_name=f'{path}')

for r in records:
    print(f"{r['Номер']}, {r['Дата заявки']}, {r['Сумма']}, {r['Статус']}, {r['Получатель']}, {r['ДДС']}") 