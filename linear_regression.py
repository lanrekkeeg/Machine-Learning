import matplotlib.pyplot as plt
import sklearn as skt
import numpy as np
def calculate_theta_value(theta_0,theta_1, m, data_set):
    # dervative of slope
    theta_0_new = 0
    theta_1_new = 0
    for i in range(m):
        theta_0_new += ((theta_0+theta_1*data_set[i][0]) - data_set[i][1])
        theta_1_new += ((theta_0+theta_1*data_set[i][0]) - data_set[i][1])*data_set[i][0]

    return (theta_0_new/m,theta_1_new/m)

def gradient_descent():
    theta_0 = 0
    theta_1 = 0
    alpha = 0.09
    m = 0
    counter = 0
    list_0_gradient = []
    list_1_gradient= []
    theta_0_values = []
    theta_1_values = []
    # load data_set
    data_set = load_data_set("housing.txt","r")
    m = len(data_set)
    while True:
        theta_values = calculate_theta_value(theta_0,theta_1,m,data_set)
        print (theta_values[0],"-",theta_values[1])
        theta_0 -= alpha*theta_values[0]
        theta_1 -= alpha*theta_values[1]
        counter += 1
        list_0_gradient.append(abs(theta_values[0]))
        list_1_gradient.append(abs(theta_values[1]))
        theta_0_values.append(theta_0)
        theta_1_values.append(theta_1)
        var = abs(theta_values[1])
        if var < 0.01:

            print ("Goal achieved")
            print ("values of theta_0 and theta_1 are",theta_0," ",theta_1)
            a = np.asarray(list_0_gradient)
            b = np.asarray(list_1_gradient)
            theta_0_values = np.asarray(theta_0_values)
            theta_1_values = np.asarray(theta_1_values)

            c = np.arange(counter)
            plt.plot(c, theta_0_values,'o-',label = "theta_0")
            plt.plot(c, theta_1_values,'x',label = "theta_1")
            plt.legend(loc = "best")
            plt.title("visualization of Theta_0 and Theta_1 values")
            plt.xlabel("Iteration")
            plt.ylabel("thetas values")
            plt.show()

            break

def load_data_set(file_name, mode):
    list = []
    with open(file_name,mode) as handle:
        for line in handle:
            a,b = map(float,line.strip().split())
            list.append((a,b))

    return list

gradient_descent()
