num = []
inp = int(input("How many numbers: "))
for x in range(inp):
    y = int(input("Your number: "))
    num.append(y)
order = sorted(num)
if inp % 2 == 1:
    print("Your median is", order[int(inp/2-0.5)])
elif inp % 2 == 0:
    print("Your median is", (order[int(inp/2)]+order[int(inp/2-1)])/2)