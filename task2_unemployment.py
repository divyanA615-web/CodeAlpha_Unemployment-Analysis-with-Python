# ==========================================================================
# --- Task 2: Unemployment in India - EDA + COVID-19 Impact Analysis ---
# ==========================================================================

import pandas as pd # type: ignore
import numpy as np # type: ignore
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt # type: ignore
import matplotlib.patches as mpatches # type: ignore
import seaborn as sns # type: ignore
import warnings
warnings.filterwarnings('ignore')

# --- Load & Clean Data ---
u1 = pd.read_csv(r"D:\data science related\CodeAlpha_Internship\CodeAlpha_Unemployment-Analysis-with-Python\Unemployment_in_India.csv.csv")
u2 = pd.read_csv(r"D:\data science related\CodeAlpha_Internship\CodeAlpha_Unemployment-Analysis-with-Python\Unemployment_Rate_upto_11_2020.csv.csv")

#  Strip whitespace from column names
u1.columns = u1.columns.str.strip()
u2.columns = u2.columns.str.strip()

# --Rename for clarity--
col_map = {
    'Estimated Unemployment Rate (%)': 'UnempRate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'LPR',
    'Frequency': 'Freq',
    'Region.1': 'RegionGroup'
}
u1.rename(columns=col_map, inplace=True)
u2.rename(columns=col_map, inplace=True)

# Drop rows where the Date column is entirely missing
u1.dropna(subset=['Date'], inplace=True)
u2.dropna(subset=['Date'], inplace=True)

# Parse datas
u1['Date'] = pd.to_datetime(u1['Date'].str.strip(), format='%d-%m-%Y')
u2['Date'] = pd.to_datetime(u2['Date'].str.strip(), format='%d-%m-%Y')

print("== DATASET 1 (Unemployment_in_India) ==")
print(f"Shape: {u1.shape} | Date Range: {u1['Date'].min().date()} to {u1['Date'].max().date()}")
print(u1[['Region','Date','UnempRate','Area']].head(4))
print("\n== DATASET 2 (Unemployment_Rate_upto_11_2020) ==")
print(f"Shape: {u2.shape} | Date Range: {u2['Date'].min().date()} to {u2['Date'].max().date()}")
print(u2[['Region','Date','UnempRate','RegionGroup']].head(4))