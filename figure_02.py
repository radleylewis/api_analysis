import pandas as pd
import matplotlib.pyplot as plt

title = 'Figure 2: API Call Sequence Length (Binned)'
df = pd.read_csv('remaining_behavior_ext.csv', sep=',\s*', engine='python')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]  # Drop unnamed columns

# Create bins for sequence length
bins = [0, 10, 20, 30, 40, 50, 100, 200, 500, 1000, float('inf')]
labels = ['1-10', '11-20', '21-30', '31-40', '41-50', '51-100', '101-200', '201-500', '501-1000', '1000+']
df['sequence_length_binned'] = pd.cut(df['sequence_length(count)'], bins=bins, labels=labels)

# Prepare data
counts = df['sequence_length_binned'].value_counts().sort_index()
explode = [0.02] * len(counts)  # Small gap for each slice

# Plot pie chart
plt.figure(figsize=(10, 6))
counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    ylabel='',
    explode=explode,
    textprops={'fontsize': 12}
)

# Formatting
plt.title(title, fontsize=14, fontweight='bold', pad=20)
plt.subplots_adjust(bottom=0.25)
plt.tight_layout()
plt.savefig('figure_2.png')
plt.show()

