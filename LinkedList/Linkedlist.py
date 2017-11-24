# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:30:41 2017

@author: mohammad
"""

class Node(object):
    def __init__(self, name):
        self.name=name
        self.nextNode=None
class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0
    def insertStart(self,name):     #if the input is node it would be infinit loop # I do not know why I have written it.
	#I implement with node instead of name
	#and everything was ok
	
        node=Node(name)
        self.size=self.size+1
        if (self.head==None):
            self.head=node
        else:
            node.nextNode=self.head
            self.head=node
            
    def traverse(self):
        currentNode=self.head
        #print(currentNode.name)
        while currentNode != None:
            print(currentNode.name)
            #print("%d " % currentNode.name)
            currentNode=currentNode.nextNode

    def remove(self, node):
        if(self.head == None):
            return
        self.size=self.size-1
        pointerNode=self.head
        while pointerNode.name != node.name:
            previousNode=pointerNode
            pointerNode=pointerNode.nextNode
        if(node.name == self.head.name):
            self.head=self.head.nextNode
        elif(pointerNode == node):
            previousNode.nextNode=node.nextNode
        
            


l=LinkedList()

l.insertStart(1)
l.insertStart(2)
l.insertStart(2)
l.insertStart(2)
l.insertStart(4)
l.insertStart(5)
l.traverse()
#l.remove(node4)

print("-----------------------")
#l.traverse()



##################################

##problem 1


def duplicateRemove(l):
    a=[]
    if (l.head == None):
        return
    a.append(l.head.name)
    previousNode=l.head
    nodePointer=l.head.nextNode
    while nodePointer!=None:
        if nodePointer.name in a:
            previousNode.nextNode=nodePointer.nextNode
            nodePointer=nodePointer.nextNode
        else:
            a.append(nodePointer.name)
            previousNode=nodePointer
            nodePointer=nodePointer.nextNode
    print(a)
    return l     
            
duplicateRemove(l)
l.traverse()
