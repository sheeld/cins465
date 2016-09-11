#!/usr/bin/env python

# Cins 465 Adv Web Dev - Assignment 1 - Written by Sheel Doshi

# ______________________Part 1: Dictionary
class stringCount(object):

    def __init__(self, alist=None):
        self.alist = alist
        from collections import Counter
        sortedlist = sorted(Counter(alist).most_common())
        for key, value in sortedlist:
            Count = '{} {}'.format(key, value)
            print (Count)

#<<<Testing Code>>>

# alist = ["hello", "hello", "bob", "apple", "college", "4"] # Test
# stringCount(alist)

# ______________________Part 2: Is Float

class isFloat(object):
    
    def __init__(self, x=None):
        import re
        tested =  bool(re.match("^[-+]?[0-9]*\.?[0-9]+$", x))
        print (tested)
        
#<<<Testing Code>>>
    
# isFloat("4.0O0") #returns False
# isFloat("-1.00") #returns True
# isFloat("+4.54") #Returns True


# ______________________Part 3: Data-structures LinkedList

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return current
        
    def printLL(self):
        current = self.head

        while current:
            print (current.get_data(), end=' ')
            current = current.get_next()
        print ('')
        
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
#<<<Testing Code>>>
            
# ll = LinkedList()
# ll.insert(1)
# ll.insert(2)
# ll.printLL()
# ll.delete(2)
# ll.printLL()
# if ll.search(2):
#     print("Value 2 found")
# else:
#     print("Value 2 not found")
# if ll.search(1):
#     print("Value 1 found")
# else:
#     print("Value 1 not found")
# ll.insert(4)
# ll.printLL()
# print(str(ll.size()))