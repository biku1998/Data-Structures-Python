# Implementation of Tree Data Structure in python
'''
@ Some proprties : 

- tree data structure can be seen as s recursive structure 
- if the no of nodes in a tree is n , then no of edges or no of links will be n-1.
- Depth of a node : no of edges or links in path from root node to that node.
- Depth of root node is 0.
- Height of a node : The no of edges in the longest path from that node to a leaf node i.e a node having no children, is called height.
- Height of leaf node will be zero.
- Height of a tree  =  Height of the root node.
- Height of an empty tree = -1
- Height of tree having just one node i.e root only = 0

@ Types of tree :
    - Binary tree : a tree in which each node has atmost 2 children.
    - Strict/proper Binary tree : a tree in which each node can have either 2 or 0 children.
    - Complete Binary Tree : A tree in which all levels except possibly the last are completly filled and all nodes are as left as possible.
    - Perfect Binary tree : All levels will be completly filled.
    - Balanced Binary Tree : a tree is balanced if the diffrence between the height of the left and right subtree for every node is not more that k(k is mostly 1).
                            diffrence = |height(of left) - height(of right)|.
    - Binary Search Tree(Balanced is good) : In binary search tree , for each node , the value of all the nodes in left sub tree is lesser and  the value of all
      the nodes in the right sub tree is greater. And the cost of operation such as insert , search or delete is O(log(n)) in avg case. This will possible only when
      the binary search tree is balanced.
    
@ Some more proprties :
    - maximum depth of the tree = height of the tree.
    - maximum no of node at any level i  = 2**i , remember level starts with 0 i.e the root node. 
    - maximum no of nodes in a Binary tree having height h  = 2**0 + 2**1 + 2**2 + .....+2**h ==> 2**(h+1) -1 == 2**(no of levels) - 1.
    - the best practice is to keep the height if the tree as less as possible , as many operation cost is propstional to the height of the tree.
    - That is keep the tree as dense as possible.
'''

## Here we will implement Binary Search Tree.

class BinarySearchTree(object):
    
    root_node = None


    def __init__(self):
        
        # The Structure : 

        self.data = None

        self.left = None

        self.right = None

    # Setter and getters

    def set_data(self,data):
        self.data = data

    def set_left(self,left):
        self.left = left

    def set_right(self,right):
        self.right = right

    def get_data(self):
        return self.data
    
    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    # This method will create an empty structure or node , insert the data provided and pass it on.
    def create_node(self,data):

        new_node = BinarySearchTree()
        new_node.set_data(data)
        
        return new_node

    
    
    # This mehtod will be used to insert data in tree.

    def insert(self,data):
        # if the tree does not exist then create one.
        if BinarySearchTree.root_node == None:

            self.create_node(data)

            return
        
        # checking if the given data is greater or smaller than the data present.Since this is a binary search tree we will insert
        # accordingly.
        if data <= BinarySearchTree.root_node.get_data():
            # if this condition holds then we will store it in left sub tree.

            BinarySearchTree.root_node  = new_node
        else:
            # if this condition holds
            pass




               




































