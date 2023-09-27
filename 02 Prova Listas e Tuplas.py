# Recebe as duas listas do usuário
lista1 = input("Digite os elementos da Lista 1 separados por espaço: ").split()
lista2 = input("Digite os elementos da Lista 2 separados por espaço: ").split()

# Converte os elementos para inteiros
lista1 = [int(x) for x in lista1]
lista2 = [int(x) for x in lista2]

# Encontra os elementos em comum entre as listas
elementos_em_comum = set(lista1) & set(lista2)

# Calcula a soma dos elementos em comum
soma_elementos = sum(elementos_em_comum)

# Retorna uma tupla com os elementos em comum e a soma
resultado = (list(elementos_em_comum), soma_elementos)

# Exibe o resultado
print(resultado)
