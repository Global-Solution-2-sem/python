import re
import repository

def menu(pacient):
    stop = 's'
    while stop != 'n':
        print()
        print(f"O que deseja ver, {pacient["name"]}? ")
        print("1 - meus dados\n2 - Histórico de consultas\n3 - Histórico de exames\n4 - Histórico de medicações\n5 - Sair")
        choice = int(input())

        if(choice == 1):
            data = repository.getPacientByDocument(pacient["document"])

            print()
            print("Seus dados são:")

            print(f"CPF: {data["document"]}")
            print(f"Nome: {data["name"]}")
            print(f"Email: {data["email"]}")
            print(f"CEP: {data["zipCode"]}")
            print(f"Telefone: {data["telephone"]}")
            print(f"Data de nascimento: {data["birthDate"]}")

            print()
            print()
            print("Deseja ver outra opção? (s)im ou (n)ão")
            stop = input().lower()

        elif (choice == 2):
            print()
            print("Suas consultas:")
            print()
            data = repository.getAppoitments(pacient["document"])
            if(len(data) < 1):
                print("Você não tem hisórico de consultas")
            else:
                for appointment in data:
                    print(f"Data da consulta: {appointment["date"]}")  
                    print(f"Nome do médico da consulta: {appointment["doctor_name"]}")  
                    print(f"Médico da consulta: {appointment["doctor_document"]}")    
                    print(f"Resumo: {appointment["checkup_summary"]}")    
                    print(f"Hospital da consulta: {appointment["hospital"]}")  

                    print()
                    print()  


def signIn():
    error = ""
    try:
        document = input("Digite seu cpf: ")
        if not (re.search(r"\d", document)):
            error = "Documento pode apenas conter números"
            raise ValueError
        password = input("Digite sua senha: ")
    
        pacientExists = repository.getPacientByDocument(document)

        if(pacientExists == False):
            print("Documento inválido!")
        else:
            if not(pacientExists["password"] == password):
                print("Documento ou senha inválido!")
            else:
                menu(pacientExists)       
    except:
        print(error)


def signUp():
    error = ""
    try:
        document = input("Digite seu CPF: ")
        if not (re.search(r"\d{11}", document)):
            error = "Documento pode apenas conter números e 11 dígitos"
            raise ValueError
        name = input("Digite seu nome: ")
        if (re.search(r"\d", name)):
            error = "Nome não deve conter números"
            raise ValueError

        email = input("Digite seu email: ")
        if(not re.search("^(.+)@(.+)$",email)):
            error = "Email inválido"
            raise ValueError

        telephone = input("Digite seu telefone: ")
        if not (re.search(r"\d{11}", telephone)):
            error = "Telefone pode apenas conter números e 11 dígitos"
            raise ValueError

        zipCode = input("Digite seu CEP: ")
        if not (re.search(r"\d{7}", zipCode)):
            error = "CEP pode apenas conter números e 7 dígitos"
            raise ValueError

        password = input("Digite sua senha: ")
        
        birthDate = input("Digite sua data de nascimento: (00/00/0000) ")
        if not re.search((r'^\d{2}/\d{2}/\d{4}$'), birthDate):
            error = "Data de nascimento no formato inválido!"
            raise ValueError
        
        pacientExist = repository.getPacientByDocument(document)
        if(pacientExist == False):
            pacient = {
                "document": document,
                "name": name,
                "email": email, 
                "telephone": telephone,
                "zipCode": zipCode,
                "password": password,
                "birthDate": birthDate
            }
            repository.savePacient(pacient)
            menu(pacient)
        else:
            print("Documento já utilizado!")
    except:
        print(error)    


print("---------------------------------- Bem vindo, Paciente ----------------------------------")
print()

print("Já possui uma conta? Digite 1 para entrar ou 2 para criar uma nova conta")
choice = int(input())

if(choice == 1):
    signIn()
else:
    signUp()
