import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
files = ['Survey_2024_Spring.xlsx', 'Survey_2024_Autumn.xlsx']
data = [pd.read_excel(file, header=0).groupby(pd.read_excel(file, header=0).columns[5]).size() for file in files]

# Get unique categories from both datasets
unique_categories = sorted(set(data[0].index).union(set(data[1].index)))

# Define a color palette and map it to the categories
palette = sns.color_palette('Dark2', len(unique_categories))
color_dict = dict(zip(unique_categories, palette))


# Plot
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
for ax, data_set, file in zip(axes, data, files):
    sns.barplot(x=data_set.values, y=data_set.index, ax=ax, palette=[color_dict[category] for category in data_set.index])
    ax.set_title(f'{file}: {data_set.index.name}')
    ax.set_xlabel('Frequency')
    ax.set_ylabel(data_set.index.name)
    ax.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.show()