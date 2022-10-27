import matplotlib.pyplot as plt
import numpy as np


# f(x) = x^2 + x + 1


def fun(x):
    return x**2 + x + 1 # a simple cost function


#generating data with numpy

data = np.linspace( start= -3, stop=3,num=100)
print(data)


#Slop and derevative to finde minimum value of cf

def derevative(x):
    return 2*x + 1;

# ploting data
# ploting data




#Gradient Descent

#Gradient Descent
new_x = 3  #random guess
previous_x =  0
step_multiplier = 0.1 #gamma
precision = 0.0001

x_list = [new_x]
slope_list = [derevative(new_x)]


for n in range(300) :
    previous_x = new_x
    gradient = derevative(previous_x)
    new_x = previous_x - step_multiplier*gradient



    x_list.append(new_x)
    slope_list.append(derevative(new_x))



    step_size = abs( new_x - previous_x)

    if step_size < precision:
        break





print(f"Local minimum occurs at:{new_x}")
print(f"slope or df(x) at this point is :{derevative(new_x)}")
print(f"f(x) or cost function is:{fun(new_x)}")



plt.figure(figsize=[10,5])

plt.subplot(1,2,1) #dividing graph

plt.title('Gradient Descent')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(data, fun(data))

x_value = np.array(x_list)
plt.scatter(x_list,fun(x_value),color='red')


plt.subplot(1,2,2)
plt.title('Slope of Cost Function')
plt.xlabel('x')
plt.ylabel('df(x)')
plt.grid()
plt.plot(data, derevative(data))
plt.scatter(x_list,slope_list,color='red')

plt.show()