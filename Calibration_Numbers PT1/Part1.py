# Abrir o arquivo em modo de leitura ('r')
with open("input.txt") as file:
    lines = file.read().strip().split("\n")

# Função para extrair o primeiro e último número de uma linha


def extract_numbers(line):
    first_number, last_number = None, None

    # Verificar se há pelo menos um número na linha
    numbers = [char for char in line if char.isdigit()]

    if numbers:
        first_number = int(numbers[0])
        last_number = int(numbers[-1])

    return first_number, last_number


# Variável para armazenar a soma total
total_sum = 0

# Iterar sobre cada linha
for line in lines:
    # Chamar a função para extrair números
    first_number, last_number = extract_numbers(line)

    # Imprimir os valores para cada linha
    print(f"Line: {line}, First Number: {
          first_number}, Last Number: {last_number}")

    # Adicionar a soma total
    total_sum += first_number * 10 + last_number

# Imprimir a soma total
print(f"Soma total dos números de dois dígitos: {total_sum}")
