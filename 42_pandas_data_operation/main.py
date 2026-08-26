import pandas as pd

pd.options.display.float_format = "{:,.2f}".format

df = pd.read_csv("./sample_data/salaries_by_college_major.csv")


# first 5 rows return...
col = df.head()


# rows and columns return..
# row_col = df.shape  # (51,6)
# rows = df.shape[0]  # 51 rows
# cols = df.shape[1]  # 6 columns

##
print(df.columns)  #  return columns
# print(len(df.columns))  # return No. of columns


# print(df.isna())
# print(df.tail())

#### Clear rows that has NaN
clean_df = df.dropna()
# print(len(clean_df))


##### What we learned here...
# df.head()
# df.columns
# df.shape
# df.isna()
# df.dropna()


# ==================Accessing Columns and individuals cell in a DafaFrame====================

# print(clean_df["Starting Median Salary"])

# max from a column
max_salary = clean_df["Starting Median Salary"].max()
# print(max_salary)

# min from a column
min_salary = clean_df["Starting Median Salary"].min()
# print(min_salary)


# Avg of a column.
avg_sal = clean_df["Starting Median Salary"].mean()
print("555555555555555555555555555", avg_sal)


# get row number of max element..
id_max = clean_df["Starting Median Salary"].idxmax()
# print(id_max)


# To see the value of 43 column having column: Undergraduate Major
# lo_id = clean_df["Undergraduate Major"].loc[id_max]
lo_id = clean_df["Undergraduate Major"][id_max]
# print(lo_id)


## get the entire row of : 43
# print(clean_df.loc[43])


#  get lowest starting salary row
# lowest_salary = clean_df["Starting Median Salary"].min()
# print(lowest_salary)
# id_of_lowest_salary = clean_df["Starting Median Salary"].idxmin()
# print(id_of_lowest_salary)  # 49

# print(clean_df.loc[id_of_lowest_salary])


##================ inlsert new Column and doing subtract, insert, sort_values)() functions


diff_two_col = clean_df["Mid-Career 90th Percentile Salary"].subtract(
    clean_df["Mid-Career 10th Percentile Salary"]
)


## Insert new Column...
clean_df.insert(1, "Diff_90_10_colmsn", diff_two_col)
## Sort the Values by new column in  DESC order...
print(clean_df.head().sort_values(by="Diff_90_10_colmsn", ascending=False))


top_5_Mid_Career_90th_Percentile_Salary = clean_df.sort_values(
    "Mid-Career 90th Percentile Salary", ascending=False
)
print(
    top_5_Mid_Career_90th_Percentile_Salary[
        ["Undergraduate Major", "Mid-Career 90th Percentile Salary"]
    ].head()
)


# group_by_groups = clean_df[["Group", "Undergraduate Major"]].groupby("Group").count()
# print("Groups==", group_by_groups)


mean_groups = clean_df.groupby("Group").mean
# print(mean_groups)
