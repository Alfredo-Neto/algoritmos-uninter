class CrudColaboradores:
    def __init__(self):
        self.lista_colaboradores = []
        self.id_global = 0

    def cadastrar_colaborador(self, id):
        print("*****************************************************************************")
        print("------------------------MENU CADASTRAR COLABORADOR---------------------------")
        
        formatted_string = "id do colaborador {}".format(id)
        print(formatted_string)

        nome = input("Por favor entre com o nome: ")
        setor = input("Por favor entre com o setor: ")
        salario = float(input("Por favor entre com o pagamento (R$): "))
        
        colaborador = {
					"id": id,
					"nome": nome,
					"setor": setor,
					"salario": salario
        }
        
        self.lista_colaboradores.append(colaborador)
        print("Colaborador cadastrado com sucesso!")

    def consultar_colaborador(self):
        print("*****************************************************************************")
        print("------------------------MENU CONSULTAR COLABORADOR---------------------------")
        while True:
            opcao = input(
                "Escolha a opção desejada:\n"
                "1 - Consultar Todos os Colaboradores\n"
                "2 - Consultar Colaborador por id\n"
                "3 - Consultar Colaborador(es) por setor\n"
                "4 - Retornar\n"
                )
            
            if opcao == "1":
                self.consultar_todos()
            elif opcao == "2":
                self.consultar_por_id()
            elif opcao == "3":
                self.consultar_por_setor()
            elif opcao == "4":
                break
            else:
                print("Opção inválida!")

    def consultar_todos(self):
        print("\nTodos os colaboradores:")
        for colaborador in self.lista_colaboradores:
            self.mostrar_colaborador(colaborador)

    def consultar_por_id(self):
        id = int(input("Informe o ID do colaborador: "))
        encontrado = False
        
        for colaborador in self.lista_colaboradores:
            if colaborador["id"] == id:
                self.mostrar_colaborador(colaborador)
                encontrado = True
                break
        
        if not encontrado:
            print("Colaborador não encontrado!")

    def consultar_por_setor(self):
        setor = input("Informe o setor: ")
        encontrados = []
        
        for colaborador in self.lista_colaboradores:
            if colaborador["setor"] == setor:
                self.mostrar_colaborador(colaborador)
                encontrados.append(colaborador)
        
        if not encontrados:
            print("Nenhum colaborador encontrado no setor especificado!")

    def remover_colaborador(self):
        print("*****************************************************************************")
        print("------------------------MENU REMOVER COLABORADOR---------------------------")
        
        id = int(input("Informe o ID do colaborador a ser removido: "))
        removido = False
        
        for colaborador in self.lista_colaboradores:
            if colaborador["id"] == id:
                self.lista_colaboradores.remove(colaborador)
                print("Colaborador removido com sucesso!")
                removido = True
                break
        
        if not removido:
            print("Colaborador não encontrado!")

    def mostrar_colaborador(self, colaborador):
        print("-" * 30)
        print(f"id: {colaborador['id']}")
        print(f"nome: {colaborador['nome']}")
        print(f"setor: {colaborador['setor']}")
        print(f"pagamento: {colaborador['salario']:.2f}")
        print("-" * 30)
    

def main():
    crud = CrudColaboradores()
    
    print("Bem-vindo ao Controle de Colaboradores do Alfredo de Aguiar Braule Pinto Neto")
    print("*****************************************************************************")
    print("-----------------------------Menu Principal----------------------------------")
    
    while True:
        opcao = input(
                "Escolha a opção desejada:\n"
                "1 - Cadastrar Colaborador\n"
                "2 - Consultar Colaborador(es)\n"
                "3 - Remover Colaborador\n"
                "4 - Sair\n"
                )
        
        if opcao == "1":
            crud.id_global += 1
            crud.cadastrar_colaborador(crud.id_global)
        elif opcao == "2":
            crud.consultar_colaborador()
        elif opcao == "3":
            crud.remover_colaborador()
        elif opcao == "4":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
