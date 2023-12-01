precos = [1000, 1500, 1250, 2500]


def adicionar_imposto(preco):
    return preco * 1.1


precos_imposto = []
for precos in precos:
    precos_imposto.append(adicionar_imposto(precos))

print(precos_imposto)
