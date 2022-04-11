

def duplicateletter(arr):
    if not arr: return 0
    if len(set(arr)) < len(arr):
        return True
    else:
        return False
    
arr = ['str', 'srt']
print(duplicateletter(arr))