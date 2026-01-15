def checkPalendrome(str):
    reverse = str[::-1]
    print(reverse)
    if str.lower() == reverse.lower():
        return True
    else: 
        return False


str = "Nitin"
palendrom = checkPalendrome(str)
print(palendrom)
