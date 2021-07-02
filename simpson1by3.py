import numpy as np              #NumPy incorporated for typical sin or cosines

def f(x):                       #Define the Function
    return (1/(1+x**2))

            
def simp1by3(a, b, n):          #Define the Simpson one-third Rule
    h = (b - a) / n
    integration = f(a) + f(b)

                                #Set the loop for sub-intervals
    for i in range (1, n):
        k = a + (i * h)
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)

#        print(i, integration)

    integration = integration * h / 3   

    print("Total integration value = ", integration)    #The final result

simp1by3(-10, 10, 385)              #Call the simp1by3 function with parameters a, b and steps
