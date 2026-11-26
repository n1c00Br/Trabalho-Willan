import json
import os

arquivo_dados = "dados.json"

def carregar():
    if os.path.exists(arquivo_dados):
        with open(arquivo_dados, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def salvar(lista):
    with open(arquivo_dados, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

def listar(lista):
    if len(lista) == 0:
        print("Nenhum registro cadastrado.")
        return
    
    for i in range(len(lista)):
        item = lista[i]
        print(i, "- Nome:", item["nome"], "| Cidade:", item["cidade"], "| Idade:", item["idade"])

def incluir(lista):
    nome = input("Digite o nome: ")
    cidade = input("Digite a cidade: ")
    idade = int(input("Digite a idade: "))

    pessoa = {
        "nome": nome,
        "cidade": cidade,
        "idade": idade
    }

    lista.append(pessoa)
    salvar(lista)
    print("Cadastro realizado!")

def alterar(lista):
    listar(lista)
    if len(lista) == 0:
        return

    pos = int(input("Digite o numero do registro que quer alterar: "))
    if pos >= 0 and pos < len(lista):
        lista[pos]["nome"] = input("Novo nome: ")
        lista[pos]["cidade"] = input("Nova cidade: ")
        lista[pos]["idade"] = int(input("Nova idade: "))
        salvar(lista)
        print("Registro alterado!")
    else:
        print("Numero invalido.")

def excluir(lista):
    listar(lista)
    if len(lista) == 0:
        return

    pos = int(input("Digite o numero do registro que quer excluir: "))
    if pos >= 0 and pos < len(lista):
        lista.pop(pos)
        salvar(lista)
        print("Registro excluido!")
    else:
        print("Numero invalido.")

def pesquisar(lista):
    if len(lista) == 0:
        print("Nenhum registro cadastrado.")
        return

    print("1 - Pesquisar por nome")
    print("2 - Pesquisar por cidade")
    op = input("Escolha: ")
    busca = input("Digite o texto da pesquisa: ").lower()

    achou = False
    for item in lista:
        if op == "1" and busca in item["nome"].lower():
            print("Nome:", item["nome"], "| Cidade:", item["cidade"], "| Idade:", item["idade"])
            achou = True
        elif op == "2" and busca in item["cidade"].lower():
            print("Nome:", item["nome"], "| Cidade:", item["cidade"], "| Idade:", item["idade"])
            achou = True

    if not achou:
        print("Nenhum resultado encontrado.")

# Ordenacao usando laços igual ao exemplo visto em aula
def ordenar_e_imprimir(lista):
    if len(lista) == 0:
        print("Nenhum registro cadastrado.")
        return

    print("1 - Ordenar por Nome")
    print("2 - Ordenar por Idade")
    op = input("Escolha: ")

    copia = lista.copy()

    if op == "1":
        for i in range(len(copia)):
            for j in range(len(copia) - 1):
                if copia[j]["nome"].lower() > copia[j + 1]["nome"].lower():
                    aux = copia[j]
                    copia[j] = copia[j + 1]
                    copia[j + 1] = aux
        print("\n--- Lista Ordenada por Nome ---")
        listar(copia)

    elif op == "2":
        for i in range(len(copia)):
            for j in range(len(copia) - 1):
                if copia[j]["idade"] > copia[j + 1]["idade"]:
                    aux = copia[j]
                    copia[j] = copia[j + 1]
                    copia[j + 1] = aux
        print("\n--- Lista Ordenada por Idade ---")
        listar(copia)
    else:
        print("Opcao invalida.")

dados = carregar()

while True:
    print("\n--- MENU ---")
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Pesquisar")
    print("5 - Imprimir ordenado")
    print("6 - Listar tudo")
    print("0 - Sair")

    opcao = input("Opcao: ")

    if opcao == "1":
        incluir(dados)
    elif opcao == "2":
        alterar(dados)
    elif opcao == "3":
        excluir(dados)
    elif opcao == "4":
        pesquisar(dados)
    elif opcao == "5":
        ordenar_e_imprimir(dados)
    elif opcao == "6":
        listar(dados)
    elif opcao == "0":
        salvar(dados)
        print("Programa finalizado.")
        break
    else:
        print("Opcao invalida.")