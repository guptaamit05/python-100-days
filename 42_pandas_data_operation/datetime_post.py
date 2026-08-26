import pandas as pd
import datetime
import matplotlib.pyplot as plt



df = pd.read_csv('./sample_data/QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
print(df.shape)

columns = df.columns
# print(columns)
# print(df.head())
# print(df.tail())


# print(df.shape)

# print(df.count())# count each column count

sum_of_all_posts = df.groupby('TAG').sum()
# print(sum_of_all_posts)


df['DATE'] = pd.to_datetime(df['DATE'])
print(df.head())

# pd.to_datetime()


reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df)

print(reshaped_df.shape)


print('-------------------------HEAD--------------------')
print(reshaped_df.head())

print('==============TAIL-==================')
print(reshaped_df.tail())

print(reshaped_df.columns)

reshaped_df.fillna(0, inplace=True)

print(reshaped_df.shape)
print("Max = ", reshaped_df.count().idxmin())
print("Min = ", reshaped_df.count().idxmax())
print("===================")

print(reshaped_df.head())

## check if any nan value still exist..
print(reshaped_df.isna().values.any())


print(plt.plot(reshaped_df.index, reshaped_df['java']))