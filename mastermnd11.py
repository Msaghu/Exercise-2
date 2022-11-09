our_list = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]
print(our_list)

for num in range(len(our_list)):
    print(num)

#To compare the items in the list using their indices
for num in range(len(our_list) - 1):
    if our_list[num] > our_list[num + 1]:
        lowerNum = our_list[num + 1]
        upperNum = our_list[num]

        our_list[num] = lowerNum
        our_list[num + 1] = upperNum


print(our_list)

#        print(f"{our_list[num]} should be swapped with {our_list[num + 1]}")

