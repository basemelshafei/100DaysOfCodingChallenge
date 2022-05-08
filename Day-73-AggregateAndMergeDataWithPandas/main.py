import img as img
import pandas as pd
import matplotlib.pyplot as plt

colors = pd.read_csv('LEGO Notebook and Data (start)/data/colors.csv')

print(colors)

print(colors['name'].nunique())

print(colors.groupby('is_trans').count())

sets = pd.read_csv('LEGO Notebook and Data (start)/data/sets.csv')

sets.sort_values('year', ascending=True)
print(sets)

sets_ordered_by_year = sets.groupby('year').value_counts()
print(sets_ordered_by_year.head())
print(sets['year'].nunique())

year_1949 = sets[sets['year'] == 1949]
print(year_1949)

sorted_by_num_parts = sets.sort_values('num_parts', ascending=False)
print(sorted_by_num_parts.head())
print(sets.loc[15004])

sets_by_year = sets.groupby('year').count()
print(sets_by_year['set_num'].head())

plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
plt.show()

themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id':'nr_themes'}, inplace=True)
print(themes_by_year)

plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
plt.show()


ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='r')

ax1.set_xlabel('year')
ax1.set_ylabel('NUmber of Sets', color='g')
ax2.set_ylabel('Number of Themes', color='r')
plt.show()

parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
parts_per_set.rename(columns={'num_parts': 'average_numparts'}, inplace=True)
print(parts_per_set.head())

plt.scatter(parts_per_set.index[:-2], parts_per_set.average_numparts[:-2])
plt.show()

themes = pd.read_csv('LEGO Notebook and Data (start)/data/themes.csv')

# <img src="https://i.imgur.com/Sg4lcjx.png">

#  linking primary key in themes to its corresponding foreign key in sets
themes[themes['name'] == 'Fire']
themes[themes['id'] == 18]

sets[sets['theme_id'] == 18]

set_theme_count = sets['theme_id'].value_counts()

set_theme_count = pd.DataFrame({'id': set_theme_count.index, 'set_count': set_theme_count.values})

merged_df = pd.merge(set_theme_count, themes, on='id')

plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()






