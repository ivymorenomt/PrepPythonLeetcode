# def arrays(arr):
#     # iterate thru an array
#     print('Print the index')
#     for x in range(len(arr)):
#         print(x)
#     print('Print the items in the array')
#     for x in range(len(arr)):
#         print(arr[x])
#     print('Print the index and the items in the array')
#     for ind, n in enumerate(arr): # enumerate will print out the index as well
#         print(ind, n)
#     print('To Reverse')
#     print(arr)
#     start, end = 0, len(arr)-1
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start +=1
#         end -=1
#     print(arr)
# arr = [1,2,3,4]        
# arrays(arr)


def printarr(ar):
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            print(i, j)

ar = [1,2,3,4,5]
printarr(ar)