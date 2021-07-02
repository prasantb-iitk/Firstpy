import numpy as np          #NumPy incorporated for typical sin or cosines

def f(x):                   #Define the Function
    return (np.cos(x))

            
def gc(a, b, n):          #Define the Rule
    
    quadrature = 0
    q = (b-a)/2
    r = (b+a)/2
                            #Set the loop for sub-intervals
    for i in np.arange (1, n+1):
        integration = q * f((q * np.cos((2*i-1)*np.pi /(2*n))) + r)
        quadrature = integration + quadrature

        print (i, integration)

    quadrature = quadrature * np.pi / (n)
    print(quadrature)
gc(-5, 5, 6)              #Call the function with parameters a, b and steps
