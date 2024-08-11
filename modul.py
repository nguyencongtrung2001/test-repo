def onex(arr, s):
    a = []  # To store the subarray elements
    start = 0  # Initial start index

    def examine(start, sum):
        # Base case: if the sum exceeds s or we are out of elements, return -1
        if start >= len(arr):
            return -1

        # Add the current element to the sum
        sum += arr[start]

        # Check if the current element itself is greater than s
        if arr[start] > s:
            return examine(start + 1, 0)

        # If the sum matches s, return the start and end indices
        if sum == s:
            a.append(arr[start])
            return start - len(a) + 2, start + 1  # 1-based index

        # If the sum is less than s, include the current element in the list
        if sum < s:
            a.append(arr[start])
            result = examine(start + 1, sum)
            if result != -1:
                return result

        # If the sum exceeds s or no solution found, backtrack by removing the last element
        if a:
            a.pop()

        # Continue to the next element
        return examine(start + 1, 0)

    result = examine(start, 0)
    return result if result != -1 else -1



        




            
            
        