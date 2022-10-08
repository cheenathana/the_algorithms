
def two_number_sum_with_hashtable(arr, targetsum):
    """
    APPROCH I
    =========
    - Create a empty hashtable
    - Loop through the array
    - If (x - arr[0]) in hashtable, then return arr[0] and hashtable_value
    - If the x - arr[0] not in hashtable, then add the arr[0] to hash table
    - Continue with the next element

    Time complexity : O(N)
    Space complexity: O(N)
    """
    # Empty dict to hold the number whose value not contibutes the total
    hashtable = {}

    for i in arr:
        val = targetsum - i;

        if val in hashtable:
            return (val, i)
        else:
            hashtable[i] = True


def two_number_sum(arr, targetsum):
    """
    APPROCH II:
    ===========
    - Sort the array
    - Place two variable to point values from left and right
    - add the value pointed by left and right and check if its equal to x
    - if left+right == targetsum, then return it and quit
    - if left+right > targetsum, then move the right pointer toward left
    - if left+right < targetsum, then move the left pointer toward right
    - Continue this until both value adds to x

    Time complexity : O(log N) + O(N) 
    Space complexity: O(1)              we are not occupying any space
    """
    lptr = 0
    rptr = -1

    while True:
        if arr[lptr] + arr[rptr] > targetsum:
            rptr += -1

        elif arr[lptr] + arr[rptr] < targetsum:
            lptr += 1

        else:
            return (arr[lptr], arr[rptr])




if __name__ == "__main__":
    arr = [3, 5, -1, 8, 11, 1, -1]
    targetsum = 10

    print(two_number_sum_with_hashtable(arr, targetsum))
    print(two_number_sum(arr, targetsum))
