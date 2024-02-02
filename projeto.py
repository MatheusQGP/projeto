contador_id_livro = 1
contador_id_membro = 1

class Livro:
    def __init__(self, id:int, titulo:str, autor:str) -> None:
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.status_disponivel = True
    
class Membro:
    def __init__(self, id: int, nome:str) -> None:
        self.id = id
        self.nome = nome
        self.historico = []

    
class Biblioteca:
    def __init__(self) -> None:
        self.catalogo_livros = []
        self.registro_membros = []
    
    def adicionar_membro(self):
        global contador_id_membro
        nome_do_membro = str(input("Digite o nome do membro: "))

        membro = Membro(nome=nome_do_membro, id=contador_id_membro)

        contador_id_membro += 1

        self.registro_membros.append(membro)

        return "Membro adicionado com sucesso"


    def adicionar_livro(self):
        global contador_id_livro

        titulo_do_livro = str(input("Digite o título do livro: "))
        autor_do_livro = str(input("Digite o autor do livro: "))

        livro = Livro(titulo=titulo_do_livro, autor=autor_do_livro, id=contador_id_livro)

        contador_id_livro += 1

        self.catalogo_livros.append(livro)

        return "Livro adicionado com sucesso"


    def pesquisar_livro(self):
        escolha = str(input("Digite o ID ou Título do livro que você deseja: "))

        for livro_atual in self.catalogo_livros:
            if livro_atual.titulo == escolha or livro_atual.id == int(escolha):
                print(f"""
            Informações do Livro pesquisado:
            ID do livro: {livro_atual.id}
            Título do livro: {livro_atual.titulo}
            Autor do livro: {livro_atual.autor}
            Status do livro: {livro_atual.status}
""")    
            else:
                print("Livro não encontrado")


    def pegar_livro_emprestado(self):
        id_membro = int(input("Digite o ID do membro que vai pegar o livro emprestado: "))
        for membro_atual in self.registro_membros:
            if membro_atual.id == id_membro:
                id_livro = int(input(f"{membro_atual.nome} escolha o ID do livro que você quer emprestado: "))
                for livro_atual in self.catalogo_livros:
                    if livro_atual.id == id_livro:
                        if livro_atual.status_disponivel:
                            livro_atual.status_disponivel = False
                            membro_atual.historico.append(livro_atual)
                            return "Livro emprestado com sucesso"
                        else:
                            return "Livro encontrado porém já está emprestado"
                    else:
                        return "Livro não encontrado"
            else:
                return "Membro não encontrado"
            
    def devolver_livro(self):
        pass


biblioteca1 = Biblioteca()

while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Adicionar Livro
    2 - Adicionar Membro
    3 - Pesquisar Livro
    4 - Pegar Livro Emprestado
    5 - Devolver Livro             
    0 - Sair
"""))
    
    match menu:
        case 1:
            print(biblioteca1.adicionar_livro())
        case 2:
            print(biblioteca1.adicionar_membro())
        case 3:
            print(biblioteca1.pesquisar_livro())
        case 4:
            print(biblioteca1.pegar_livro_emprestado())
        case 5:
            print(biblioteca1.devolver_livro())
        case 0:
            break
        case _:
            print("Opção inválida")
            