def median(numbers):
    medium = []
    result = 0
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        place = len(numbers) / 2
        medium.append(numbers[place])
        medium.append(numbers[place - 1])
        result = (medium[0] + medium[1]) / (2.0)
    else:
        place = (len(numbers) - 1) / 2
        result = numbers[place]
    return result
