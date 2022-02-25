## Tuples and Sets

### What is a Tuple:

An ordered collection or grouping of items.

```
    numbers = (1,2,3,4)
```
A tuple is immutable! It means, it cannot be changed. It is an unchanging way of storing data

```
    x = (1,2,3)
    3 in x # True
    x[0] = "Change" # TypeError: 'tuple' object does not support item assignment
```
**Why use a Tuple?**

Tuples are faster than lists. They are light weight, and if you have an ordered data that it is not going to change, you can make it a tuple which is faster.

Tuples are safer. It is not going to be suddenly empty or something is changed.

It can be used as valid keys in dictionary.

Some methods return them to you - like .items() when working with dictionaries!

Example: months - you can use tuples since these do not change

### Creating / Accessing
Create using ()
Accessing is just like a list!

```
    months = ('January', 'February'..)
    months[0] # January
```
### How to use it as keys in the dictionary

```
    locations = 
    {
        (35.6895, 39.6197) : "Tokyo",
        (36.6895, 40.6197) : "New York",
        
    }
    locations[(36.6895, 40.6197)] # "New York"
```
