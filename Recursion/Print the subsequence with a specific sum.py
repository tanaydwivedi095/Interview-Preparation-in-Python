def subsequence(sub, index, sum):
    if sum==target:
        print(sub)
        return None
    if index==len(arr):
        return None
    sub.append(arr[index])
    subsequence(sub, index+1, sum+arr[index])
    sub.pop(-1)
    subsequence(sub, index+1, sum)

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    target = 5
    subsequence([], 0, 0)
