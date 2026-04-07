# =========================
# EXERCÍCIOS EM PYTHON
# =========================

# 1. Manipulação de lista
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

print("=== EXERCÍCIO 1 ===")

# a) maior elemento
print("Maior elemento:", max(lista))

# b) menor elemento
print("Menor elemento:", min(lista))

# c) números pares
pares = [num for num in lista if num % 2 == 0]
print("Números pares:", pares)

# d) ocorrências do primeiro elemento
primeiro = lista[0]
print("Ocorrências do primeiro elemento:", lista.count(primeiro))

# e) média dos elementos
media = sum(lista) / len(lista)
print("Média:", media)

# f) soma dos negativos
soma_negativos = sum(num for num in lista if num < 0)
print("Soma dos negativos:", soma_negativos)


# =========================
# 2. Dados do usuário
# =========================
print("\n=== EXERCÍCIO 2 ===")

dados = []
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = input("Digite sua idade: ")

dados.append(nome)
dados.append(sobrenome)
dados.append(idade)

print("Dados informados:", dados)


# =========================
# 3. Notas
# =========================
print("\n=== EXERCÍCIO 3 ===")

notas = []
for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media_notas = sum(notas) / len(notas)

print("Notas:", notas)
print("Média:", media_notas)


# =========================
# 4. Dicionário (dict)
# =========================
print("\n=== EXERCÍCIO 4 ===")

pessoa = {}
pessoa["nome"] = input("Nome: ")
pessoa["idade"] = input("Idade: ")
pessoa["cidade"] = input("Cidade: ")

print("\nDados da pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")


# =========================
# 5. Lista de pessoas
# =========================
print("\n=== EXERCÍCIO 5 ===")

pessoas = []

while True:
    p = {}
    p["nome"] = input("Nome: ")
    p["idade"] = input("Idade: ")
    p["cidade"] = input("Cidade: ")

    pessoas.append(p)

    continuar = input("Deseja adicionar outra pessoa? (s/n): ").lower()
    if continuar != 's':
        break

print("\n=== LISTA DE PESSOAS ===")
for i, pessoa in enumerate(pessoas, start=1):
    print(f"\nPessoa {i}:")
    for chave, valor in pessoa.items():
        print(f"{chave.capitalize()}: {valor}")
