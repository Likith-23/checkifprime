from math import sqrt
number = int(input("ENTER A NUMBER..."))
print("\n")
if number > 1:
    for i in range(2, int(sqrt(number)) + 1):
        if int(number%i) == 0:
            print(number, "IS NOT A PRIME NUMBER...")
            break
    else:
        print(number, "IS A PRIME NUMBER...")