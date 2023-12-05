with open("input2.txt") as file:
    lines = file.read().strip().split("\n")

mapping = {

    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def extract_numbers(line):
    first_number, last_number = None, None

    # Verificar se há pelo menos um número na linha
    numbers = [char for char in line if char.isdigit()]

    if numbers:
        first_number = int(numbers[0])
        last_number = int(numbers[-1])

    return first_number, last_number


for line in lines:
    first_number, last_number = extract_numbers(line)
