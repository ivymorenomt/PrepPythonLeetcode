# Own linear search
def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False

a_list = [1, 8, 91, 32, 5, 6, 18, 100, 3]
print(linear_search(a_list, 92))


# Built In 'In'
unsorted = [1, 8, 9, 100, 4, 2, 10, 93]
print(93 in unsorted)