def add_user(agenda, user_name, user_phone, user_email):
    contact = {
        "contact": user_name,
        "phone": user_phone,
        "email": user_email,
        "Favorito": True,
    }
    agenda.append(contact)
    print(
        f"Contato {user_name}, com telefone {user_phone} e email {user_email} adicionado com sucesso!"
    )
    return


def view_contacts(agenda):
    print("\nLista de contatos: ")
    for index, contact in enumerate(agenda, start=1):
        favorite = "⭐" if contact["Favorito"] else " "
        user_name = contact["contact"]
        user_phone = contact["phone"]
        user_email = contact["email"]
        print(f"{favorite} {index}. {user_name} ({user_phone}) {user_email}")
    return


def edit_user(agenda, index_contact, new_name, new_phone, new_email):
    index_contact_fixed = int(index_contact) - 1
    if index_contact_fixed >= 0 and index_contact_fixed < len(agenda):
        agenda[index_contact_fixed]["contact"] = new_name
        agenda[index_contact_fixed]["phone"] = new_phone
        agenda[index_contact_fixed]["email"] = new_email
        print(f"Contato {new_name} editado com sucesso!")
    else:
        print("Índice inválido!")
    return


agenda = []
while True:
    print("-----------------------------")
    print("   Bem-Vindo a sua agenda!")
    print("-----------------------------")
    print("Escolha uma opção:")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Excluir contato")
    print("6. Sair")
    option = input("Digite o número da opção desejada: ")

    if option == "1":
        user_name = input("Digite o nome do contato: ")
        user_phone = input("Digite o telefone do contato: ")
        user_email = input("Digite o email do contato: ")
        add_user(agenda, user_name, user_phone, user_email)

    elif option == "2":
        view_contacts(agenda)

    elif option == "3":
        view_contacts(agenda)
        index_contact = input("Digite o índice do contato que deseja editar: ")
        new_name = input("Digite o novo nome do contato: ")
        new_phone = input("Digite o novo telefone do contato: ")
        new_email = input("Digite o novo email do contato: ")
        edit_user(agenda, index_contact, new_name, new_phone, new_email)

    elif option == "6":
        break

print("Programa finalizado! 🔴")
