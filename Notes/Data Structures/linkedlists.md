## Linked List

Every Node has 2 parts:
data and a pointer to the next Node.

It is a whole collection of Nodes.

root node - should be pointed to as head
next node - Null/None

### Operations

**get_size()** - tracks the size of a list.

**find(data)** - starts at root and compare the values, then it goes to the next node. If it can't find the node, it will return Null.

**add(data)** - it will create a new node. It will change the next pointer so it would change the old root node to Next node. The new node would be the new root.

**remove(data)** - first we have to find, so we will start from the root, then compare the data, then look at next pointer in our previous node.  