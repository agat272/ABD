#Agata Swatowska, zadanie 3- rysowanie wykresow funkcji x^2+5
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from dataclasses import make_dataclass

def function(x):
    return x**2+5

x1 = np.linspace(-1,1)
x2 = np.linspace(-6,6)
x3 = np.linspace(0,5)

fig, ax = plt.subplots(3,1)
fig.set_size_inches(6, 18)

y1 = function(x1)
ax[0].plot(x1, y1, label = 'x^2+5')
ax[0].set_ylabel("y")
ax[0].legend()
ax[0].set_title("wykres (-1, 1)")
ax[0].grid()

ax[1].plot(x2,function(x2), label = 'x^2+5')
ax[1].set_title("wykres (-6, 6)")
ax[1].set_ylabel("y")
ax[1].legend()
ax[1].grid()

ax[2].plot(x3,function(x3), label = 'x^2+5')
ax[2].set_title("wykres (0, 5)")
ax[2].set_ylabel("y")
ax[2].legend()
ax[2].grid()

plt.xlabel("x")
#plt.show()
fig.savefig("wyk1.jpg")


#zadanie 4--------------------------------------------

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
