def adicionar_contato(agenda, nome_contato):
    contato = {"contato":nome_contato, "favorito":False}
    agenda.append(contato)
    print(f'{nome_contato} adicionado na agenda com sucesso!')
    return

def visualizar_agenda(agenda):
    print("\nLista de contatos:")
    for indice, contato in enumerate(agenda, start=1): 
        favorito = "☆" if contato["favorito"] else " "
        nome_contato = contato['contato']
        print(f'{indice}. {nome_contato} {favorito}')
    return

def atualizar_nome_agenda(agenda, indice_contato, novo_nome_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
        agenda[indice_contato_ajustado]["contato"] = novo_nome_contato
        print(f"Contato {indice_contato} atualizado para {novo_nome_contato}")
    else: 
        print("Índice de contato inválido")
    return

def favoritar_desvaforitar_contato(agenda, indice_contato): 
    indice_contato_ajustado = int(indice_contato) - 1 
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
        agenda[indice_contato_ajustado]["favorito"] = False if agenda[indice_contato_ajustado]["favorito"] else True
        print(f"Contato {indice_contato} favoritado/desfavoritado")
    return

def visualizar_favoritos_agenda(agenda):
    print("\nLista de contatos favoritos:")
    if len(agenda) > 0 : 
        for indice, contato in enumerate(agenda, start=1): 
            favorito = "☆" if contato["favorito"] else " "
            nome_contato = contato['contato']
            if contato["favorito"]: 
                print(f'{indice}. {nome_contato} {favorito}')
    else:
        print("Você não tem contato salvo como favorito")
    return

def deletar_contato(agenda, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1 
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
        del agenda[indice_contato_ajustado]
        print(f"Contato exluido")
    else: 
        print("Índice de contato inválido")
    return

agenda = []
while True: 
    print("\nMenu da agenda:")
    print("1 - Adicionar um contato")
    print("2 - Visualizar lista de contato")
    print("3 - Editar contato")
    print("4 - Marcar/Desmarcar favorito no contato")
    print("5 - Lista de favoritos")
    print("6 - Apagar contato")
    print("7 - Sair do menu")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato: ")
        adicionar_contato(agenda, nome_contato)
    elif escolha == "2":
        visualizar_agenda(agenda)
    elif escolha == "3": 
        visualizar_agenda(agenda)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome_contato = input("Digite o novo nome desse contato: ")
        atualizar_nome_agenda(agenda, indice_contato, novo_nome_contato)
    elif escolha == "4": 
        visualizar_agenda(agenda)
        indice_contato = input("Digite o número do contato que deseja favoritar ou desmarcar como favorito: ")
        favoritar_desvaforitar_contato(agenda, indice_contato)
    elif escolha == "5":
        visualizar_favoritos_agenda(agenda)
    elif escolha == "6": 
        visualizar_agenda(agenda)
        indice_contato = input("Digite o número do contato que deseja excluir: ")
        deletar_contato(agenda, indice_contato)    
    elif escolha == "7":
        break