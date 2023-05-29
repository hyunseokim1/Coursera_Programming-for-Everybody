def computepay(h, r):
    if h > 40 :
        pay = 40 * r + (h-40) * r * (1.5)
    else :
        pay = h * r
    return(pay)

h = input("Enter Hours:")
r = input("Enter Rate:")

f_h = float(h)
f_r = float(r)

pay = computepay(f_h, f_r)
print("Pay", pay)