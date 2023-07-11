#!/usr/bin/env python
# coding: utf-8

# ## Production Planning Problem:
# 
# >A company produces three products, Product A, Product B, and Product C. 
# 
# >Each unit of Product A requires 2 hours of labor, 3 units of raw material, and generates a profit of 10 dollars. 
# 
# >Each unit of Product B requires 3 hours of labor, 2 units of raw material, and generates a profit of 12 dollars. 
# 
# >Each unit of Product C requires 4 hours of labor, 4 units of raw material, and generates a profit of 15 dollars. 
# 
# >The company has 80 hours of labor available per day and 90 units of raw material available per day. 
# 
# >Additionally, there are sales constraints that limit the maximum number of units sold for each product. The sales constraints are as follows:
# 
# * The maximum number of units sold for Product A is 30.
# * The maximum number of units sold for Product B is 20.
# * The maximum number of units sold for Product C is 25.

# ### objective function
# 
# $$\text{Maximize:} 10x + 12y + 15z$$

# ### subject to

# $$2x + 3y +4z<= 80$$
# $$3x + 2y +4z<= 90$$
# $$x <= 30$$
# $$y <= 20$$
# $$z <= 25$$

# In[24]:


from pulp import *


# In[25]:


problem = LpProblem('Production_Planning', LpMaximize)


# In[26]:


# Decision Variables
x = LpVariable('Product_A', lowBound=0, cat=LpInteger)
y = LpVariable('Product_B', lowBound=0, cat=LpInteger)
z = LpVariable('Product_C', lowBound=0, cat=LpInteger)

# Objective Function
problem += 10 * x + 12 * y + 15 * z

# Constraints
problem += 2 * x + 3 * y + 4 * z <= 80  # Labor Constraint
problem += 3 * x + 2 * y + 4 * z <= 90  # Raw Material Constraint
problem += x <= 30                      # Sales Constraint for Product A
problem += y <= 20                      # Sales Constraint for Product B
problem += z <= 25                      # Sales Constraint for Product C

# Solve the problem
problem.solve()

# Print the optimal solution
print("Optimal Solution:")
print("Product A:", value(x))
print("Product B:", value(y))
print("Product C:", value(z))
print("Maximum Daily Profit:", value(problem.objective))


# ### In conclusion, to maximize profit we should produce 22 units of product A, 12 units of product B and 0 units of product C for a maximum daily profit of 364 dollars
