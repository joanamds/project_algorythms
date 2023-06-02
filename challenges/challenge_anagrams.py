def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(string):
    """Ordena os caracteres de uma string."""
    if len(string) <= 1:
        return string

    middle = len(string) // 2
    left = string[:middle]
    right = string[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def is_anagram(first_string, second_string):
    """Verifica se duas strings são anagramas."""
    if not first_string or not second_string:
        return '', '', False

    if len(first_string) != len(second_string):
        return first_string, second_string, False

    if len(first_string) == 0 or len(second_string) == 0:
        return '', '', False

    fs = first_string.lower()
    ss = second_string.lower()

    first_list = merge_sort(fs)
    second_list = merge_sort(ss)

    return "".join(first_list), "".join(second_list), first_list == second_list
