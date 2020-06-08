'''making a single linked list
each LL has a head and a tail. The tail-node 
always points to None and the tail to that tail-node. The head can be None if the tail is None.
The LL would be empty. The head will equal
the tail if there is a single node in LL.

a single node has a value and a pointer to
the next node location
next_node is a pointer to the next location of 
the neighbor node. it is defaulted to none 
'''
class Node:
    def __init__(self, value, next_node=None)
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def set_next(self, new_next):
        self.next_node = new_next
    
    def get _next(self)
        return self.next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    #defaulted to empty
    
    def add_to_tail(self, value):
        #making a new tail is the goal so the next_node 
        #would be None for tail-node
        new_node = Node(value, None)    
        #check if list is empty because tail=head then
        if not self.head:
            self.head = new_node
            self.tail = new_node
            # now the LL has one item
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next():
            head=self.head
            self.head = None
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    
