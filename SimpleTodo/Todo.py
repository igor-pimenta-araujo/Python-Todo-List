# Função para adicionar uma tarefa à lista
def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    todo_list.append({"tarefa": tarefa, "concluida": False})
    print("Tarefa adicionada com sucesso!")

# Função para exibir todas as tarefas da lista
def exibir_tarefas():
    if len(todo_list) == 0:
        print("A lista de tarefas está vazia.")
    else:
        print("Lista de tarefas:")
        for i, item in enumerate(todo_list):
            concluida = "[x]" if item["concluida"] else "[ ]"
            print(f"{i + 1}. {concluida} {item['tarefa']}")

# Função para remover uma tarefa da lista
def remover_tarefa():
    exibir_tarefas()
    indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
    if indice >= 0 and indice < len(todo_list):
        tarefa_removida = todo_list.pop(indice)
        print(f"Tarefa '{tarefa_removida['tarefa']}' removida com sucesso!")
    else:
        print("Índice inválido.")

# Função para marcar uma tarefa como concluída
def marcar_tarefa_concluida():
    exibir_tarefas()
    indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
    if indice >= 0 and indice < len(todo_list):
        todo_list[indice]["concluida"] = True
        print("Tarefa marcada como concluída.")
    else:
        print("Índice inválido.")

# Função para desmarcar uma tarefa como concluída
def desmarcar_tarefa_concluida():
    exibir_tarefas()
    indice = int(input("Digite o número da tarefa que deseja desmarcar como concluída: ")) - 1
    if indice >= 0 and indice < len(todo_list):
        todo_list[indice]["concluida"] = False
        print("Tarefa desmarcada como concluída.")
    else:
        print("Índice inválido.")

# Função para salvar a lista de tarefas em um arquivo de texto
def salvar_tarefas():
    nome_arquivo = input("Digite o nome do arquivo para salvar as tarefas: ")
    with open(nome_arquivo, "w") as arquivo:
        for item in todo_list:
            arquivo.write(f"{item['tarefa']},{item['concluida']}\n")
    print("Tarefas salvas com sucesso!")

# Função para carregar a lista de tarefas de um arquivo de texto
def carregar_tarefas():
    nome_arquivo = input("Digite o nome do arquivo para carregar as tarefas: ")
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            todo_list.clear()
            for linha in linhas:
                tarefa, concluida = linha.strip().split(",")
                todo_list.append({"tarefa": tarefa, "concluida": concluida == "True"})
        print("Tarefas carregadas com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

# Loop principal do programa
todo_list = []

while True:
    print("\n----- TODO List -----")
    print("1. Adicionar tarefa")
    print("2. Exibir tarefas")
    print("3. Remover tarefa")
    print("4. Marcar tarefa como concluída")
    print("5. Desmarcar tarefa como concluída")
    print("6. Salvar tarefas em um arquivo")
    print("7. Carregar tarefas de um arquivo")
    print("8. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        exibir_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        marcar_tarefa_concluida()
    elif opcao == "5":
        desmarcar_tarefa_concluida()
    elif opcao == "6":
        salvar_tarefas()
    elif opcao == "7":
        carregar_tarefas()
    elif opcao == "8":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, digite um número válido.")
