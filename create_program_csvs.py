from pathlib import Path
import pandas as pd

DATA_FOLDER = Path("./tmd_conference/_data")
ABSTRACT_COLS = ['AbstractA', 'AbstractB', 'AbstractC', 'AbstractD']

program = pd.read_excel("program.xlsx", sheet_name=None)

print("Loaded program:")

print(program)

print("Adding extra newlines to abstracts")

for schedule in program.values():
    schedule.loc[:, ABSTRACT_COLS] = schedule.loc[:, ABSTRACT_COLS].replace('\n([^\n])', '\n\\1', regex=True)

for day, schedule in program.items():
    file = DATA_FOLDER / f'{day}_program.csv'
    print("Creating", file)
    schedule.to_csv(file)
    
    