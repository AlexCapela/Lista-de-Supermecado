#projeto: Sistema de vendas para supermercado 
#objetivo: criar um programa simples para simular compras em um supermercado 
#Funcionalidades principais: 
#cadastrar produtos (nome, preço )
#adicionar produtos ao carrinho (quantidade). 
#exibir resumo da compra, (itens, quantidade, total).
#finalizar compra, (mostrar total geral)

produtos = {}       # Armazena {nome: preço}
carrinho = []       # Lista de itens no carrinho


def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))
    produtos[nome] = preco
    print(f"Produto '{nome}' cadastrado!\n")


def adicionar_ao_carrinho():
    nome = input("Produto para adicionar: ")

    if nome not in produtos:
        print("Produto não encontrado!\n")
        return
    
    quantidade = int(input("Quantidade: "))
    
    carrinho.append({"nome": nome, "preco": produtos[nome], "quantidade": quantidade})
    print(f"{quantidade}x '{nome}' adicionado ao carrinho!\n")


def resumo_da_compra():
    print("\n--- RESUMO DA COMPRA ---")
    
    if not carrinho:
        print("Carrinho vazio!\n")
        return

    total = 0

    for item in carrinho:
        subtotal = item["preco"] * item["quantidade"]
        total += subtotal
        print(f"{item['quantidade']}x {item['nome']} - R$ {subtotal:.2f}")

    print(f"TOTAL PARCIAL: R$ {total:.2f}\n")


def finalizar_compra():
    print("\n--- FINALIZANDO COMPRA ---")
    
    total = sum(item["preco"] * item["quantidade"] for item in carrinho)

    print(f"TOTAL A PAGAR: R$ {total:.2f}")
    print("Obrigado pela compra!\n")



# MENU PRINCIPAL

while True:
    print("""
----- SUPERMERCADO -----
1 - Cadastrar produto
2 - Adicionar ao carrinho
3 - Resumo da compra
4 - Finalizar compra
5 - Sair
""")

    opc = input("Escolha uma opção: ")

    if opc == "1":
        cadastrar_produto()
    elif opc == "2":
        adicionar_ao_carrinho()
    elif opc == "3":
        resumo_da_compra()
    elif opc == "4":
        finalizar_compra()
    elif opc == "5":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida!\n")
