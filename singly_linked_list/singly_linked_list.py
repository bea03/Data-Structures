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
        '''If there is only one item in the LL then the head and the tail will be the same, 
        therefore, you must set both the tail and head to none
        '''
        if not self.head.get_next():
            head=self.head
            self.head = None
            self.tail = None
            return head.get_value()
        value = self.head.get_value()#Why do we return the value?
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return false

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = none
            self.tail = none
            return value

        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False

        # Recursive solution
        # def search(node):
        #   if node.get_value() == value:
        #     return True
        #   if not node.get_next():
        #     return False
        #   return search(node.get_next())
        # return search(self.head)
    
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value
    
