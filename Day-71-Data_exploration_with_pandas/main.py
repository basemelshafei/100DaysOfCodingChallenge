import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
df.head()
df.tail()

df['spread_col'] = df['Mid-Career 90th Percentile Salary'] - df['Mid-Career 10th Percentile Salary']

spread_col = df['Mid-Career 90th Percentile Salary'] - df['Mid-Career 10th Percentile Salary']

low_risk = df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

highest_potential = df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

highest_spread = df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

df.groupby('Group').count()

pd.options.display.float_format = '{:,.2f}'.format