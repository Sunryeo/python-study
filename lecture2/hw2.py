num = int(input("input your number: "))
hundreds = num // 100
tens = num // 10 % 10
unit = num % 10

print(f"hundreds' digit: {hundreds}, tens' digit: {tens}, unit digit: {unit}")