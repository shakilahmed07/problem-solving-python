# Take Two Numbers
# calculate result second number power of first number

base_num = int(input("Give me the base number : "))
power_num = int(input("Give me the power number : "))
result = base_num ** power_num
print("Your Result is : ", result)

# shortcut

base_num = int(input("Give me the base number : "))
power_num = int(input("Give me the power number : "))
result = pow(base_num, power_num)
print("Your short Result is : ", result)