'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    result = 0
    for num in arr:
        # XOR (exclusive OR) returns the result of two integers
        result ^= num
    # result will equal the single number
    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    pass

    # print(f"The odd-number-out is {single_number(arr)}")