


def sum_10(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 10
    
    return wrapper

@sum_10
def multiplier(param : int):
    return param *2

print(multiplier(20))









def is_even(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        final_result = []
        for i in result:
            if i % 2 == 0:
                final_result.append(i)
        return final_result
    return wrapper

@is_even
def divisible_by_3(lst):
    numbers = []
    for i in lst:
        if i % 3 == 0:
            numbers.append(i)
    return numbers
    
check = [i for i in range(100)]

print(divisible_by_3(check))









def  there_are_vowels(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        letters = []
        Vowels = "aeiouAEIOU"
        for i in result:
            if i in Vowels:
                continue
            else:
                letters.append(i)
        return letters
    return wrapper

@there_are_vowels
def check_for_numbers(lst):
    new_list = []
    for i in lst:
        if isinstance(i, int):
            continue
        else:
            new_list.append(i)
    return new_list
            
print(check_for_numbers([1, 2, 'A', 'e', 34, 'b', 'c']))



class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def area(self):
        return self._length * self._width
    
    @property
    def double_area(self):
        return (self._length * self._width) * 2

cubo = Rectangle(2, 6)

print(cubo.double_area)