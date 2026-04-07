# =========================
# LISTA DE EXERCÍCIOS 2
# =========================

# 1. Tupla
print("=== EXERCÍCIO 1 ===")
tupla = (10, 20, 30)
print("Tupla original:", tupla)

try:
    tupla[0] = 100  # Isso vai gerar erro
except TypeError as e:
    print("Erro ao tentar alterar tupla:", e)


# =========================
# 2. Dicionário aluno
# =========================
print("\n=== EXERCÍCIO 2 ===")
aluno = {
    "nome": "Ana",
    "idade": 22,
    "curso": "ADS"
}

print("Nome do aluno:", aluno["nome"])

aluno["nota"] = 9.5
print("Dicionário atualizado:", aluno)


# =========================
# 3. Lista
# =========================
print("\n=== EXERCÍCIO 3 ===")
lista = [1, 2, 3, 4, 5]
print("Lista inicial:", lista)

lista.append(6)
print("Após adicionar:", lista)

lista.pop(2)  # remove terceiro elemento (índice 2)
print("Lista final:", lista)


# =========================
# 4. Remover duplicados
# =========================
print("\n=== EXERCÍCIO 4 ===")
numeros = [1, 2, 2, 3, 4, 4, 5]
sem_duplicados = list(set(numeros))
print("Sem duplicados:", sem_duplicados)


# =========================
# 5. Produto
# =========================
print("\n=== EXERCÍCIO 5 ===")
produto = {
    "nome": "Teclado",
    "preco": 100.0
}

print("Preço:", produto["preco"])

produto["preco"] *= 0.9  # desconto de 10%
print("Preço com desconto:", produto["preco"])


# =========================
# 6. Notas de alunos
# =========================
print("\n=== EXERCÍCIO 6 ===")
alunos = {
    "João": 8.5,
    "Maria": 9.0,
    "Pedro": 7.5
}

nome = input("Digite o nome do aluno: ")
if nome in alunos:
    print(f"Nota de {nome}:", alunos[nome])
else:
    print("Aluno não encontrado")


# =========================
# 7. Nomes únicos
# =========================
print("\n=== EXERCÍCIO 7 ===")
nomes = ["Ana", "João", "Ana", "Maria", "João"]
nomes_unicos = list(set(nomes))
print("Nomes únicos:", nomes_unicos)


# =========================
# 8. Coordenadas
# =========================
print("\n=== EXERCÍCIO 8 ===")
coordenadas = (-3.12, -60.02)
print("Coordenadas:", coordenadas)

try:
    coordenadas[0] = 0
except TypeError as e:
    print("Erro ao tentar alterar coordenadas:", e)


# =========================
# 9. Funcionários
# =========================
print("\n=== EXERCÍCIO 9 ===")

funcionarios = {
    "Carlos": {"cargo": "Gerente", "salario": 3000},
    "Ana": {"cargo": "Analista", "salario": 2500},
    "João": {"cargo": "Dev", "salario": 2800}
}

nome = input("Digite o nome do funcionário para atualizar salário: ")
if nome in funcionarios:
    novo_salario = float(input("Novo salário: "))
    funcionarios[nome]["salario"] = novo_salario
else:
    print("Funcionário não encontrado")

print("\nFuncionários cadastrados:")
for nome, dados in funcionarios.items():
    print(f"{nome} - Cargo: {dados['cargo']} - Salário: {dados['salario']}")


# =========================
# 10. Linguagens
# =========================
print("\n=== EXERCÍCIO 10 ===")

respostas = [
    "Python", "Java", "Python", "C++", "Java",
    "Python", "JavaScript", "Python", "C++"
]

linguagens_unicas = set(respostas)
print("Linguagens únicas:", linguagens_unicas)

contagem = {}
for linguagem in respostas:
    contagem[linguagem] = contagem.get(linguagem, 0) + 1

print("Contagem:", contagem)

mais_escolhida = max(contagem, key=contagem.get)
print("Mais escolhida:", mais_escolhida)
