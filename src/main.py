print(" ** BEM-VINDO! **")
while True:
    print("\n\n\nO que você deseja fazer? \n ")
    print("1. Listar contatos...")
    print("2. Adcionar novo contato...")
    print("3. Pesquisar contato por nome...")
    print("4. Sair")
    print("\n")
    opcao = int(input("Opção selecionada -> "))
    if opcao == 1:
        print("Listar contatos")
    elif opcao == 2:
        print("Adicionar contato")
    elif opcao == 3:
        print("Filtrar contato")
    elif opcao == 4:
        break
    else:
        print(" * Opção invalida! **")
print("Até a próxima! :)")