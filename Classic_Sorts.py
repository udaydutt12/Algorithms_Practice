#Do Classic Sorting Algorithms

#Bubble Sort
def bubble_sort(list1):
    n=len(list1)
    for i in range(n-1):
        for j in range(i+1,n):
            if list1[i]>list1[j]:
                temp=list1[i]
                list1[i]=list1[j]
                list1[j]=temp
    return list1
    
#Insertion Sort
def insertion_sort(list1):
    n=len(list1)
    for i in range(1,n):
        temp1=list1[i]
        index=i
        for j in range(i-1,-1,-1):
            temp2=list1[j]
            if temp1<temp2:
               list1[j]=temp1
               list1[index]=temp2
               index=j
    return list1
                
#quick sort
def quick_sort(list1):
    
#selection sort
def selection_sort(list1):

#merge sort 
def merge_sort(list1):

#Heap Sort
def heap_sort(list1):

#counting sort
def counting_sort(list1):
    
    
def radix_sort(list1):