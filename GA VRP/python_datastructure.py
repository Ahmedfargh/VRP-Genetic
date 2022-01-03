# -*- coding: utf-8 -*-
"""
الملف ده فى كل ال implementation بتاع linear datastructures أى خدمة
Created on Mon Dec  6 14:42:56 2021
#كل method من أسمها بتعمل أيه
#the graph datastructure is applied on romanian road map model as a graph
#ده كود أنا كاتبه فىه داتا ستراكتشرس بتاعة بايثون علشان تعملوا زيه و تذاكروه
@author: Ahmed farghly thabet
"""
import random
class Stack:
    def __init__(self):
        self._items=[]
    def push(self,item):
        self._items.append(item)
        return True
    def pop(self):
        if len(self._items)==0:
            return None
        else:
            temp=self._items.pop()
            return temp
    def delete_stack(self):
        while len(self._items):
            self._items.pop()
    def get_size(self):
        return self._top+1
    def is_empty(self):
        return len(self._items)==0
"""# مثال على أزاى تستخدم الكلاس
st=Stack()
for i in range(20):
    print(i)
    st.push(i)
while not st.is_empty():
    print(st.pop())
"""
class Queue:
    def __init__(self):
        self._items=[]
        self._front=0
        self._size=0
    def Enqueue(self,item):
        self._items.append(item)
        self._size+=1
        return True
    def Dequeue(self):
        if self.Is_empty():
            return None
        item=self._items[self._front]
        self._items[self._front]=None
        self._front=(self._front+1)%len(self._items)
        self._size-=1
        return item
    def Is_empty(self):
        return self._size==self._front
    def Get_size(self):
        return self._front-self._size
"""
Qu=Queue()
for i in range(21):
    print(i)
    Qu.Enqueue(i)
print("\n")
while not Qu.Is_empty():
    print(Qu.Dequeue())
"""
class PriorityQueue:
    def __init__(self):
        self._items=[]
        self._size=0
        self._front=0
    def Enqueue(self,item,priority):
        if self._size==0:
            self._size=1
            self._items.append([item,priority])
        else:
            item=[item,priority]
            i=self._size-1
            self._items.insert(int(priority), [item,priority])
            self._size+=1
            self._items.append(item)
            return True
    def Dequeue(self):
        if self.Is_empty():
            return None
        else:
            item=self._items[self._front]
            self._items[self._front]=None
            self._front+=1
            return item
    def get_Size(self):
        return self._size-self._front
    def Is_empty(self):
        return self._size==self._front
"""
Pqu=PriorityQueue()
for i in range(21):
    print(i)
    Pqu.Enqueue(i,i)
print("\n")
Pqu.Enqueue(3, 2.4)
while not Pqu.Is_empty():
    item=Pqu.Dequeue()
    print("item "+str(item[0])+" has priority "+str(item[1]))
"""
class Graph:
    def __init__(self,vlist=None):
        self._vlist={}
        self._vcount=0
        self._edge=0
        if self._vlist==None:
            self._vlist={}
            self._vcount=0
        elif not self._vlist==None:
            for v in self._vlist:
                self._vlist[v]=None
            self._vcount=len(self._vlist)
    def connect(self,source,adj,weight):#this connect a vertix with another
        if not source in self._vlist.keys():
            self._vlist[source]=list()
            self._vcount+=1
        if not adj in self._vlist.keys():
            self._vlist[adj]=list()
            self._vcount+=1
        if source==adj:
            self._vlist[source].append([adj,weight])
        else:
            self._vlist[source].append([adj,weight])
            self._vlist[adj].append([source,weight])
        self._vcount+=1
        self._edge+=1
    def get_graph(self):#get the graph as dicetionary datatype
        return self._vlist
    def get_size(self):#get the number of the edge +1
        return self._edge+1
    def _get_edge(self,v,tar):
        for item in self._vlist[v]:
            if tar==item[0]:
                return item
        return None
    def _shuffle(self,source):
        edge_list=self._vlist[source]
        new_edge_list=[]
        repeated=[]
        while len(repeated)!=len(edge_list):
            cur=random.randint(0,len(edge_list)-1)
            if not cur in repeated:
                new_edge_list.append(edge_list[cur])
                repeated.append(cur)
        return new_edge_list
    #def return_to_more_two_adj(self,)
    def find_Route(self,source,dist,route=[],org_start=None,discovered=[]):
        """
        *********************************************
        *this method work as bredth first algortihm* 
        *********************************************
        """
        #check where is the distination adjacent of current head
        edges=self._shuffle(source)
        for item in edges:
            #item[1] = weight 
            #item[0]=adj code
            if item[0]==dist:
                route.append(item)
                return route
        discovered.append(source)
        for item in edges:
            if item[0] in discovered:
                continue
            route.append(item)
            is_found=self.find_Route(item[0], dist,route,org_start,discovered)
            if is_found:
                return route
        return route
#building romanian roadmap graph
graph=Graph()
graph.connect(1, 2, 75)
graph.connect(1, 4, 118)
graph.connect(1, 11, 140)
graph.connect(2, 3, 71)
graph.connect(3, 11, 151)
graph.connect(4, 5, 111)
graph.connect(5, 6, 70)
graph.connect(6, 7, 75)
graph.connect(7, 8, 120)
graph.connect(8, 10, 138)
graph.connect(8, 9,140)
graph.connect(11, 9, 80)
graph.connect(11, 12, 99)
graph.connect(10, 13, 101)
graph.connect(12, 13, 211)
graph.connect(13, 14, 90)
graph.connect(13, 15, 85)
graph.connect(15, 16, 98)
graph.connect(15, 18, 142)
graph.connect(18, 19, 92)
graph.connect(19,20 , 87)
graph.connect(16, 17, 86)
route=[]
#print(graph.get_graph())
#print(graph.find_Route(1, 19,route))
#print(route)