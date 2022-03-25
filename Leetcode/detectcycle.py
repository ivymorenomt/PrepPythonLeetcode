class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def detect_cycle_start(head):
    if not head or not head.next:
            None
    slow = head
    fast = head
    while True:
        try:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        except:
            return False