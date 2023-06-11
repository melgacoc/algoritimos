def is_num(nums):
    try:
        if any(n < 0 for n in nums):
            return False
    except TypeError:
        return False

    return True


def find_duplicate(nums):
    if not is_num(nums):
        return False

    nums_set = set()
    for num in nums:
        if num in nums_set:
            return num
        nums_set.add(num)

    return False
