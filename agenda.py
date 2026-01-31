def add_user(agenda, user_name, user_phone, user_email):
    contact = {"contact": user_name, "phone": user_phone, "email": user_email, "Favorito": False}
    agenda.append(contact)
    print(f"Contato {user_name}, com telefone {user_phone} e email {user_email} adicionado com sucesso!")
    return

agenda = []
while True:
    print("-----------------------------")
    print("   Bem-Vindo a sua agenda!")
    print("-----------------------------")
    print("Escolha uma opção:")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Editar contato")
    print("4 - Excluir contato")
    print("5 - Sair")
    option = input("Digite o número da opção desejada: ")

    if option == "1":
        user_name = input("Digite o nome do contato: ")
        user_phone = input("Digite o telefone do contato: ")
        user_email = input("Digite o email do contato: ")
        add_user(agenda, user_name, user_phone, user_email)

    elif option == "6":
        break

print("Programa finalizado! 🔴")
