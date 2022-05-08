import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
# print(df)
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.count())

grouped = df.groupby('TAG')
grouped_count = df.groupby('TAG').count()
group_sum = df.groupby('TAG').sum()
group_max = df.groupby('TAG').sum().max()
group_max_index = df.groupby('TAG').sum().idxmax()
print(grouped)
print(grouped_count)
print(group_sum)
print(group_max)
print(group_max_index)

df.DATE = pd.to_datetime(df.DATE)
print(df)

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df)
print(reshaped_df.shape)
print(reshaped_df.head())
print(reshaped_df.columns)
print(reshaped_df['python'][10])
print(reshaped_df.count())

print(reshaped_df.fillna(0, inplace=True))
print(reshaped_df.isna().values.any())

plt.figure(figsize=(16, 10))
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of posts', fontsize=14)
plt.ylim(0, 35000)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.plot(reshaped_df.index, reshaped_df.java)
plt.show()

plt.figure(figsize=(16, 10))
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of posts', fontsize=14)
plt.ylim(0, 35000)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)
plt.show()

for column in reshaped_df.columns:
    plt.figure(figsize=(16, 10))
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Number of posts', fontsize=14)
    plt.ylim(0, 35000)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3, label=reshaped_df[column].name)
    plt.show()

roll_df = reshaped_df.rolling(window=6).mean()
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
plt.show()





