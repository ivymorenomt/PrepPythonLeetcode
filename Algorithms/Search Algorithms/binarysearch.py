def binary_search(a_list, n):
    first = 0 # use first and last to keep track of the beginning and end of the list.
    last = len(a_list) -1
    while last >= first: # it will loop as long as there are still items in the list.
        mid = (first + last) // 2 # you are going to locate the midpoint using this line; this is the POSITION index of the item.
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

a_list = [10, 12, 13, 14, 15, 18, 19]
print(binary_search(a_list, 19))

from bisect import bisect_left

def bina_search(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if index <= len(an_iterable) and an_iterable[index] == target:
        return True
    return False


sorted_fruits = ['c', 'f', 'j']
print(bina_search(sorted_fruits, 'd'))