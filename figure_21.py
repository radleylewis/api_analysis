import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
from scipy.stats import t

title = 'Figure 21: Predicting Unique APIs from Sessions (Bots Only)'

# Load and clean data
df = pd.read_csv('remaining_behavior_ext.csv')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
df = df.dropna(subset=['num_sessions', 'num_unique_apis', 'behavior_type'])

# Filter for bots only
df_bot = df[df['behavior_type'] == 'bot']
X = df_bot[['num_sessions']]
y = df_bot['num_unique_apis']

# Fit model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

# Predict for new values
new_sessions = pd.DataFrame({'num_sessions': [10, 50, 100, 200, 500]})
predicted_apis = model.predict(new_sessions.values)  # fix for feature name warning

# Print predictions
print("Predicted Unique APIs for given Sessions:")
for s, p in zip(new_sessions['num_sessions'], predicted_apis):
    print(f"  {s} sessions → {p:.2f} unique APIs")

# Confidence intervals (simple approximation, assuming constant variance)
n = len(X)
mean_x = X['num_sessions'].mean()
se = np.sqrt(np.sum((y - y_pred)**2) / (n - 2))  # standard error of regression
t_val = t.ppf(0.975, df=n - 2)

# Prediction range
x_range = np.linspace(X['num_sessions'].min(), X['num_sessions'].max(), 300).reshape(-1, 1)
y_range_pred = model.predict(x_range)
ci = t_val * se * np.sqrt(
    1 + (x_range.flatten() - mean_x)**2 / np.sum((X['num_sessions'] - mean_x)**2)
)

# Plot with confidence band
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, label='bot datapoints', color='orange')
plt.plot(x_range, y_range_pred, color='black', linewidth=2, label=f'Linear Regression (R² = {r2:.2f})')
plt.fill_between(x_range.flatten(),
                 y_range_pred - ci,
                 y_range_pred + ci,
                 color='gray', alpha=0.3, label='~95% Prediction Interval')

# Formatting
plt.xlabel('Number of Sessions', fontsize=14, labelpad=15)
plt.ylabel('Number of Unique APIs', fontsize=14, labelpad=15)
plt.title(title, fontsize=18, fontweight='bold', pad=20)
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=2, frameon=False, fontsize=12)
plt.subplots_adjust(bottom=0.3)
plt.tight_layout()
plt.show()
