import pandas as pd
import matplotlib.pyplot as plt

title="Figure 4: Number of Sessions (Binned)"

# Load the dataset
df = pd.read_csv('remaining_behavior_ext.csv', sep=',\s*', engine='python')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]  # Drop unnamed columns

# Create bins for number of sessions
session_bins = [0, 5, 10, 20, 50, 100, float('inf')]
session_labels = ['1-5', '6-10', '11-20', '21-50', '51-100', '100+']
df['num_sessions_binned'] = pd.cut(df['num_sessions'], bins=session_bins, labels=session_labels)

# Prepare data
counts = df['num_sessions_binned'].value_counts().sort_index()
explode = [0.02] * len(counts)  # Add small gaps between slices

# Plot pie chart
plt.figure(figsize=(10, 6))
counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    explode=explode,
    ylabel='',
    textprops={'fontsize': 12}
)

# Formatting
plt.title(title, fontsize=18, fontweight='bold', pad=20)
plt.subplots_adjust(bottom=0.25)
plt.tight_layout()
plt.show()

plt.savefig('figure_4.png')
