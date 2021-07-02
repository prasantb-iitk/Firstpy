import numpy as np          #NumPy incorporated for typical sin or cosines

def f(x):                   #Define the Function
    return (np.exp(-x**2))   

            
def trap(a, b, n):          #Define the Trapezoidal Rule
    h = (b - a) / n
    integration = (f(a) + f(b)) * h / 2

                            #Set the loop for sub-intervals
    for i in range (1, n):
        k = a + (i * h)
        integration = integration + (f(k) * h)      
#        print (i,  integration)

    print("Total integration value = ", integration)    #The final result


trap(0, 5, 50)              #Call the trap function with parameters a, b and steps
