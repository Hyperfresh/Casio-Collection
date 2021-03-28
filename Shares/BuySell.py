print('Shares: Buy & Sell')
print('DOES NOT SUPPORT\nFLAT RATE BROK!')

def optype():
    global optype
    optype = input("Buy or sell? ")
    if optype not in ["buy","sell"]: optype()
optype()

print("To exit, enter '0'\nfor all points.")
def repeat():
    a = int(input("Input shar: "))
    b = float(input("Input pric: "))
    c = float(input("Input brok: "))

    cons = round(a*b, 2)
    brok = round(cons*c, 2)
    tax = round(brok*.1, 2)
    if optype == "buy":  
        sol = round(cons+brok+tax, 2)
    else:
        sol = round(cons-brok-tax, 2)
    print("Consid is " + str(cons))
    print("Brok is " + str(brok))
    print("Tax is " + str(tax))
    print("Solution is " + str(sol) + "\n")
    if sol == 0: return
    else: repeat()
repeat()