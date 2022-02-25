## List Comprehension

It is the most unique function of python.
It allows us to generate new list - example, if we want a list with squares, etc.

#### The syntax
[__ for __ in __]

The blanks are the variable: First is the variable name. The second blank is the same as the first one, Then the last one is where we are iterating to.
It could be a list, a range, etc.

```
    nums = [1,2,3]
```
Let's say, for every x in a list, we are going to multiply by 10 and put in new list.

```
    [x*10 for x in nums]
    # [10,20,30]
```

#### List comprehension vs looping

```
    numbers = [1,2,3,4,5]
    doubled_numbers = []

    for num in numbers:
        doubled_number = num*2
        doubled_numbers.append(doubled_number)
    
    # [2,4,6,8,10]

    # With list comprehension

    doubled_numbers = [ num * 2 for num in numbers]
    print(doubled_numbers) # [2,4,6,8,10]

    [num * 10 for num in range(1,6)] # [10, 20, 30, 40, 50]

    [bool(val) for val in [0, [], ' ']] # [False, False, False] 

    [str(num) for num in numbers] # ['1', '2', '3'] - you don't need to execute str to each line. 
```
Examples for String

```
    name = 'colt'
    [char.upper() for char in name] # ['C', 'O', 'L', 'T']

    friends = ['ashley', 'matt']
    [friend[0].upper() for friend in friends] # ['Ashley', 'Matt']
```

## List Comprehension with Conditional Logi
```
    numbers = [1,2,3,4,5]
    evens = [num for num in numbers if num % 2==0]
    odds = [num for num in numbers if num %2 !-0]

    with_vowels = "This is so much fun!"
    ''.join(char for char in with_vowels if char not in "aeiou") # Ths s s mch fn!
```

Some examples:
1. Given two lists [1,2,3,4] and [3,4,5,6], create a variable called answer, which is a new list that is the intersection of the two.
Your output should be [3,4]. Hint: use the in opearator to test whether an element is in a list. For example: 5 in [1,5,2] is True. 3 in [1,5,2] is False.
**Input**: [1,2,3,4] and [3,4,5,6]
**Output**: [3,4]
2.  Reverse a string

```
    answer = [val for val in [1,2,3,4] if val in [3,4,5,6]] - look the value 3,4 in the first list, and if value is in the second list, create the list.
    #the slice [::-1] is a quick way to reverse a string
    answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
```

Without list comprehensions, things are a bit longer:
```
    answer = []
    for x in [1,2,3,4]:
        if x in [3,4,5,6]:
            answer.append(x)
    answer2 = []
    for name in ["Elie", "Tim", "Matt"]:
        answer2.append(name[::-1].lower())
```
3. For all the numbers between 1 and 100(including 100) create a variable called answer, which contains a list with all the numbers that are divisible by 12.
```
    answer = [n for n in range(1,101) if n% 12==0]
```
4. Given a string "amazing" create a variable called answer, which is a list containing letters from "amazing" but not the vowels
```
    answer = [char for char in "amazing" if char not in "aeiou"] # 'm','z','n','g'
    
    answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]]
```