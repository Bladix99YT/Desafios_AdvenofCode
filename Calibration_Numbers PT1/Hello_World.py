# Exemplo de lista de strings simulando linhas do documento
lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet", "no_numbers"]

# Função para extrair o primeiro e último número de uma linha


def extraction_numbers(line):
    first_number, last_number = None, None

    # Verificar se há pelo menos um número na linha
    numbers = [char for char in line if char.isdigit()]

    if numbers:
        first_number = int(numbers[0])
        last_number = int(numbers[-1])

    return first_number, last_number


# Iterar sobre cada linha
for line in lines:
    # Chamar a função para extrair números
    first_number, last_number = extraction_numbers(line)

    # Imprimir os valores para cada linha
    print(f"Line: {line}, First Number: {
          first_number}, Last Number: {last_number}")
    