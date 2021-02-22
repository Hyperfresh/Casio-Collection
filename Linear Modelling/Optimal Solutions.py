# Find an optimal solution for maximising or minimising a value.
# Intended for linear programming tasks.

print("Linear Programming\nOptimal Solution Finder\n")

def optype():
    global optype
    optype = input("Max + or min -? > ")
    if optype != ("+" or "-"): optype()
optype()

x = int(input("Input x var > "))
y = int(input("Input y var > "))

print("To exit, enter '0' as vertex points for A and B.")
def repeat():
    a = int(input("Input vertex A > "))
    b = int(input("Input vertex B > "))
    if optype == "+":
        sol = (x*a) + (y*b)
    else:
        sol = (x*a) - (y*b)
    print("Solution is " + str(sol) + "\n")
    if sol == 0: exit()
    else: repeat()
repeat()