# Multiply an equation for simultaneous equations
# and use the solution to find a common term to
# eliminate.

# Intended for linear programming tasks.

print("Linear Programming\nEquation Multiplier")
print("To exit, product of\nabc should equal 0.\n")

def rep():
    a = float(input("Enter var x: "))
    b = float(input("Enter var y: "))
    c = float(input("Enter var =: "))
    m = float(input("Enter multi: "))
    if (a*b*c*m)==0:return
    else:
        print("Solution is:\na: "+str(round(a*m, 2))+"\nb: "+str(round(b*m, 2))+"\nc: "+str(round(c*m, 2))+"\n")
        rep()

rep()