def reverse(l, r):
    if l>=r:
        return None
    else:
        arr[l], arr[r] = arr[r], arr[l]
        reverse(l+1, r-1)

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    reverse(0,len(arr)-1)
    print(arr)
