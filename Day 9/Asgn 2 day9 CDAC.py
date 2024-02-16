from pulp import *
model = LpProblem(name="C-DAC ACTS", sense=LpMaximize)

# Parameters
f = 100 # Faculty members
c = 12 # Classrooms
m = 500 # Machines
fh = 40 # Maximum teaching hours per faculty member
ch = 50 # Maximum teaching hours per classroom
m_s = 0.5 # Minimum machines required per student
sc = 70 # Student capacity per classroom

# Decision variables 
x = LpVariable("Students", 0, None, LpInteger)

# Define objective function
# 2 * fh * x : Represents the total teaching hours contributed by faculty members for a given number of students. Assumption: Each student
# requires two hours of faculty time per week.

obj = 2 * fh * x + ch * x
model += obj

# Define constraints
model += (2 * fh / sc) * x <= f
model += x <= c*sc
model += m_s * x <= m

# Solve model
model.solve()

for v in model.variables():
    print(v.name, "=", v.varValue)






