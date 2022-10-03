import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# READ DATA:
X = data.iloc[:,:-1].values
y = data.iloc[:, -1:].values


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)


# x = np.array(np.arange(1,11,0.5))

# Draw SCATTERPLOT OF TRAINING DATA:


# Draw SCATTERPLOT OF Testing DATA:
