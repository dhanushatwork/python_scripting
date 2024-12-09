message = "welcome to fight club"
actor = "Brad pit"
credits = message + " By " + actor
print(message.upper())
print(message.lower())
print(message.title())
print(credits)

#length of string
print(len(message))

#To find a string 
print(message.find("f"))
print(message.find("w"))
print(message.find("b"))
print(message.find("z"))

#To count string 
print(message.count("c"))
print(message.count("o"))

#Replace
print(message.replace("fight club", "fight club mania"))

#Check is all char are alphabets
print(message.isalpha())