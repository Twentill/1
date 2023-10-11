def even_or_odd(number):
    if number % 2 == 0: 
        return "Even"
    else:
        return "Odd"


def multiply(a, b):
    return a * b


def positive_sum(arr):
    result = 0
    for num in arr:
        if num > 0:
            result += num 
    return result


def make_negative( number ):
    if number < 0:
        return number
    else:
        return number * -1


def solution(string):
    word = string
    revers = word[::-1]
    return revers
