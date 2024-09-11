#before running this program on your system, ensure that you have access to UC Irvine's dataset handler:
#
#on cmd line run >> pip install ucimlrepo

from ucimlrepo import fetch_ucirepo 
import pandas
import matplotlib.pyplot as pyplot

# fetch dataset 
print("Retrieving dataset...")
adult = fetch_ucirepo(id=2) 
print("Dataset retrieved.")

# data (as pandas dataframes) 
X = adult.data.features 
y = adult.data.targets 

# variable information, also available on the webpage: https://archive.ics.uci.edu/dataset/2/adult
print(adult.variables) 

#isolate, combine, and graph two of the values
age = pandas.DataFrame(X.loc[:,"age"])
hpw = pandas.DataFrame(X.loc[:,"hours-per-week"])
age.insert(1, "hours-per-week", hpw)
age.plot.scatter(x="age",y="hours-per-week")
#pyplot.show()


#data cleaning example: remove those who work less than full time or are unemployed, and limit our search to the U.S.
df = pandas.DataFrame(X)
df.dropna()
#remove the unemployed
df = df.drop(df[df['workclass'] == 'Never-worked'].index)
#purge the sloths
df = df.drop(df[df['hours-per-week'] >= 40].index)
#enforce the borders
selection = df['native-country'] == 'United-States'
df = df[selection]
subselection = df[['age', 'hours-per-week']]
subselection.plot.scatter(x="age",y="hours-per-week")
pyplot.show()
