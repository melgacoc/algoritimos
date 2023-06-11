def sort(string):
    if len(string) <= 1:
        return string

    middle = len(string) // 2
    start = string[:middle]
    end = string[middle:]

    at_start = sort(start)
    at_end = sort(end)

    return merge(at_start, at_end)


def merge(list_a, list_b):
    result = []
    a = 0
    b = 0

    while a < len(list_a) and b < len(list_b):
        if list_a[a] < list_b[b]:
            result.append(list_a[a])
            a += 1
        else:
            result.append(list_b[b])
            b += 1

    result += list_a[a:]
    result += list_b[b:]

    return result


def is_anagram(first_string, second_string):

    first_string_to_lower = first_string.lower()
    second_string_to_lower = second_string.lower()

    first_string = "".join(sort(first_string_to_lower))
    second_string = "".join(sort(second_string_to_lower))

    same_strings = first_string == second_string

    if not first_string or not second_string:
        return (first_string, second_string, False)

    return (first_string, second_string, same_strings)
