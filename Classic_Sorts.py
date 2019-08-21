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
    n=len(list1)
    for i in range(n):
        mymin=list1[i]
        index=i
        for j in range(i+1,n):
            if list1[j]<mymin:
                index=j
                mymin=list1[j]
        if index!=i:
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
    return list1

#merge sort 
def merge_sort(list1):
    n=len(list1)
    if n<=1:
        return list1
    elif n==2:
        if list1[0]>list1[1]:
            temp=list1[0]
            list1[0]=list1[1]
            list1[1]=temp
    else:
        partition=n/2
        list2=merge_sort(list1[:partition])
        list3=merge_sort(list1[partition:])
        list4=[]
        p1=0
        p2=0
        n2=len(list2)
        n3=len(list3)
        while p1<n2 or p2<n3:
            if p1==n2:
                while p2<n3:
                    list4.append[list3[p2]]
                    p2+=1
                break
            elif p2==n3:
                while p1<n2:
                    list4.append[list2[p1]]
                    p1+=1
                break
            if list2[p1]<list3[p2]:
                list4.append(list2[p1])
                p1+=1
            else:
                list4.append(list3[p2])
                p2+=1
        return list4
        
#counting sort
def counting_sort(list1):
    
    
def radix_sort(list1):