def subsequences(subsequence, index):
    if index == len(arr):
        print("".join(subsequence))
        return None
    else:
        subsequence.append(arr[index])
        subsequences(subsequence, index+1)
        subsequence.pop(-1)
        subsequences(subsequence, index+1)
        
if __name__ == "__main__":
    arr = ["a","b","c"]
    subsequences([],0)
