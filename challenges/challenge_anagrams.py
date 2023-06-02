def is_anagram(first_string, second_string):
    """Verifica se duas strings são anagramas."""
    if (
        not isinstance(first_string, str)
        or not isinstance(second_string, str)
    ):
        return first_string, second_string, False

    if first_string == "" and second_string == "":
        return first_string, second_string, False

    fs = first_string.lower() if first_string else ""
    ss = second_string.lower() if second_string else ""

    ordered_first_string = "".join(merge_sort(list(fs)))
    ordered_second_string = "".join(merge_sort(list(ss)))

    return (
        ordered_first_string,
        ordered_second_string,
        ordered_first_string == ordered_second_string,
    )


def merge_sort(lst):
    """Ordena uma lista."""
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    return merge(left, right)


def merge(left, right):
    """Combina duas listas ordenadas em uma única lista ordenada."""
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
