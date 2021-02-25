# Find an optimal solution for maximising
# or minimising the solution within a
# feasible region.

# Intended for linear programming tasks.

print("Linear Programming:\nOptimal Solution\nFinder\n")

def optype():
    global optype
    optype = input("Max or min? ")
    if optype != ("max" or "min"): optype()
optype()

x = float(input("Input x const: "))
y = float(input("Input y const: "))

print("To exit, enter '0' as\nvertex points for\nx and y.")
def repeat():
    a = float(input("Input vertex x: "))
    b = float(input("Input vertex y: "))
    if optype == "+":
        sol = round((x*a) + (y*b), 2)
    else:
        sol = round((x*a) - (y*b), 2)
    print("Solution is " + str(sol) + "\n")
    if sol == 0: return
    else: repeat()
repeat()