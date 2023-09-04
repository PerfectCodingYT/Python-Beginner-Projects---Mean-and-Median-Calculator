num = int(input("How many numbers: "))
average = 0
for x in range(num):
    userInp = int(input("Your number: "))
    average = average + userInp
print("Your average number is", average/num)