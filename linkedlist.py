# LinkedList implementation in python

class LinkedList(object):
    
    '''
    Making the structure of the list.
    The data part will store our data.
    The next part will store the address of the next node.
    '''
    def __init__(self):
        
        self.data = None

        self.next = LinkedList

        self.head = None

        self.tail = None

    # setters and getters.

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self,data):
        self.data = data
    
    def set_next(self,next_node):
        self.next = next_node
    
    '''
    This method will initialise our list.
    '''
    def create_list(self,data):
        new_node = self.create_node(data)
        new_node.set_next(None)
        self.head = new_node
        self.tail = new_node

    '''
    This method will create an empty node i.e structure , puts the data provided and 
    returns it.
    '''
    def create_node(self,data):
        new_node = LinkedList()
        new_node.set_data(data)
        
        return new_node

    '''
    This method will store data in the starting end i.e front
    '''
    def store_at_first(self,data):

        # check if this is the first node or not ?

        if self.head == None:
            self.create_list(data)
            return
        # else we will store the data at first. i.e add a node at start

        new_node = self.create_node(data)

        new_node.set_next(self.head)

        self.head = new_node


    def __str__(self):

        ref = self.head
        data = ''
        while ref != None:
            data = data+str(ref.get_data())+'--'
            ref = ref.get_next()
        return data[:-2]
    
    '''
    This method will store data at last. i.e add a node at the end of the list
    '''

    def store_at_last(self,data):

        if self.head == None:
            self.create_list(data)
            return
        new_node = self.create_node(data)
        
        self.tail.set_next(new_node)

        new_node.set_next(None)

        self.tail = new_node






# main function ## Tester

def main():
    l = LinkedList()
    l.store_at_first(12)
    l.store_at_first(99)
    l.store_at_last(1001)
    l.store_at_last(1002)
    print(l)

if __name__ == '__main__':
    main()
