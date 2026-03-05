def get_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def get_avg(numbers):
    return get_sum(numbers) / len(numbers)

def get_highest(numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest

def get_lowest(numbers):
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
    return lowest
