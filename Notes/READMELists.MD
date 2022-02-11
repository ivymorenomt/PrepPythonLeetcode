## Lists
What is a List? It is a collec tion or grouping of items.
This is also known as Array in other languages.

It is a fundamental data structure for organizing collections of items.

A list should look like this:
```
    tasks = ['Install Python', 'Learn Python', 'Take a Break']
```
We can have a string, a boolean, or integers in the list.

**len** - this is used to find out how many elements or items are there in a list.
This is very useful when looping in a list. We need to know how many elements are there to loop.

**range** - this is a built in function used to make a list.

```
    r = (1,10) # this is going to create a sequence from 1 - 9
    list(r)
    [1,2,3,4,5,6,7,8,9]
```
When we do list on a range, it will give us a list of a range. We are not only using range to loop thru items, but we can also convert a range of numbers to a list.

## Accessing values in a list
``` 
    colors = ['purple', 'teal', 'orange']
    colors[2]  - this would access index 2's element which is orange.
    colors[-1] - this would access index 2' element which is orange.
    colors[-3] - this would access 3 index backwards which is purple.
```
### Check if a value is in a list
Capitalization matters!

``` 
    colors = ['purple', 'teal', 'orange']
    'purple' in colors
     - True
    'Purple' in colors
     - False
```
Every item has an index, and it starts with 0.
If we go past the range, it will give you an error.

## Iterating over a list

### Using FOR Loop
``` 
    colors = ['purple', 'teal', 'orange']
    for color in colors:
        print(color) # this will output all the items in the colors list.

    for x in range(1,4):
        print(x) # this will output a range of numbers
```
### Using While Loop
We have to take advantage of the index.

print out the numbers and add 1.

``` 
   numbers = [1,2,3,4]
   idx = 0

   while idx < len(numbers):
        print(numbers[i])
        i += 1
numbers[i]
# 1
# 2
# 3
# 4

```
To combine strings together, and format in upper case:

```
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = (''.join(sounds)).upper()
```
or
```
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()

```
## List Methods

Note: Functions and Methods are not the SAME! They are not entirely interchangeable. A method is a type of a function, but there is a significant distinction.

Built in functions examples are print, len.
Methods are .append(), .sort(). The way we use them is to access with a dot.

* ### Append
This is a list method used to add an item to the end of the list.

```
    list = [1,2,3,4]
    list.append(5)
    # [1,2,3,4,5]
```
It only takes 1 argument.

* ### Extend
It adds the items in the end, individually. It would not add it as a nested list.

```
    list = [1,2,3,4]
    list.extend([5,6,7,8])
    # [1,2,3,4,5,6,7,8]
```
* ### Insert
This method is used to insert an item at a given position.

```
    .insert(position, string/number)
```
Example:
```
    list = [1,2,3,4]
    list.insert(2, 'Hi') - this will be inserted, before the indicated position.
    # [1,2,'Hi', 3, 4] 
    list.insert(-1, 'End')
    # [1,2,3,'End',4] 
```

* ### Clear
Remove all items from the list

```
    first_list = [1,2,3,4]
    first_list.clear()
    # first_list is empty
```
* ### Remove
* Removes the first item from the list whose value is x
* Throws a ValueError if the item is not found.
```
    first_list = [1,2,3,4,4]
    first_list.remove(2) # removes the value 2 [1,3,4,4]
    first_list.remove(4) # removes the first item which is 4 [1,3,4]
```
* ### Pop
* Remove the item at the given position in the list
* If no index is specified, it removes and returns last item

```
    first_list = [1,2,3,4]
    first_list.pop(1) # removes 2
    first_list.pop() # removes 4
```
* ### Index
Returns the index of the specified item

```
    numbers = [5,6,7,8]
    numbers.index(6) # 1
    numbers.index(8) # 3
```
* ### Count
Returns the number of times x appears in the list

```
    numbers = [5,6,6,8]
    numbers.count(6) # 2
    numbers.index(8) # 1
```

* ### Sort
Sorts the items of the list (in-place)

```
    numbers = [8,7,6,5]
    numbers.sort(6) # [5,6,7,8]

    names = ["arya", "colt", "ARYA", "Arya"]
    names.sort() # ["ARYA", "Arya", "arya", "colt"]
```
* ### Reverse
Reverses the elements of the list(in place)

```
    numbers = [5,6,7,8]
    numbers.reverse() # [8,7,6,5]
```
* ### Join
Join is not a list method. It is a string method, and we are calling it on a string. This is used to convert list to strings.

```
    words = ['Coding', 'is', 'Fun']
    ' '.join(words) # Coding is fun
```
## Slices
Make new lists using slices of the old list.

```
 some_list [start:end:step]
```
### First Parameter: Start
What index to start slicing from

```
    first_list = [1,2,3,4]
    first_list[1:] # [2,3,4]
    first_list[3:] # [4]
```
If you enter a negative number, it will start the slice that many back from the end.
```
    first_list[-1:] # [4]
    first_list[-3] # [2,3,4]
```

## Swapping values in list
