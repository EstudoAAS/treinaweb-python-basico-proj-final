from os.path import exists
from agenda.modelos import Contato
from agenda.enuns import TipoContato

class GerenciadorContatos:

    __contatos = []

    def listar_contatos(self):
        self.__contatos.clear()
        if exists("agenda.txt"):
            with open("agenda.txt", "r") as leitor:
                linhas = leitor.readline()
                for linha in linhas:
                    informacoes_contato = linha.split("|")
                    contato = Contato()
                    contato.nome = informacoes_contato[0]
                    contato.tipo_contato = TipoContato(int(informacoes_contato[1]))
                    contato.valor_contato = informacoes_contato[2].replace("\n","")
                    self.__contatos.append(contato)
        return self.__contatos

    def incluir_contato(self, contato):
        pass

    def pesquisar_contato_por_nome(self, nome_contato):
        pass