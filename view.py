from  controller import ControllerCadastro, ControllerLogin

def menu():
    print("Escolha uma das opções:")
    print("1. Registrar")
    print("2. Login")
    print("3. Sair")

    option = input("Digite sua opção: ")

    match option:
        case '1':
            print("Registro de novo usuário")
            name = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            pwd = input("Digite sua senha: ")

            result = ControllerCadastro.register(name, email, pwd)
            if result == 1:
                print("Usuário cadastrado com sucesso!")
                print("Nome inválido. Deve conter entre 3 e 50 caracteres.")
            elif result == 3:
                print("Email muito longo. Deve conter até 200 caracteres.")
            elif result == 4:
                print("Senha inválida. Deve conter no mínimo 6 caracteres.")
            elif result == 5:
                print("Email já cadastrado.")
            else:
                print("Erro ao cadastrar usuário.")

        case '2':
            print("Login de usuário")
            email = input("Digite seu email: ")
            pwd = input("Digite sua senha: ")

            result = ControllerLogin.login(email, pwd)
            if result:
                print(f"Login bem-sucedido! ID do usuário: {result['id']}")
            else:
                print("Login falhou. Email ou senha incorretos.")

        case '3':
            print("Saindo do sistema...")
            exit()

        case _:
            print("Opção inválida! Tente novamente.")

# Exibe o menu
if __name__ == "__main__":
    while True:
        menu()
