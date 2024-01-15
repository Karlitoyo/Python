def hasEvenNumber(numbers: list) -> bool:
    for number in numbers:
        if number % 2 == 0:
            return True
    return False

numbers_list = [1, 3, 5, 7, 8, 9, 10]
result = hasEvenNumber(numbers_list)
print(result)

cylinder_volume = lambda r, h: 3.14159265358979323846 * r**2 * h

radius = 3.0
height = 5.0
volume = cylinder_volume(radius, height)
print(f"Volume of the cylinder is {volume:.2f}.")
