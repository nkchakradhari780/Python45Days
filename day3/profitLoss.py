costPrice = float(input("Enter Cost Price: "))
sellingPrice = float(input("Enter Selling Price: "))

if sellingPrice > costPrice:
    print("Profit")
elif sellingPrice < costPrice:
    print("Loss")
else:
    print("No Profit No Loss")

amount = abs(costPrice - sellingPrice)
print(f"Amount: {amount}")
