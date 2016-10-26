from .interface import AbstractLinkedList
from .node import *


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        self.length = 0
        
        if elements is not None and len(elements) != 0:
            self.start = Node(elements[0])
            self.length += 1
            current = self.start
            for elem in elements[1:]:
                current.next = Node(elem)
                current = current.next
                self.length += 1
            self.end = current
        else:
            self.elements = elements
            

    def __str__(self):
        if not len(self):
            return '[]'
        ret_val = '['
        for elem in self:
           ret_val += "{}, ".format(elem)
        #if ret_val[-2:] == ", ":
        ret_val = ret_val[:-2]
        ret_val += ']'
        return ret_val

    def __len__(self):
        return self.length
            
    def __iter__(self):
        iter_object = self.start
        while iter_object:
            yield iter_object.elem
            iter_object = iter_object.next
        raise StopIteration

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        for idx, elem in enumerate(self):
            if idx == index:
                return elem

    def __add__(self, other):
        ret_list = LinkedList()
        # add the current nodes
        for elem in self:
            ret_list.append(elem)
        for elem in other:
            ret_list.append(elem)
        return ret_list

    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        return self

    def __eq__(self, other):
        idx = 0
        current = self.start
        other_current = other.start
        while idx < len(self):
            if current.elem != other_current.elem:
                return False
                
            current = current.next
            other_current = other_current.next
            idx += 1
            
        return True
        
    def __ne__(self,other):
        if len(self) != len(other):
            return True
        return not self.__eq__(other)
         
            

    def append(self, elem):
        node = Node(elem)
        if self.start is None:
            self.start = node
            self.end = node
            self.length += 1
        else:
            self.end.next = node
            self.end = self.end.next
            self.length += 1
        
    def count(self):
        return self.length

    def pop(self, index=None):
        if self.start is None: 
            raise IndexError
            
        if index and index > self.length-1:
            raise IndexError
            
        if len(self) == 1:
            to_pop = self.start.elem
            self.start = Node([])
            self.end = self.start
            self.length -= 1
            return to_pop
            
        if (index == None) or (index == len(self)-1):
            ''' Pop last item by default '''
            to_pop = self.end.elem
            current = self.start
            for elem in self:
                if current.next == self.end:
                    self.end = current
                    self.length -= 1
                    break
                current = current.next
            return to_pop
            
        elif index == 0:
            '''Pop first item '''
            to_pop = self.start.elem
            self.start = self.start.next
            self.length -= 1
            return to_pop
        else:
            ''' Pop for other elements'''
            current = self.start
            counter = 0
            for elem in self:
                if counter == index-1:
                    to_pop = current.next.elem
                    temp = current.next.next
                    current.next = temp
                    self.length -= 1
                    break
                counter += 1
                current = current.next
            return to_pop 
        