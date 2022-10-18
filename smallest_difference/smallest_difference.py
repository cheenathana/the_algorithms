def smallest_difference(arr1, arr2):
    # Sort both the array
    arr1.sort()
    arr2.sort()

    # setting up var to point to the elements of the array
    idx1 = 0      
    idx2 = 0
    output = []

    # Initialize to infinity ie. the biggest value
    smallest_diff = float("inf")

    while (idx1 < len(arr1) and idx2 < len(arr2)):
        # checking the difference b/w current elements of array
        diff = abs(arr1[idx1] - arr2[idx2])

        if diff == 0:
            # means the numbers are same from both the array and ther diff is 0
            return [arr1[idx1], arr2[idx2]], diff

        # checking the current diff wih the smallest diff and updating the
        # output and diff values
        if diff < smallest_diff:
            smallest_diff = diff
            output = [arr1[idx1], arr2[idx2]]

        # Moving the index pointer
        if arr1[idx1] < arr2[idx2]:
            idx1 += 1;
        else:
            idx2 += 1;

    return output, smallest_diff





# Execution begins here
if __name__ == "__main__":
    arr1 = [-1, 5, 10, 20, 28, 3];
    arr2 = [26, 134, 135, 15, 17];

    output, diff = smallest_difference(arr1, arr2)
    print("NUmber pair with smallest difference: ", output)
    print("Smallest difference: ", diff)
