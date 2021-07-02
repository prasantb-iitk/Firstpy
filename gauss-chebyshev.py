import numpy as np          #NumPy incorporated for typical sin or cosines

def f(x):                   #Define the Function
    return (np.cos(x))

            
def gc(a, b, n):          #Define the Rule
    
    quadrature = 0
                            #Set the loop for sub-intervals
    for i in range (1, n+1):
        integration = f(np.cos((2*i-1)*np.pi /(2*n)))
        quadrature = integration + quadrature
        print (i, integration)
    quadrature = quadrature * np.pi / (n)
    print(quadrature)
gc(-1, 1, 6)              #Call the function with parameters a, b and steps
