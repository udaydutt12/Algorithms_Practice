#Given a Maze in the form of a Binary M x N Matrix, find the length of the 
#shortest path in a maze a given source to a given destination.
#use BFS
class Node:
    def __init__(self,x,y,d):
        self.x = x
        self.y = y
        self.distance = d
def IsValid(mat_in,visited,i,j):
    r=len(mat_in)
    c=len(mat_in[0])
    if i>r or j>c or i<0 or j<0:
        return False
    if mat_in[i][j]==0 or visited[i][j]:
        return False
    return True
def BFS(mat_in,xs,ys,xe,ye):
    num_row=len(mat_in)
    num_col=len(mat_in[0])
    visited=[0*num_col]*num_row
    queue=[]
    queue.append(Node(xs,ys,0))
    while queue:
        curNode=queue.pop(0)
        #check the node first
        if curNode.x == xe and curNode.y == ye:
            return curNode.distance
        else:
            visited[curNode.x][curNode.y] = 1
        #add the node's neighbors
        if IsValid(mat_in,visited,curNode.x-1,curNode.y):
            queue.append(Node(curNode.x-1,curNode.y,curNode.distance+1))
        elif IsValid(mat_in,visited,curNode.x+1,curNode.y):
            queue.append(Node(curNode.x+1,curNode.y,curNode.distance+1))
        elif IsValid(mat_in,visited,curNode.x,curNode.y-1):
            queue.append(Node(curNode.x,curNode.y-1,curNode.distance+1))
        elif IsValid(mat_in,visited,curNode.x,curNode.y+1):
            queue.append(Node(curNode.x,curNode.y+1,curNode.distance+1))       
    return -1   

def main():
    # input a test maze
    mat = [
        [1,1,1,1,1,0,0,1,1,1],
        [0,1,1,1,1,1,0,1,0,1],
        [0,0,1,0,1,1,1,0,0,1],
        [1,0,1,1,1,0,1,1,0,1],
        [0,0,0,1,0,0,0,1,0,1],
        [1,0,1,1,1,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,0,0],
        [1,1,1,1,1,0,0,1,1,1],
        [0,0,1,0,0,1,1,0,0,1]
    ]
    
    #do BFS
    BFS(mat,0,0,7,5)
    return 0

if __name__ == "__main__":
    main()