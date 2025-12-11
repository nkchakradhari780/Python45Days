percentage = float(input("Enter the percentage of the student: "))

if percentage >= 81 and percentage <= 100:
    print("Very Good")
elif percentage >= 61 and percentage <= 80:
    print("Good")
elif percentage >= 41 and percentage <= 60:
    print("Average")
elif percentage <= 40 and percentage >= 0:
    print("Fail")
else:
    print("Invalid Percentage Entered Please Enter in range of 0 to 100")
