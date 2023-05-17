from pathlib import Path
import pandas as pd

DATA_FOLDER = Path("./tmd_conference/_data")

program = pd.read_excel("program.xlsx", sheet_name=None)

print("Loaded program:")

print(program)

for day, schedule in program.items():
    file = DATA_FOLDER / f'{day}_program.csv'
    print("Creating", file)
    schedule.to_csv(file)
    
    