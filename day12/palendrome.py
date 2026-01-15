def checkPalendrome(str):
    str1 = str.replace(" ", "")
    reverse = str1[::-1]
    print(reverse)
    return str1.lower() == reverse.lower()


str = "Ni t in"
palendrom = checkPalendrome(str)
print(palendrom)
