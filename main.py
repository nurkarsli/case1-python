class Array:
    
    @staticmethod
    def remove_duplicates(*arrays):
        
        result = []
        for arr in arrays:
            for elem in arr:
                if elem not in result:
                    result.append(elem)
        return result

    @staticmethod
    def separate_even_odd(arr):

        if not arr:
            print("You can not separate an empty array.")
            return {"odd_numbers": [], "even_numbers": []}
        
        even_numbers = []
        odd_numbers = []
        for elem in arr:
            if isinstance(elem, int) and elem % 2 == 0:
                even_numbers.append(elem)
            elif isinstance(elem, int) and elem % 2 == 1:
                odd_numbers.append(elem)
        
        return {"odd_numbers": odd_numbers, "even_numbers": even_numbers}

array_1 = [4,6,2,3,9,6,12,11,143,10]
array_2 = [5,8,12,4,54,12,5,41,2,30]
array_3 = [21,9,9,1,4,52,9,1,4,2]

utils = Array()

# Duplicate values are removed from the array in this part of the code.
result_1 = utils.remove_duplicates(array_1, array_2, array_3)
print(result_1)

# This part of the code contains even and odd number values. The values found are placed in arrays.
array_4 = [1, 2, 3, 4, "hello", 5, "world"]
result_2 = utils.separate_even_odd(array_4)
print(result_2)  

