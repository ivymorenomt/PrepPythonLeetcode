## Code to remember

### There are multiple ways to reverse a string in Python
#### Slicing Method
```
    string = "python"
    rev_string = string[::-1]
    print(rev_string)
```
#### using reversed function
```
    string = "python"
    rev= reversed(string) 
    rev_string = "".join(rev) 
    print(rev_string)
```
#### Using Recursion
```
    string = "python"
    def reverse(string):
    if len(string)==0:
        return string
    else:
        return reverse(string[1:])+string[0]
    print(reverse(string))
```
#### Using for Loop
```
    string = "python"
    rev_string =""
    for s in string:
    rev_string = s+ rev_string
    print(rev_string)
```

#### Using while Loop
```
    string = "python"
    rev_str =""
    length = len(string)-1
    while length >=0:
    rev_str += string[length]
    length -= 1
    print(rev_str)
```