def mergeTwoList(list1, list2):
    joinedList = (list1+list2)
    return sorted(joinedList)
list1 = [1,2,3]
list2 = [5,4,2]

print(mergeTwoList(list1, list2))
