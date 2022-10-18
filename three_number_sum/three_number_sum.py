def three_number_sum(arr, targetsum):
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
