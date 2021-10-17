import pandas as pd
import numpy as np
from dataclasses import make_dataclass

#second solution with diversification of dtypes
base1 = make_dataclass("base1", [("name", 'string'), ("surname", 'string'), ("age", int), ("sex", 'string')])
df = pd.DataFrame([base1("Jan", "Kowalksi", 25, "male"), base1("John", "Black", 69, "male"), base1("Jane", "Red", 12, "female"),
                   base1("Ruby", "Pot", 34, "female"), base1("Aaron", "Schmit", 21, "male")])

#first solution- without specification of dtypes
#df = pd.DataFrame(columns= ["name", "surname", "age", "sex"])
#df = df.append({"name": "Jan", "surname": "Kowalski", "age": 25, "sex": "male"}, ignore_index = True)
#df = df.append({"name": "John", "surname": "Black", "age": 69, "sex": "male"}, ignore_index = True)
#df = df.append({"name": "Jane", "surname": "Red", "age": 12, "sex": "female"}, ignore_index = True)
#df = df.append({"name": "Ruby", "surname": "Pot", "age": 34, "sex": "female"}, ignore_index = True)
#df = df.append({"name": "Aaron", "surname": "Schmit", "age": 21, "sex": "male"}, ignore_index = True)
print("----dataframe:")
print (df)

print("----panda.info:")
df.info()

print("----pandas.describe:")
print(df.describe(include='all'))

print("----pandas.head:")
print(df.head(3))
