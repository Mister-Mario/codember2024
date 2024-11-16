"""
R (Right)  movernos al siguiente dígito
L (Left)   desplazarnos al dígito anterior
U (Up)     incrementar ese dígito
D (Down)   decrementar el dígito actual

Si llegamos a la derecha del todo y recibimos un R,
volvemos al primer dígito. Si recibimos L y estamos en el primero, 
vamos al último. En el caso de que el dígito actual sea 9
y recibamos una U, pasará a 0. Y si es D y ese dígito es 0, pasará a ser 9
"""

MAX_NUMBER = 9
MIN_NUMBER = 0

combination = input("Give me the problem: ")

splittedCombinations = combination.split(" ")
numbers = splittedCombinations[0]
instructions = splittedCombinations[1]

numbers_array = [int(numbers[i]) for i in range(len(numbers))]

instructions_array = list(instructions)

max_pos = len(numbers) - 1
min_pos = 0

pointer = min_pos

while instructions_array:
    instruction = instructions_array.pop(0)
    if instruction == 'R':
        if(pointer == max_pos):
            pointer = min_pos
        else:
            pointer += 1
    elif instruction == 'L':
        if(pointer == min_pos):
            pointer = max_pos
        else:
            pointer -= 1
    elif instruction == 'U':
        if(numbers_array[pointer] == MAX_NUMBER):
            numbers_array[pointer] = MIN_NUMBER
        else:
            numbers_array[pointer] += 1
    else: #instruction == 'D'
        if(numbers_array[pointer] == MIN_NUMBER):
            numbers_array[pointer] = MAX_NUMBER
        else:
            numbers_array[pointer] -= 1

print(numbers_array)