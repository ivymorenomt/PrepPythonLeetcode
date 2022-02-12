def transfer(list1):
    list2 = []
    for i in list1:
        list2.append(i)
    print(list2)
    
def removeVowel(s):
    for i in s:
        if i is 'a':
            print('It is a vowel')
        else:
            print('Not a vowel')

def recurse(n):
    if n>1:
        recurse(n-1)
    print(n, end=" ")

recurse(5)

          
            
removeVowel("ba")

transfer([1,2,3,4,5])

