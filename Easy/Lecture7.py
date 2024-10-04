# Weight Converter  1kg ==2.2 lbs
weight=float(input("Enter Your Weight : "))
unit=input("Kilograms or Pounds : (K/P)").upper()

if unit=="P":
    weight/=2.2
    unit="Kgs"
    print(f"Your weight is : {weight} {unit}")
elif unit=="K":
    weight*=2.2
    unit="Lbs"
    print(f"Your weight is : {weight} {unit}")
else:
    print(f"{unit} is an Invalid Unit! ")