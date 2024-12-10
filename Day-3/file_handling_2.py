# loop thru file
f = open("test.txt", "r")
for x in f:
    print(x)

f = open("test.txt", "w")
f.write("File tested done. Content overwritten")
f.close
f = open("test.txt", "r")
print(f.read())