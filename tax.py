a=input("enter income")
e=float(input("enter exemption"))
income=a-e
tax=0
if income <= 500000:
        tax = income * 0.01
elif income <= 700000:
        tax = 5000 + (income - 500000) * 0.1
elif income <= 2000000:
        tax = 25000 + (income - 700000) * 0.2
else:
        tax = 215000 + (income - 2000000) * 0.3
print(f"Your income tax payable is: NPR {tax:.2f}")
