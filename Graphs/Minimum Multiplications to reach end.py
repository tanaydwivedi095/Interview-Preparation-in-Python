from math import inf

def minMultication(start, end, array):
    distance = [inf for i in range(0,100000)]
    distance[start] = 0
    queue = []
#     node = [steps, start]
    queue.append((0,start))
    while queue:
        currNode = queue.pop(0)
        steps, node = currNode
        for it in array:
            num = (it * node)%100000
            if (steps+1) < distance[num]:
                distance[num] = steps+1
                if num==end: return steps+1
                queue.append((steps+1,num))
    return -1
    
if __name__ == "__main__":
    start = 3
    end = 30
    array = [2,5,7]
    print(minMultication(start, end, array))
