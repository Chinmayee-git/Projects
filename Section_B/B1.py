# taking inputs

n = input('Enter the size of the array : ')
arr = input('Enter the array (digits with space in between): ').split(' ')
arr = [int(j) for j in arr]

# making an array of indices of all the '1' inputs

indices = [i for i in range(len(arr)) if arr[i] == 1]

# if you see, logically, all the 1's would gather around the central '1'

mid = round(len(indices) / 2) - 1

swaps = 0

# this loop will itterate through the array and count the total number of swaps 
# required to get all the other '1' (except the mid) towards the mid

for x in range(len(indices)):
    swaps += abs(indices[mid] - indices[x]) - abs(mid - x)

print(swaps)
