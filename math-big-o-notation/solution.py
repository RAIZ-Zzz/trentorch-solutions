def count_comparisons_linear_search(arr, target):
    """
    arr:    a list of numbers
    target: the value being searched for

    Returns:
        (found, comparisons): found is True if target is in arr, False
        otherwise. comparisons is the number of element-to-target
        comparisons actually performed (stop as soon as a match is
        found -- don't keep scanning).
    """
    # TODO: Implement a left-to-right linear scan, counting comparisons.
    n = 0
    for i in arr:
        n += 1
        if target == i:
            return True, n
    return False, n


def count_comparisons_binary_search(sorted_arr, target):
    """
    sorted_arr: a list of numbers, already sorted ascending
    target:     the value being searched for

    Returns:
        (found, comparisons): same shape as count_comparisons_linear_search,
        but using binary search -- each comparison must actually halve
        the remaining search space.
    """
    left = 0
    right = len(sorted_arr)
    n = 0
    while left != right:
        n+=1
        center = (left + right)//2
        if target == sorted_arr[center]:
            return True, n
        if target > sorted_arr[center]:
            left = center + 1
        else:
            right = center
    return False, n
