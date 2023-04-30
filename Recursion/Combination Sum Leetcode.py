def combSum(sub, index, sum):
    if index==len(arr) or sum>target:
        return None
    if sum==target:
        res.add(tuple(sub))
    sub.append(arr[index])
    combSum(sub, index, sum+arr[index])
    combSum(sub, index+1, sum+arr[index])
    sub.pop(-1)
    combSum(sub, index+1, sum)

if __name__ == "__main__":
    arr = [2,3,6,7]
    target = 10
    res = set()
    combSum([],0,0)
    print(list(res))
