class Node:
    '''
    A Node class
    '''
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self):
        '''
        Link to the first element
        '''
        self.top = Node()
        self.tail = None
        self.len = 0

    def append(self, value):
        '''
        Append a value to LinkedList
        O(1)
        '''
        new_node = Node(value)
        if self.tail:
            self.tail.next_node = new_node
        else:
            self.top.next_node = new_node
        self.tail = new_node
        self.len += 1

    def prepend(self, value):
        '''
        Insert value to the beginning of LinkedList
        O(1)
        '''
        new_node = Node(value)
        new_node.next_node = self.top.next_node
        self.top.next_node = new_node
        if self.tail is None:
            self.tail = new_node
        self.len += 1

    def find(self, target):
        '''
        Find the first node with value
        O(N)
        '''
        current = self.top.next_node
        while current:
            if current.value == target:
                return current
            current = current.next_node
    
    def insert(self, target, value):
        '''
        Insert value after target
        O(N)
        '''
        target_node = self.find(target)
        if target_node:
            new_node = Node(value)
            new_node.next_node = target_node.next_node
            target_node.next_node = new_node
            
            if self.tail == target_node:
                self.tail = new_node
            self.len += 1

    def delete(self, target):
        '''
        Delete the first node with value
        O(N)
        '''
        current = self.top.next_node
        prev = self.top
        while current:
            if current.value == target:
                prev.next_node = current.next_node
                self.len -= 1
                if current == self.tail:
                    if prev == self.top:
                        self.tail = None
                    else:
                        self.tail = prev
                break
            prev = current
            current = current.next_node

    def __len__(self):
        '''
        Return length of LinkedList
        '''
        return self.len
   
    def __str__(self):
        '''
        Return all elements as a string
        '''
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"