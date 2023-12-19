class Livro:
    def __init__(self,titulo,autor,id):
        self.titulo=titulo
        self.id=id
        self.autor=autor
        self.status_de_emprestimo=False

class Membro:
    def __init__(self,nome, num_membro):
        self.nome=nome
        self.num_membro = num_membro
        self.historico=[]

        

class Biblioteca:
    def __init__(self):
        self.catalogo_disponiveis=[]
        self.reg_membros=[]

    def adicionar_livros (self,livro):
        self.catalogo_disponiveis.append(livro)
        return "Livro adicionado com sucesso"
    
    def add_membro (self,membro):
        self.reg_membros.append(membro)
        membro_encontrado = ""
        for item_atual in self.reg_membros:
            if item_atual.nome == membro:
                membro_encontrado = item_atual
               
        return membro_encontrado 
        # return "Cliente cadastrado com sucesso"
     

    
    def emprestar_livro (self,membro,livro):
        if livro.status_de_emprestimo == False:
            membro.historico.append(livro)
            livro.status_de_emprestimo = True
            return "Livro emprestado com sucesso"
        else:
            return "Livro não disponível"

    def devolver_livro (self, livro):
        livro.status_de_emprestimo = False

    def pesquisa (self,titulo):
        livro_encontrado = ""
        for item_atual in self.catalogo_disponiveis:
            if item_atual.titulo == titulo:
                livro_encontrado = item_atual
                print(f"""
                      ID: {item_atual.id}
                      Titulo: {item_atual.titulo}
                      Autor: {item_atual.autor}
                      Alugado: {item_atual.status_de_emprestimo}
                      """)
        return livro_encontrado
    def pesquisaMembro (self,nome):
        membro_encontrado = ""
        for item_atual in self.reg_membros:
            if item_atual.nome == nome:
                membro_encontrado = item_atual
                print(f"""
                      Número do membor: {item_atual.num_membro}
                      Nome: {item_atual.nome}
                      """)
        return membro_encontrado
    



biblioteca = Biblioteca()

while True:
    menu= int(input("""
           1. Adicionar livros ao catálogo
           2. Adicionar membros à biblioteca
           3. Emprestar livros.
           4. Registrar a devolução de livros.
           5. Pesquisar por livro
           6. Sair

"""))

    if menu == 1:
        nome_livro= str (input("Digite o nome do livro: "))       
        autor_livro=str (input("Digite o nome do autor: "))
        num_id=int (input("Digite o ID do livro: "))
        livro_qualquer= Livro (titulo=nome_livro, autor=autor_livro,id=num_id)
        biblioteca.adicionar_livros(livro=livro_qualquer)

    elif menu == 2:
        nome_cliente = str (input("Digite o seu nome:"))
        num_cliente = int (input("Digite o seu número de ID: "))    
        cliente_qualquer = Membro (nome=nome_cliente, num_membro=num_cliente)
        biblioteca.add_membro (membro=cliente_qualquer)

    elif menu == 3:
        nome_do_livro=str (input("Digite o titulo do livro que deseja alugar: "))
        nome_do_membro = str (input ("Digite seu nome: "))
        livro_encontrado = biblioteca.pesquisa(nome_do_livro)
        membro_encontrado = biblioteca.pesquisaMembro(nome_do_membro)
        biblioteca.emprestar_livro (membro=membro_encontrado, livro=livro_encontrado)    
    
    elif menu == 4:
        retornar_livro= str (input("Digite o nome do livro a ser retornado: "))
        livro_encontrado = biblioteca.pesquisa(retornar_livro)
        biblioteca.devolver_livro(livro=livro_encontrado)

    elif menu == 5:
        pesquisar_livro= str (input("Digite o titulo do livro que deseja buscar: ")) 
        biblioteca.pesquisa(titulo=pesquisar_livro)  

    else:
        break
            

