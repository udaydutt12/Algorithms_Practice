from math import floor
def HeapSort(mylist):
    n=len(mylist)
    BuildMaxHeap(mylist,n)
    for i in range(n,0,-1):
        mylist[1],mylist[i] = mylist[i],mylist[1]
        mylist=Heapify(mylist,1,n)
    return mylist
    
def BuildMaxHeap(mylist,n):
    for i in range(floor(n/2),0,-1):
        mylist=Heapify(mylist,i,n)
    return mylist

def Heapify(mylist,i,n):
    left=2*i
    right=2*i+1
    if left<=n and mylist[left]>mylist[i]:
        mymax=left
    else:
        mymax=i
    if right<=n and mylist[right]>mylist[max]:
        max=right
    if max!=i:
        mylist[i],mylist[max] = mylist[max],mylist[i]
        mylist=Heapify(mylist,max,n)
    return mylist
    