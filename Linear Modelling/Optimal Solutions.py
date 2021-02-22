print("Linear Programming")
print("Optimal Solution Finder")

def optype():
    global optype
    optype = input("Max + or min -? > ")
    if optype != ("+" or "-"): optype()
optype()

x = input("Input x var > ")
y = input("Input y var > ")

def repeat():
    a = input("Input vertex A > ")
    b = input("Input vertex B > ")
    if optype == "+":
        sol = (x*a) + (y*b)
    else:
        sol = (x*a) - (y*b)
    print("Solution is " + str(sol))
    if sol == 0: exit()
    else: repeat()
repeat()