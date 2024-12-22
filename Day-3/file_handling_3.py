f = open("logs.txt", "r")
find_str = str(input("Enter the String to count "))
count = 0
for x in f:
        count += x.count(find_str)
print(find_str, "appear", count, "times")
