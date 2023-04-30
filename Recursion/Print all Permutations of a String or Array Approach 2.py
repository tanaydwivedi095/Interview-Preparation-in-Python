def permutations(index):
    if index == len(arr):
        perm = []
        for i in range(0,len(arr)):
            perm.append(arr[i])
        print("".join(perm), end="   ")
        return None
    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]
        permutations(index+1)
        arr[index], arr[i] = arr[i], arr[index]
        
if __name__ == "__main__":
    arr = ["a","b","c","d","e","f","g"]
    permutations(0)
