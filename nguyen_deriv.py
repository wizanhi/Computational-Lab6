#Author: Anh Nguyen
#Course: PHY3990C - Introduction to Scientific Computing with Python
#Project: Lab 6 - Derivatives
#Date: Feb 16, 2017
#PyCharm 5.0.3 with Anaconda 3 for Python 3.5

from pylab import*

#Define the first function
def f1(t):
    return cos(t)

#define -sin(x)
def df1(x):
    return -sin(x)

#Define the second function
def f2(t):
    return exp(t)

#This is the forward difference method
def fd(f1,t,h):
    return (f1(t+h)-f1(t))/h

#This is the backward difference method

#This is the central difference method
def cd(f1,t,h):
    return (f1(t+0.5*h)-f1(t-0.5*h)/h)

#This is the extended difference method
def ed(f1,t,h):
    return (8*(f1(t+0.25*h)-f1(t-0.25*h))-(f1(t+0.5*h)-f(t-0.5*h)))/(3*h)

#This is the cubic approximation

#This is the quartic approximation

#Take function and find its derivative
def derivTest(f1,df1):
    errList=[] #list for error
    hList=[] # list for h values
    err=abs((cd()-cos())/cos()) #relative error
    #create a while loop to reduce h
    while h <= finfo(float).eps:#use numpy to get machine precision
        errList.append()
        hList.append()

#run main code
if __name__=="__main__":
    fd(cos,1,.5)