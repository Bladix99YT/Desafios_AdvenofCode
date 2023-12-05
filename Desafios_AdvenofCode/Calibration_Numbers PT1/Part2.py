with open("Calibration_Numbers PT1/Part2.py") as file:
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


def convert_Word_to_Number(word):
    return mapping.get(word, 0)


def extract_numbers(line):
    first_number, last_number = None, None

    # Verificar se há pelo menos um número na linha
    words = line.split()

    if words:
        first_number = convert_Word_to_Number(words[0])
        last_number = convert_Word_to_Number(words[-1])

    return first_number, last_number


for line in lines:
    first_number, last_number = extract_numbers(line)

    print(f"Line: {line}, First Number: {
          first_number}, Last Number: {last_number}")

    total_sum = 0
    total_sum += first_number * 10 + last_number

    if first_number is not None and last_number is not None:
        total_sum += first_number * 10 + last_number

    print(f"Soma total dos números de dois dígitos: {total_sum}")
