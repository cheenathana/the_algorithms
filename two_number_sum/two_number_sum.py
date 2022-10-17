# WAY 01
def two_number_sum_with_hashtable(arr, targetsum):
    # Empty dict to hold the number whose value not contibutes the total
    hashtable = {}

    for i in arr:
        val = targetsum - i;

        if val in hashtable:
            return (val, i)
        else:
            hashtable[i] = True


# WAY 02
def two_number_sum(arr, targetsum):
    # sort array by ascending order
    arr.sort()

    # var to point elements in the array
    lptr = 0
    rptr = -1

    while True:
        if arr[lptr] + arr[rptr] > targetsum:
            rptr += -1

        elif arr[lptr] + arr[rptr] < targetsum:
            lptr += 1

        else:
            return (arr[lptr], arr[rptr])




# Execution begins here
if __name__ == "__main__":
    arr = [3, 5, 22, 8, 11, 1, -1]
    targetsum = 10

    print(two_number_sum_with_hashtable(arr, targetsum))
    print(two_number_sum(arr, targetsum))
