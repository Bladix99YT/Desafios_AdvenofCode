from math import factorial


def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def count_possible_combinations():
    total_red = 12
    total_green = 13
    total_blue = 14

    total_combinations = 0

    for red_count in range(total_red + 1):
        for green_count in range(total_green + 1):
            for blue_count in range(total_blue + 1):
                # Verificar se a soma dos cubos selecionados é igual a 12 + 13 + 14
                if red_count + green_count + blue_count == total_red + total_green + total_blue:
                    # Calcular o número de combinações para esta configuração
                    combinations_for_config = (
                        combinations(total_red, red_count) *
                        combinations(total_green, green_count) *
                        combinations(total_blue, blue_count)
                    )
                    total_combinations += combinations_for_config

    return total_combinations


result = count_possible_combinations()
print(f"Número total de combinações possíveis: {result}")
