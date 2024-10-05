# Format Specifiers

number1=3.145
number2=-6978.23655
greet="HELLO AND WELCOME"
# Deciaml places 
print(f"Your Total Price is : {number1:.2f}")

# Right and Left Align
print(f"Your Total Price is : {number2:>10}") 
print(f"Your Total Price is : {number1:<10}")


# Thousand's place seperator , 
print(f"Your Total Price is : {number2:,}")

# Center Align 
print(f"{greet:^10}")