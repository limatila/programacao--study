
def binarySearchRecursive(numbers: list[int] | int, entry: int) -> int:
    """Returns index of a given entry inside a list of numbers, on recursive execution

    Args:
        numbers (list[int] | int): either a list of numbers, or a max value to generate a list of range(numbers)
        entry (int): number to be searched for its index

    Returns:
        int: index found of entry
    """

    #converting int to a usable list
    if not isinstance(numbers, list):
        numbers = list(range(numbers))
    else: numbers = sorted(numbers)
    # print( numbers[len(numbers) // 2] ) #verify middle

    def compute(arr = numbers, entry = entry, start: int = 0, end: int = len(numbers)) -> int:
        if start > end: return False
        
        middlePoint = (start + end) // 2

        if arr[middlePoint] == entry: return (True, middlePoint)
        elif entry < arr[middlePoint]: 
            return compute(start=0, end=middlePoint - 1) 
        else:
            return compute(start=middlePoint + 1, end=end)
        
    return compute()

if __name__ == "__main__":
    print(binarySearchRecursive(1024, 371))
    print(binarySearchRecursive(list(range(2 ** 8)), 192))
    print(binarySearchRecursive([1, 30, 35, 90, 192], 192))