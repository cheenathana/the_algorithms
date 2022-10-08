def three_number_sum(arr, targetsum):
    """
    Inputs:
    arr = [12, 3, 1, 2, -6, 5, -8, 6]
    targetsum = 0

    Output:
    All possible three number combination which adds to the target sum value
    [[-8, 2, 6], [-8, 3,5], [-6, 1, 5]]

    APPROACH:
    - Sort the array
    - Use two loop. first loop to pick each element
    - Second loop 
       - use two variable to point to left & right values
       - at each iteration check firstloop_var + right_val + left_val
       - if all adds to targetsum, add to output list and move both the pointer position
       - if add_value > targetsum, move the right_pointer towards left
       - if add_value < targetsum, move the left_pointer towards right
       - Left position should always lower than right position to avoid out-of-bound

    Time complexity:  O(N^2)    # as we loop using two loops
    Space complexity: O(N)      # space used by output array,in worst case we 
                                # may have all elements in the output
    """
    output = []

    # Sorting the array
    arr.sort();

    # len -2 is used to ensure we always have two number ie. left & right pointers
    for i in range(len(arr) - 2):
        # Initialize left and right pointer with positions of array
        lptr = i + 1
        rptr = len(arr) - 1

        # Loop to control the moving of left and right positions
        while lptr < rptr:
            current_sum = arr[i] + arr[lptr] + arr[rptr]

            # CHECKPOINT 1
            if current_sum == targetsum:
                output.append([arr[i], arr[lptr], arr[rptr]])
                
                # Moving both the pointer positions one step
                lptr = lptr + 1
                rptr = rptr - 1

            # CHECKPOINT 2
            if current_sum < targetsum:
                lptr = lptr + 1

            # CHECKPOINT 3
            if current_sum > targetsum:
                rptr = rptr - 1

    return output






# EXECUTION BEGINS HERE
if __name__ == "__main__":
    # Inputs
    arr = [12, 3, 1, 2, -6, 5, -8, 6]
    targetsum = 0

    # Output: 
    # Find all possible three number combination which adds to
    # the targetsum value
    output = three_number_sum(arr, targetsum);
    print(output)
