#Aqui vou desenvolver meu código de teste para a revisão.

# Lista (array) principal para armazenar os dicionários de motores
motores = []
proximo_id = 1


def exibir_menu():
    print("\n=== SISTEMA DE CADASTRO DE MOTORES ===")
    print("1. Cadastrar novo motor")
    print("2. Listar todos os motores")
    print("3. Buscar motor por número de série")
    print("4. Remover motor por ID")
    print("0. Sair")
    return input("Escolha uma opção: ")


def cadastrar_motor():
    global proximo_id
    print("\n--- Novo Cadastro ---")
    modelo = input("Modelo do motor (ex: WEG W22): ").strip()
    potencia = input("Potência em CV (ex: 5.0): ").strip()
    tensao = input("Tensão nominal em V (ex: 220/380): ").strip()
    rpm = input("Rotação em RPM (ex: 1750): ").strip()
    num_serie = input("Número de série: ").strip()

    # Verifica se o número de série já existe
    for motor in motores:
        if motor["num_serie"].lower() == num_serie.lower():
            print("Erro: Já existe um motor cadastrado com este número de série!")
            return

    novo_motor = {
        "id": proximo_id,
        "modelo": modelo,
        "potencia_cv": potencia,
        "tensao_v": tensao,
        "rpm": rpm,
        "num_serie": num_serie,
    }

    motores.append(novo_motor)
    proximo_id += 1
    print(f"Motor '{modelo}' cadastrado com sucesso! (ID: {novo_motor['id']})")


def listar_motores():
    print("\n--- Motores Cadastrados ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    for m in motores:
        print(
            f"ID: {m['id']} | Modelo: {m['modelo']} | Potência: {m['potencia_cv']} CV | "
            f"Tensão: {m['tensao_v']} V | RPM: {m['rpm']} | Série: {m['num_serie']}"
        )


def buscar_motor():
    print("\n--- Buscar Motor ---")
    termo = input("Digite o número de série: ").strip().lower()

    for m in motores:
        if m["num_serie"].lower() == termo:
            print("\nMotor encontrado:")
            print(f"  ID: {m['id']}")
            print(f"  Modelo: {m['modelo']}")
            print(f"  Potência: {m['potencia_cv']} CV")
            print(f"  Tensão: {m['tensao_v']} V")
            print(f"  Rotação: {m['rpm']} RPM")
            print(f"  Número de Série: {m['num_serie']}")
            return

    print("Nenhum motor encontrado com esse número de série.")


def remover_motor():
    print("\n--- Remover Motor ---")
    if not motores:
        print("A lista está vazia.")
        return

    try:
        id_alvo = int(input("Digite o ID do motor que deseja remover: "))
    except ValueError:
        print("ID inválido. Digite apenas números.")
        return

    for i, m in enumerate(motores):
        if m["id"] == id_alvo:
            removido = motores.pop(i)
            print(f"Motor '{removido['modelo']}' (ID {id_alvo}) removido com sucesso.")
            return

    print(f"Motor com ID {id_alvo} não encontrado.")


def iniciar_sistema():
    # Pré-populando com 2 motores para facilitar seus testes iniciais
    global proximo_id
    motores.extend([
        {
            "id": 1,
            "modelo": "WEG W22 IR3 Premium",
            "potencia_cv": "10.0",
            "tensao_v": "220/380",
            "rpm": "1760",
            "num_serie": "SN-1001",
        },
        {
            "id": 2,
            "modelo": "Siemens 1LE0",
            "potencia_cv": "3.0",
            "tensao_v": "380/660",
            "rpm": "3500",
            "num_serie": "SN-1002",
        },
    ])
    proximo_id = 3

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            buscar_motor()
        elif opcao == "4":
            remover_motor()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Ponto de entrada do programa
if __name__ == "__main__":
    iniciar_sistema()