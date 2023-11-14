from datetime import datetime
import re
import uuid
import repository

def menu(doctor):
    stop = 's'
    while stop != 'n':
        print()
        print(f"O que deseja ver, {doctor["name"]}?")
        print("""
              1 - Realiazar consulta\n
              2 - Realizar exame\n
              3 - Prescrever medicações\n
              4 - Veriricar consultas do paciente\n 
              5 - Veiricar exames do paciente\n
              6 - Vericiar medicações do paciente\n
              7 - Sair
            """)
        choice = int(input())

        if(choice == 1):
            print()

            pacientDocument = input("Qual o documento do paciente?: ")

            sumarry = input("Qual foi o resumo da consulta?: ")

            hospital = input("Em qual hospital que foi realizada a consulta?: ")
            
            today = datetime.now()
            
            todayFortated = today.strftime("%d/%m/%Y")

            appointment = {
                "id": str(uuid.uuid4()),
                "doctor_document": doctor["document"],
                "pacient_document": pacientDocument,
                "checkup_summary": sumarry,
                "hospital": hospital,
                "date": todayFortated
            }

            repository.saveAppoitment(appointment)
        
        elif (choice == 2):
            print()

            pacientDocument = input("Qual o documento do paciente?: ")

            type = input("Qual tipo do exame?: ") 

            description = input("Qual a descrição do exame?:" )
            
            hospital = input("Em qual hospital que foi realizada a consulta?: ")
            
            today = datetime.now()
            
            todayFortated = today.strftime("%d/%m/%Y")

            exam = {
                "id": str(uuid.uuid4()),
                "doctor_document": doctor["document"],
                "pacient_document": pacientDocument,
                "type": type,
                "description": description,
                "hospital": hospital,
                "date": todayFortated
            }

            repository.saveExam(exam)

        elif (choice == 3):
            print()   

            pacientDocument = input("Qual o documento do paciente?: ")

            startDate = input("Data de inicio para tomar a medicação?: (00/00/000) ") 

            endDate = input("Data de final para tomar a medicação?: (00/00/000) ") 
            
            medicine = input("Qual o medicamento?: ")

            activePrinciple = input("Qual o princípio ativo do medicamento?: ")

            prescription = {
                "id": str(uuid.uuid4()),
                "doctor_document": doctor["document"],
                "pacient_document": pacientDocument,
                "start_date": startDate,
                "end_date": endDate,
                "medicine": medicine,
                "active_principle": activePrinciple
            }

            repository.savePrescription(prescription) 

        elif (choice == 4):
            print()
            pacientDocument = input("Qual o documento do paciente?: ")
            data = repository.getAppoitments(pacientDocument)
            if(len(data) < 1):
                print("O paciente não tem hisórico de consultas")
            else:
                for appointment in data:
                    print(f"Data da consulta: {appointment["date"]}")  
                    print(f"Nome do médico da consulta: {appointment["doctor_name"]}")  
                    print(f"Médico da consulta: {appointment["doctor_document"]}")    
                    print(f"Resumo: {appointment["checkup_summary"]}")    
                    print(f"Hospital da consulta: {appointment["hospital"]}")  
                    print()
                    print()  
        print("Deseja ver outra opção? (s)im ou (n)ão")
        stop = input().lower()




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
                menu(doctorExists)       
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
            menu(doctor)
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
