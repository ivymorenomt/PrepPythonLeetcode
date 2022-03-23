class SLLNode:
    # Keep track of head value and next node
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # Methods to interact with Singly Linked List

    # get_data allows to get self.data attribute
    
    def get_data(self):
        ''''Return the self.data attribute'''
        return self.data

    # Set data allows to change self.data attribute
    def set_data(self, new_data):
        """Whatever we pass in here will replace current or existing value of self.data"""
        self.data = new_data
    
    # To traverse
    def get_next(self):
        """Return the self.next attribute"""
        self.next
    
    # Pass and reassign
    def set_next(self, new_next):
        """Whatever we pass in here will replace current or existing value of self.next
        This will be used if there is value on the next pointer.
        """
        
        self.next = new_next

node = SLLNode('apple')
print(node.get_data())

node2 = SLLNode('carrot')
print(node.set_next(node2))