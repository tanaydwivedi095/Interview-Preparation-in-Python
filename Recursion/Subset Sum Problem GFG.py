def subset(sub, index, target):
    if target==0:
        res.add(tuple(sub))
        return None
    if index == len(arr):
        return None
    sub.append(arr[index])
    subset(sub, index+1, target-arr[index])
    sub.pop(-1)
    subset(sub, index+1, target)

if __name__ == "__main__":
    arr = [3,34,4,12,5,2]
    target = 9
    res = set()
    subset([],0,target)
    for i in res: print(list(i))  
