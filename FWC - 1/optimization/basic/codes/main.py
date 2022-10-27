import numpy as np
import cvxpy as cp

cost= np.array([250,200])
P= np.array([[2,1],[2,3],[2,9]])
Q= np.array([12,24,36])

def opt(x):
 return cost@x

# defining the variable
x= cp.Variable(2, integer=True)

# assigning constraints
constraints = [P@x>=Q] 

# defining ojective
objective= cp.Minimize(cost@x)

#defining the problem
prob= cp.Problem(objective,constraints)

# solving the problem
prob.solve()

#printing the optimum value to minimum cost
print(x.value)
print(opt(x.value))
