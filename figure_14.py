import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from itertools import combinations
import numpy as np

# Load and clean data
df = pd.read_csv('remaining_behavior_ext.csv')

# Drop any columns starting with "Unnamed"
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]

# Select numeric columns only
numeric_cols = df.select_dtypes(include=[np.number]).columns
df_clean = df[numeric_cols].dropna()

df_normal = df[df['behavior_type'] == 'normal'].dropna(subset=['num_sessions', 'num_unique_apis'])

# Iterate over all combinations of numeric column pairs
for x_col, y_col in combinations(numeric_cols, 2):
    X = df_clean[[x_col]]
    y = df_clean[y_col]

    # Fit linear regression
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, alpha=0.6, label='Datapoint')
    plt.plot(X, y_pred, color='red', linewidth=2, label=f'Linear Regression (R² = {r2:.2f})')

    # Enhanced formatting
    plt.xlabel(x_col, fontsize=14, labelpad=15)
    plt.ylabel(y_col, fontsize=14, labelpad=15)
    plt.title(f'Linear Fit: {x_col} vs {y_col}', fontsize=18, fontweight='bold', pad=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.subplots_adjust(bottom=0.25)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=False, fontsize=14)

    plt.tight_layout()
    plt.show()
