# from pyomo.env import * (don't import like this, you may see this method of import in forums)
import pyomo.environ as pyo

## fix it according to your GLKP solver local path
solvername = 'glpk'
solverpath_exe = 'D:\\Solver\\winglpk-4.65\\glpk-4.65\\w64\\glpsol'

## Connecting to Solver and solving the instance
solver= pyo.SolverFactory(solvername, executable=solverpath_exe)

## constructing the model object
model = pyo.ConcreteModel()

## Variables
model.x = pyo.Var(within=pyo.NonNegativeReals)
model.y = pyo.Var(domain=pyo.NonNegativeReals)

## Constraints
model.con1 = pyo.Constraint(expr=model.x + 4*model.y <= 1 )
model.con2 = pyo.Constraint(expr=4*model.x + model.y <= 1)

## Objective
# model.obj = pyo.Objective(expr=model.x_1 + model.x_2)
model.obj = pyo.Objective(expr=model.x + model.y, sense=pyo.maximize)

##debugging the model
# model.pprint()
# model.x_1.pprint()
# model.con1.pprint()


results = solver.solve(model)
print(results)
## retrieving optimal values
# print(pyo.value(model.x))
# print(f"x: {pyo.value(model.x)}, y: {pyo.value(model.y)}")