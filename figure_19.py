import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

title = 'Figure 19: Sessions vs Unique APIs by Behavior Type'

# Load and clean data
df = pd.read_csv('remaining_behavior_ext.csv')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]  # Drop unnamed columns
df = df.dropna(subset=['num_sessions', 'num_unique_apis', 'behavior_type'])

X = df[['num_sessions']]
y = df['num_unique_apis']

# Fit model across all behavior types
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

# Plot
plt.figure(figsize=(10, 6))

# Scatterplot with color per behavior_type
for behavior_type, group in df.groupby('behavior_type'):
    plt.scatter(group['num_sessions'], group['num_unique_apis'],
                alpha=0.6, label=behavior_type)

# Linear regression line
plt.plot(X, y_pred, color='black', linewidth=2, label=f'Linear Regression (R² = {r2:.2f})')

# Formatting
plt.xlabel('Number of Sessions', fontsize=14, labelpad=15)
plt.ylabel('Number of Unique APIs', fontsize=14, labelpad=15)
plt.title(title, fontsize=18, fontweight='bold', pad=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.subplots_adjust(bottom=0.3)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=2, frameon=False, fontsize=12)

plt.tight_layout()
plt.show()

