# Assignment 2

This project reads daily weather observations for Edinburgh Castle and produces a summary report.

## Requirements

- Python 3.15 or later
- No third-party Python packages are required

## Input data

The program reads `edinburgh_castle.csv` from the project root. The CSV must contain these columns:

| Column | Description |
| --- | --- |
| `date` | Observation date |
| `max_temp_c` | Maximum temperature in degrees Celsius |
| `max_wind_mph` | Maximum wind speed in miles per hour |

## Run

From the project root, run:

```powershell
python src/castlecode/parta.py
```

The script first runs its built-in calculation checks, then prints the report in the terminal and saves it to `castle_report.txt` in the current working directory.

The report includes the date range, number of days, average maximum temperature and wind speed, and the dates when each maximum was recorded. When a maximum occurs on multiple days, the earliest date is reported.
