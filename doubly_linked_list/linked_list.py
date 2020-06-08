class Node:
    def __init__(self,value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_next(self, new_next):
        self.next_node = new_next

    def get_next(self):
        return sefl.next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #needs to set head/tail get head/tail
    #add tail (append)
    def add_tail(self, value):
        new_node = Node(value, None)#the tail next value is always None! that is bc it is the tail :)
        #what if LL is empty?How will know if LL empty
        if not self.head:#check if there is no head
            self.head = new_node
            self.tail = new_node#both head and tail = new node when adding first node to a LL
        else:
            self.tail.set_next(new_node)
            set.tail = new_node
    
    def update_head(self):
        #when setting a new head (prepend)
        #first must check if head
        if not self.head:
            return None
        
        #check if head has no next value, there single element in list and that means
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()

        value = self.head.get_value()
        self.head = self.head.get_next()
        return value
