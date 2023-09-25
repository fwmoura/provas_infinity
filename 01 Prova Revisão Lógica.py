# Solicita a quantidade de alunos na turma
quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))

# Inicializa a variável que irá armazenar a soma das idades
soma_idades = 0

# Loop FOR para receber as idades dos alunos
for i in range(quantidade_alunos):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    
    # Adiciona a idade à soma
    soma_idades += idade

# Inicializa um contador
contador = 0

# Loop WHILE para realizar a soma das idades
while contador < quantidade_alunos:
    # Leitura da idade não é necessária no loop WHILE, pois já foi feita no loop FOR
    contador += 1

# Calcula a média das idades
media_idades = soma_idades / quantidade_alunos

# Exibe a média de idade da turma
print(f"A média de idade da turma é: {media_idades:.2f}")
