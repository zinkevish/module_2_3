my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = []
i = 0

while i < len(my_list):
    if my_list[i] < 0:
        break
    elif my_list[i] <= 0:
        i += 1
        continue
    number.append(my_list[i])
    i += 1
for num in number:
    print(num)
