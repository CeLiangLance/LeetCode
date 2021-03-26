# -*- coding: utf-8 -*-
"""
641. Design Circular Deque
Medium

385

42

Add to List

Share
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
"""

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.arr = [0 for _ in range(k)]
        self.maxi = k
        self.length =0
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.length < self.maxi:
    
            #tmp = self.arr[0:]
            #self.arr = [0 for _ in range(self.length+1)]
            self.arr[0],self.arr[1:] = value,self.arr[0:-1]
            self.length +=1
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.length < self.maxi:
            '''
            tmp = self.arr
            self.arr = [0 for _ in range(self.length+1)]
            self.arr[0:-1],self.arr[-1] = tmp,value
            '''
            self.arr[self.length] = value
            self.length +=1
            return True
        else:
            return False       

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if(self.length>0):
            tmp = self.arr
            self.arr[0:-1],self.arr[-1] = tmp[1:],0
            self.length-=1
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if(self.length>0):
            
            self.arr[self.length-1]=0
            self.length-=1
            return True
        else:
            return False
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if(self.length>0):
            return self.arr[0]
        else:
            return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if(self.length>0):
            return self.arr[self.length-1]
        else:
            return -1     

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if(self.length>0):
            return False
        else:
            return True    
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if(self.length==self.maxi):
            return True
        else:
            return False   

        


