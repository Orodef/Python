def remove_duplicates(numbers):
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result
