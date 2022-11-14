import pandas as pd

# data = {
# "calories": [420, 380, 390],
# "duration": [50, 40, 45]
# }

# load data into a DataFrame object:
#df = pd.DataFrame(data)

# print(df)

import pandas as pd
import numpy as np

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

x = pd.DataFrame(np.random.randn(
    10, 5), index='row1 row2 row3 row4 row5 row6 row7 row8 row9 row10'. split(),
    columns='column1 column2 column3 column4 column5'.split())
print(x['column3'])
print(x[['column3', 'column4', 'column5']])  # selecting multiple columns
print(x.loc[['row4', 'row3', 'row5']])  # selecting multiple rows
print()
print(x.iloc[6])
