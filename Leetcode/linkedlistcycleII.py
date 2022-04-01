class Node:
    def __init__(self, val):
        self.head = val
        self.next = None
def detect_cycle(head: Node)-> Node:
    if not head or not head.next: None
    
    slow, fast = head, head
    cycle_len = -1
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_len = get_cycle_length(slow)
            break
    return None if cycle_len == -1 else get_starting_point(head, cycle_len)