'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    result = []

    for i in arr:
        # if arr[i] == 0: 
        #     zero_arr.append(arr.pop(i))
        if arr[i] == 0:
            result.append(arr.pop(i))
    return arr

    # return arr[0], arr + zero_arr

# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [0, 3, 1, 0, -2]

#     print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")