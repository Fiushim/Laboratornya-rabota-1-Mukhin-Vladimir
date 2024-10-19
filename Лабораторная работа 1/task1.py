numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers_ = numbers[0:4] + numbers[5:]

averange_of_numbers = sum(numbers_)/len(numbers)

numbers[4] = averange_of_numbers

print("Измененный список:", numbers)
