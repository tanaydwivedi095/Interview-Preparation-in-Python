def combSum(sub, index, sum):
    if index==len(arr):
        return None
    if sum==target:
        res.add(tuple(sub))
    sub.append(arr[index])
    combSum(sub, index+1, sum+arr[index])
    sub.pop(-1)
    combSum(sub, index+1, sum)
    
if __name__ == "__main__":
    arr = [10,1,2,7,6,1,5]
    target = 8
    res = set()
    arr.sort()
    combSum([],0,0)
    print(list(res))
        
