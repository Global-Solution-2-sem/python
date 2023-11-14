import re
import repository

def signIn():
    error = ""
    try:
        document = input("Digite seu CRM: ")
        if not (re.search(r"\d", document)):
            error = "Documento pode apenas conter números"
            raise ValueError
        password = input("Digite sua senha: ")
    
        doctorExists = repository.getDoctorByDocument(document)

        if(doctorExists == False):
            print("Documento inválido!")
        else:
            if not(doctorExists["password"] == password):
                print("Documento ou senha inválido!")
            else:
                print("login aproved")        
    except:
        print(error)

def signUp():
    error = ""
    try:
        document = input("Digite seu CRM (CRM-UF-XXXXX): ")
        if not (re.search(r"^CRM-[A-Z]{2}-\d{5}$", document)):
            error = "Documento deve estar no formato CRM-UF-XXXXX"
            raise ValueError(error)
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

        password = input("Digite sua senha: ")
        
        birthDate = input("Digite sua data de nascimento: (00/00/0000) ")
        if not re.search((r'^\d{2}/\d{2}/\d{4}$'), birthDate):
            error = "Data de nascimento no formato inválido!"
            raise ValueError
        
        doctorExist = repository.getDoctorByDocument(document)
        if(doctorExist == False):
            doctor = {
                "document": document,
                "name": name,
                "email": email, 
                "telephone": telephone,
                "password": password,
                "birthDate": birthDate
            }
            repository.saveDoctor(doctor)
        else:
            print("Documento já utilizado!")
    except:
        print(error)    


print("---------------------------------- Bem vindo, Doutor ----------------------------------")
print()

print("Já possui uma conta? Digite 1 para entrar ou 2 para criar uma nova conta")
choice = int(input())

if(choice == 1):
    signIn()
else:
    signUp()
