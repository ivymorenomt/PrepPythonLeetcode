# [], [0], [0,0] - no head, one head and there's a next pointer, or one head, next pointer has value.
# use two pointers
def oddevenLinkedList(head):
    if not head or not head.next or not head.next.next:
        return head
    oddptr = current = head # node number 1
    evenptr = head.next # node number 2    
    evenhead = evenptr
    i = 1 # this is our moving pointer
    
    while current:
        if i > 2 and i % 2 !=0:
            oddptr.next = current
            oddptr = oddptr.next
        elif i > 2 and i % 2 == 0:
            evenptr.next = current
            evenptr = evenptr.next
        current = current.next
        i +=1
    evenptr.next = None # the next nodes after even nodes is Null
    oddptr.next = evenhead # make sure if it is an oddptr, the next nodes should be even
    
    return head
#Snippet of leetcode 