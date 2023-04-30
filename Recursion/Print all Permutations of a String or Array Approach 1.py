def permutations(perm, visited):
    if len(perm) == len(arr):
        print("".join(perm), end="    ")
    for i in range(0,len(arr)):
        if i not in visited:
            perm.append(arr[i])
            visited.add(i)
            permutations(perm, visited)
            perm.pop(-1)
            visited.remove(i)

if __name__ == "__main__":
    arr = ["a","b","c","d","e","f","g"]
    permutations([],set())
