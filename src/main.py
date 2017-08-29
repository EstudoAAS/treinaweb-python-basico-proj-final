from agenda.gerenciadores import GerenciadorContatos
import sys

gerenciador = GerenciadorContatos()

def exibir_contatos(contatos):
    for contato in contatos:
        print(" - {nomeContato}, {tipoContato} = {valorContato}".format(nomeContato=contato.nome,
                                                                        tipoContato=contato.tipo_contato,
                                                                        valorContato=contato.valor_contato))
    print(" * Total de contatos: ",len(contatos))

def listar_contatos():
    print(" ** LISTA DE CONTATOS:")
    try:
        contatos = gerenciador.listar_contatos()
        exibir_contatos(contatos)
    except:
        tipo_erro, valor_erro, traceback = sys.exc_info()
        print(" ** Houve um erro ao listar os contatos: ")
        print(tipo_erro)
        print(valor_erro)


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
        listar_contatos()
    elif opcao == 2:
        print("Adicionar contato")
    elif opcao == 3:
        print("Filtrar contato")
    elif opcao == 4:
        break
    else:
        print(" * Opção invalida! **")
print("Até a próxima! :)")