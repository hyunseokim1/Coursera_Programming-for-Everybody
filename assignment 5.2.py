largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        num1 = int(num)
    except :
        print("Invalid input")
        continue
    if smallest == None and largest == None :
        smallest = largest = num1
        
    elif num1 > largest :
        largest = num1
        
    elif num1 < smallest :
        smallest = num1

print("Maximum is", largest)
print("Minimum is", smallest)