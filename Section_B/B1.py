n = input('Enter the size of the array : ')
arr = input('Enter the array (digits with space in between): ').split(' ')
arr = [int(j) for j in arr]

indices = [i for i in range(len(arr)) if arr[i] == 1]
mid = round(len(indices) / 2) - 1
swaps = 0

for x in range(len(indices)):
    swaps += abs(indices[mid] - indices[x]) - abs(mid - x)

print(swaps)
