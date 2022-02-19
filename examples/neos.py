import pyomo.environ as pyo
import os

# provide an email address
os.environ['NEOS_EMAIL'] = 'sina.hkazemi@gmail.com'

# formulate optimization model
model = pyo.ConcreteModel()

## Variables
model.x = pyo.Var(within=pyo.NonNegativeReals)
model.y = pyo.Var(domain=pyo.NonNegativeReals)

## Constraints
model.con1 = pyo.Constraint(expr=model.x + 4*model.y <= 1 )
model.con2 = pyo.Constraint(expr=4*model.x + model.y <= 1)

## Objective
model.obj = pyo.Objective(expr=model.x + model.y, sense=pyo.maximize)

solver_manager = pyo.SolverManagerFactory('neos')
results = solver_manager.solve(model, opt='cplex')
model.pprint()