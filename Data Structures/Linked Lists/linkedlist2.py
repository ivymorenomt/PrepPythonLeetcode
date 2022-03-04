import re
from tkinter.tix import ListNoteBook


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        new_node = Node(data)
        cur = self.head # we will start at leftmost point of the list
        # we are going to iterate over each
        while cur.next !=None:
            #traverse to the list
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total = 0 
        while cur.next!=None:
            total+=1
            # traverse to the next node
            cur = cur.next
        return total
    def display_all(self):
        elems = []
        cur_node = self.head
        while cur_node.next !=None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
        
    def get(self, index):
        # check if the index is not out of range
        if index > self.length():
            print("Error: Index out of range!")
            return None    
        cur_index = 0
        cur_node=self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                print(f"The data in {index} is ", cur_node.data)
                return cur_node.data
            cur_index +=1
    def remove(self, index):
        if index > self.length():
            print("Error: Index out of range!")
            return None    
        cur_index = 0
        cur_node=self.head
        while True:
            last_node = cur_node
            # last node should point to the next node after the deleted.
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                print("Deleted Current node: ", cur_node.data)
                if(last_node.next is None):
                    return None
                else:
                    print("the next node is ", last_node.next.data)
                return
            cur_index +=1
            
    def remove_by_value(self, data):
        if self.head == data:
            self.head = self.head.next
            return
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                prev.next = cur.next
            prev = cur
            cur = cur.next
    def print_helper(self, node, name):
        if node is None:
           print(name + ": None")
        else:
           print(name, ":", node.data)
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev

            # self.print_helper(prev, "Prev")
            # self.print_helper(cur, "CUR")
            # self.print_helper(nxt, "NXT")
            # print("\n")
        
            prev = cur
            cur = nxt
        self.head = prev
        return self.head
    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            self.print_helper(prev, "Prev")
            self.print_helper(cur, "CUR")
            self.print_helper(nxt, "NXT")
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)
            
        self.head = _reverse_recursive(cur=self.head, prev=None)
            
       
            

        
a_list = LinkedList()
a_list.append("A")
a_list.append("B")
a_list.append("C")
a_list.append("D")
a_list.append("E")
a_list.display_all()
a_list.reverse_recursive()
a_list.display_all()
