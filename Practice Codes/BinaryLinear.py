# Find the number in the list and display the position of the searched number
# return -1 if not found
# input: 7
# output: 3

# Binary Search - the list should be sorted first before performing binary search

def locate_number(cards, query):
    print('Binary search with O of n 15ms')
    left, right = 0, len(cards) - 1
    while left <= right:
            pivot = left + (right - left) // 2
            if cards[pivot] == query:
                return pivot
            if query < cards[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
    return -1

# linear search
def linear_search(cards,query):
    position = 0
    print('This is Linear search with O of n 21ms')
    print('cards:', cards)
    print('query:', query)
    
    while True:
        print('position:', position)
        
        if cards[position] == query:
            return position
        
        position += 1
        if position == len(cards):
            return -1

test = {
      'input': {
        'cards': [-1, 0, 3, 5, 9, 12],
        'query': 9
    },
    'output': 0
}

result = locate_number(test['input']['cards'], test['input']['query'])
print(result)

res = linear_search(test['input']['cards'], test['input']['query'])
print(res)