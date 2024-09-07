num1 = 0
num2 = 1
limit = int(input("Enter Limit: "))

for i in range (limit):
    temp = num1
    num1 = num2 + temp
    num2 = temp
    print(temp)
