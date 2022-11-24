import pandas as pd
import numpy as np

# data = {
# "calories": [420, 380, 390],
# "duration": [50, 40, 45]
# }

# load data into a DataFrame object:
#df = pd.DataFrame(data)

# print(df)


# -----------------Serries---------------
#animals = ['Cat', 'Dog', 'Bird', 'Rabit', 'Duck', 'Cow', 'Tiger', 'Lion']

#animal_list = pd.Series(animals)

# print(animal_list)

# ------------------

# --------------------
# courses = pd.Series(['React', 'Node', 'Python', 'NumPy', 'Pandas'], index=[
#    'Day1', 'Day2', 'Day3', 'Day4', 'Day5'])
# print(courses)

#days = pd.Series(['Day1', 'Day2', 'Day3', 'Day4', 'Day5'])
# print(days)

#week_day = pd.Series(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
# print(week_day)

# course_schedule = pd.Series(['React', 'Node', 'Python', 'NumPy', 'Pandas'], index=[
#    'Day1', 'Day2', 'Day3', 'Day4', 'Day5'])
# print(course_schedule)

#complete_schedule = courses + ' ' + week_day
# print(complete_schedule)
# ----------------


# --------loc & iloc--------

# sports = {'Football': 'Spain',
# 'NBA': 'USA',
# 'Cricket': 'India',
# 'Athelets': 'Jamaica'}

#sports_series = pd.Series(sports)
# print(sports_series)
# print(sports_series.loc['Cricket'])
# print(sports_series.iloc[3])

# -------------DataFrame-------------

# x = pd.DataFrame(np.random.randn(
# 10, 5), index='row1 row2 row3 row4 row5 row6 row7 row8 row9 row10'. split(),
# columns='column1 column2 column3 column4 column5'.split())
# print(x)
#y = type(x['column1'])
#z = type(x)
# print(y)
# print(z)


# -----------Selection And Indexing On Pandas-----------

# x = pd.DataFrame(np.random.randn(
# 10, 5), index='row1 row2 row3 row4 row5 row6 row7 row8 row9 row10'. split(),
# columns='column1 column2 column3 column4 column5'.split())
# print(x['column3'])
# print(x[['column3', 'column4', 'column5']])  # selecting multiple columns
# print(x.loc[['row4', 'row3', 'row5']])  # selecting multiple rows
# print()
# print(x.iloc[6])


# ------------Reading A Dataset Into Pandas DataFrame------------
# www.kaggle.com/nisargpatel/automobiles/data
# https://www.stats.govt.nz/large-datasets/csv-files-for-download/

#data = pd.read_csv('annual-enterprise-survey.csv')
# print(data)
# print(data.head(20))
# print(data.tail(20))

# -----------------Adding A Column To Pandas DataFrame-----------------

# x = pd.DataFrame(np.random.randn(
# 10, 5), index='row1 row2 row3 row4 row5 row6 row7 row8 row9 row10'. split(),
# columns='column1 column2 column3 column4 column5'.split())
#x['column6'] = x['column1']*5
# print(x)


# ------------Drop Columns And Rows In Pandas DataFrame-------------

# x = pd.DataFrame(np.random.randn(
# 10, 5), index='row1 row2 row3 row4 row5 row6 row7 row8 row9 row10'. split(),
# columns='column1 column2 column3 column4 column5'.split())
# use axis = 1 to refer to the column
# use inplace=True to make the changes affect
#print(x.drop('column2', axis=1, inplace=True))
# use axis = 0 to refer to the row
#print(x.drop('row3', axis=0, inplace=True))
# print(x.iloc[1])
#print(x.loc['row7', 'column2'])


# ------- Reset Index in Pandas DataFrame-------

# x = pd.DataFrame(np.random.randn(
# 10, 5), index='row1 row2 row3 row4 row5 row6 row7 row8 row9 row10'. split(),
# columns='column1 column2 column3 column4 column5'.split())
# print(x.index)
# y = x = pd.DataFrame(np.random.randn(
# 10, 5), index='row1 row2 row3 row4 row5 row6 row7 row8 row9 row10'. split(),
# columns='column1 column2 column3 column4 column5'.split())

#y['spin'] = ['sp1', 'sp2', 'sp3', 'sp4', 'sp5', 'sp6', 'sp7', 'sp8', 'sp9', 'sp10']
# print(y)

#z = y.set_index('spin', inplace=True)
# print(z)


# -----------rename column name------------
# r = x.rename(columns={'column1': 'first',
# 'column2': 'second',
# 'column3': 'third',
# 'column4': 'fourth',
# 'column5': 'fifth',
# 'column6': 'sixth'}, inplace=True)

# print(r)


# -----------Tail(), Column and Index------------

# data = pd.read_csv('annual-enterprise-survey.csv')
# print(data.index)
# print(data.columns)
# print(data.tail())


# -----------Check For Missing Values or Null Values(isnull() Vs Isna())---------

#data = pd.read_csv('annual-enterprise-survey.csv')
# print(data.isnull())
# print(data.isna())
# print(data.isnull().sum())

# --------------to deal with null values----------------
# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data)

# print(df)

# # Locate Row
# print(df.loc[0])
# print(df.loc[[0, 1]])

#df = pd.DataFrame(data, index=["day1", "day2", "day3"])

# print(df)
# print(df.loc["day2"])
# print(df.isnull())
# print(df.mean())

# Sort values
#print(df.sort_values(by='calories', ascending=True))
#print(df.sort_values(by='calories', ascending=False).head())


# ----Count() & Value_Count(), groupby(), conditional selection in the lecture and exercises


# -----------------Concatenate Function-------------------

# mm = {'one': [2, 3, 1, 4, 5],
#       'two': [5, 4, 3, 2, 1],
#       'letter': ['a', 'a', 'b', 'b', 'c']}

# m1 = pd.DataFrame(mm)
# print(m1)

# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index=["day1", "day2", "day3"])

# new_df = pd.concat([df, m1])
# new_df2 = pd.concat([df, m1], axis=1)
# print(new_df)
# print(new_df2)


# -----------------Join and Merge-------------------

# DataFrame of number of sales made by an employees

# sales = {
#     'Jones': 10000,
#     'Chris': 50000,
#     'Lari': 440,
#     'Rosa': 6700,
#     'Luna': 300
# }

# DataFrames of all employees and the region they work in

# region = {
#     'Jones': 'West',
#     'Chris': np.nan,
#     'Lari': 'West',
#     'Rosa': 'East',
#     'Luna': 'South',
#     'Kevin': 'West',
#     'Peter': 'East',
#     'James': np.nan,
#     'Karl': 'North'
# }

# covert dictionary to dataframes

# sales_df = pd.DataFrame.from_dict(sales, orient='index',
#                                   columns=['sales'])
# region_df = pd.DataFrame.from_dict(region, orient='index',
#                                    columns=['region'])

# print(sales_df)
# print(region_df)


# -----------------Join-------------------

# sales = {
#     'Jones': 10000,
#     'Chris': 50000,
#     'Lari': 440,
#     'Rosa': 6700,
#     'Luna': 300
# }

# region = {
#     'Jones': 'West',
#     'Chris': np.nan,
#     'Lari': 'West',
#     'Rosa': 'East',
#     'Jackson': 'South',
#     'Kevin': 'West',
#     'Peter': 'East',
#     'James': np.nan,
#     'Karl': 'North'
# }

# sales_df = pd.DataFrame.from_dict(sales, orient='index',
#                                   columns=['sales'])
# region_df = pd.DataFrame.from_dict(region, orient='index',
#                                    columns=['region'])
# --------here goes below the join formulas----------
#joined_df = region_df.join(sales_df, how='left')
# print(joined_df)

# joined_df = region_df.join(sales_df, how='right')
# print(joined_df)

# joined_df = region_df.join(sales_df, how='inner')
# print(joined_df)

# joined_df = region_df.join(sales_df, how='outer')
# print(joined_df)


# -----------------Merge-------------------

# give title to the index column
# sales_df.index.name = 'names'
# region_df.index.name = 'names'

# print(sales_df)
# print(region_df)
# print(pd.merge(region_df, sales_df, on='names'))
# print(pd.merge(region_df, sales_df, on='names', how='left'))
# print(pd.merge(region_df, sales_df, on='names', how='right'))
# print(pd.merge(region_df, sales_df, on='names', how='inner'))
# print(pd.merge(region_df, sales_df, on='names', how='outer'))


# ---------------------Cleaning Data--------------------

# -----------------Cleaning empty cells-------------------

# df = pd.read_csv('Automobile.csv')
# new_df = df.dropna()
# print(new_df.to_string())

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

# If want to change the original DataFrame, use the inplace = True argument:

# df = pd.read_csv('Automobile.csv')
# df.dropna(inplace=True)
# print(df.to_string())


#      --------replace empty values--------
# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

# The fillna() method allows us to replace empty cells with a value:

# df = pd.read_csv('data.csv')

# df.fillna(130, inplace=True)


# -----------Replace Only For Specified Columns--------------


# df = pd.read_csv('data.csv')

# df["Calories"].fillna(145)

# print(df)

# ----duplicate-----

# print(df.duplicated())
