#if
a = int(input("Enter number A "))
b = int(input("Enter number B "))
if a > b:
    print("A is greater than B")
elif a == b:
    print("A and B are same")
else:
    print("A is smaller than B")

cpu = float(input("Enter CPU usage value "))
mem = float(input("Enter Memory usage value "))
if cpu > 75:
    print("CPU usage is more the 75%")
elif cpu > 90:
    print("CPU usage is more than 90%")
else:
        print("CPU is not over cooked")
if mem > 75:
    print("Memory usage is more the 75%")
elif mem > 90:
        print("Memory usage is more than 90%")
else:
        print("Memory is not over cooked")