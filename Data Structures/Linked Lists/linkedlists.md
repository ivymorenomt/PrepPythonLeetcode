## Linked List

### Overview
A linked list is a linear data structure, where elements are stored at non-contiguous locations. A linked list is like a chain made of **nodes** and the links are **pointers**.

**Pointers are the connections** that hold the pieces of linked structures together.Pointers represent the address of a location in memory.

Every Node has 2 parts:
data and a pointer to the next Node.

It is a whole collection of Nodes.

root node - should be pointed to as head
next node - Null/None

![linked list](../img/linkedlist.png)

There are two types:
* Doubly Linked List - each node has two pointer, this allows you to go backwards and forward rather than one direction way in a linked list. - Next, Previous
* Circular Linked list - end node points to the front node

### Why Linked List?
* They can be used to implement other common abstract data types, including lists, stacks, queues.
* Preferred data structures over arrays because of elements can be easiliy inserted or removed without reallocation or reorganization of the entire structure.

Pros and Cons
|Advantages | Disadvantages |
| --- | --- |
| Dynamic Size (there is no need to ever resize a linked list.) |  Very Slow when it comes to **Access** and **Search** we have to iterate over each element sequentially starting from the list node. |
|  Quick Insertion/Deletion of Nodes because you just change the pointers of each node to insert/delete. |  Extra space for pointer. |

### Big O Analysis
![linked list](../img/linkedlistbigo.png)

### Operations

**get_size()** - tracks the size of a list.

**find(data)** - starts at root and compare the values, then it goes to the next node. If it can't find the node, it will return Null.

**add(data)** - it will create a new node. It will change the next pointer so it would change the old root node to Next node. The new node would be the new root.

**remove(data)** - first we have to find, so we will start from the root, then compare the data, then look at next pointer in our previous node.  

 