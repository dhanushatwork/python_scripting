str_og = str(input("Enter a string "))
vowels = "aeiouAEIOU"
vow_str = ""
for i in str_og:
    if i in vowels:
        vow_str = vow_str + i
print(vow_str)        