og_str = str(input("Enter a string"))

rev_str = ""
index = len(og_str)-1
print(index)

while index >= 0:
    rev_str += og_str[index]
    print(rev_str)
    index -= 1
    print(index)

if rev_str == og_str:
    print(og_str, " is a planidrome")
else:
    print(og_str, " is not a planidrome")