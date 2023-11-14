import re
import repository

def signIn():
    users = repository.getAllPacient()
    error = ""
    try:
        document = input("Digite seu cpf: ")
        if not (re.search("\d", document)):
            error = "Documento pode apenas conter números"
            raise ValueError
        password = input("Digite sua senha: ")
    
        

    except:
        print(error)


print("---------------------------------- Bem vindo ao App ----------------------------------")
print()

print("Já possui uma conta? Digite 1 para entrar ou 2 para criar uma nova conta")
choice = int(input())

if(choice == 1):
    signIn()
else:
    print()
