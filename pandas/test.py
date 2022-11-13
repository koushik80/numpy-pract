import pandas as pd

# data = {
# "calories": [420, 380, 390],
# "duration": [50, 40, 45]
# }

# load data into a DataFrame object:
#df = pd.DataFrame(data)

# print(df)

import pandas as pd

animals = ['Cat', 'Dog', 'Bird', 'Rabit', 'Duck', 'Cow', 'Tiger', 'Lion']

animal_list = pd.Series(animals)

print(animal_list)
