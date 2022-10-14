import pandas as pd
import matplotlib.pyplot as plotlib
from sklearn.linear_model import LinearRegression

data = pd.read_csv('cost_revenue_clean.csv')

data.describe()

# Assigning list data to variables
x = pd.DataFrame(data, columns=['production_budget_usd'])
y = pd.DataFrame(data, columns=['worldwide_gross_usd'])



regression = LinearRegression()

regression.fit(x,y)

regression.coef_  # slope cofficient  theta-1

regression.intercept_ # theta

print(f"{regression.coef_} , {regression.intercept_}" )


regression.score(x,y) # Goodness of fit r^2
print(regression.score(x,y))

plotlib.figure(figsize=(20,12 ))
plotlib.scatter(x,y,alpha=0.3)

#to plot line

plotlib.plot(x.values,regression.predict(x.values), color='red')
plotlib.title('Film Cost vs Global Revinue')
plotlib.xlabel('production budget')
plotlib.ylabel('gross budget')

plotlib.show()





