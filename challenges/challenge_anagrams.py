def is_anagram(first_string, second_string):
    """Verifica se duas strings são anagramas."""
    if not first_string or not second_string:
        return first_string, second_string, False

    if len(first_string) == 0 or len(second_string) == 0:
        return False

    fs = first_string.lower()
    ss = second_string.lower()

    first_list = merge_sort(fs)
    second_list = merge_sort(ss)

    return "".join(first_list), "".join(second_list), first_list == second_list


def merge_sort(string):
    if len(string) <= 1:
        return string

    middle = len(string) // 2
    left = merge_sort(string[:middle])
    right = merge_sort(string[middle:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].lower() < right[j].lower():
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return "".join(merged)
