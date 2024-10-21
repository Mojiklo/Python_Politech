numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
su = sum(numbers[:4]) + sum(numbers[5:])
co = len(numbers)
ar = su / co
numbers[4] = ar
print("Измененный список:", numbers)
