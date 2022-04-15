class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def reverse2(self, head):
        
        
        #phase 2
        prev = None # previous should be null
        cur = head #initialize current node as hode
        
        while cur:
            nxt = cur.next # how we set curr.next to temp prev variable, so we should have this temporary variable
            cur.next = prev # shift the curr.next to previous
            prev = cur # current should be previous
            cur = nxt
        return prev
    
    #big O(n), space complexity O(1)
