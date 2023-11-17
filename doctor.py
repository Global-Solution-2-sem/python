from datetime import datetime
import re
import uuid
import DAO

def calculateDuration(startDate, endDate):
    dateFormat = "%d/%m/%Y"

    dateDifference = datetime.strptime(endDate, dateFormat) - datetime.strptime(startDate, dateFormat) 

    return dateDifference.days

def menu(doctor):
    stop = 's'
    while stop != 'n':
        print()
        print(f"O que deseja ver, {doctor["name"]}?")
        print("""
                1 - Realizar consulta\n
                2 - Realizar exame\n
                3 - Prescrever medicações\n
                4 - Realizar Cirurgia\n
                5 - Verificar consultas do paciente\n 
                6 - Verificar exames do paciente\n
                7 - Verificar medicações do paciente\n
                8 - Verificar as cirurgias do paciente\n
                9 - Sair
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

            DAO.saveAppoitment(appointment)
        
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

            DAO.saveExam(exam)

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

            DAO.savePrescription(prescription) 

        elif (choice == 4):
            date = input("Qual a data da cirurgia? (00/00/0000) ")

            pacientDocument = input("Qual o documento do paciente?: ")
            
            name = input("Qual a cirurgia? ")

            reason = input("Qual a razão da cirurgia? ")

            hospital = input("Em qual hospital foi realizada a cirurgia? ")

            surgery = {
                "id": str(uuid.uuid4()),
                "name": name,
                "date": date,
                "reason": reason,
                "doctor_document": doctor["document"],
                "pacient_document": pacientDocument,
                "hospital": hospital
            }
            DAO.saveSurgery(surgery)
        
        elif (choice == 5):
            print()
            pacientDocument = input("Qual o documento do paciente?: ")
            data = DAO.getAppoitments(pacientDocument)
            if(len(data) < 1):
                print("O paciente não tem hisórico de consultas")
            else:
                for appointment in data:
                    print(f"Data da consulta: {appointment["date"]}")  
                    print(f"Nome do médico da consulta: {appointment["doctor_name"]}")  
                    print(f"CRM do médico: {appointment["doctor_document"]}")    
                    print(f"Resumo: {appointment["checkup_summary"]}")    
                    print(f"Hospital da consulta: {appointment["hospital"]}")  
                    print()
                    print()  

        elif (choice == 6):
            print()
            pacientDocument = input("Qual o documento do paciente?: ")
            data = DAO.getExams(pacientDocument)
            if(len(data) < 1):
                print("O paciente não tem hisórico de exames")
            else:
                for exam in data:
                    print(f"Data da consulta: {exam["date"]}")  
                    print(f"Nome do médico do exame: {exam["doctor_name"]}")  
                    print(f"CRM do médico: {exam["doctor_document"]}")  
                    print(f"Tipo do exame: {exam["type"]}")  
                    print(f"Descrição: {exam["description"]}")    
                    print(f"Hospital da consulta: {exam["hospital"]}")  
                    print()
                    print()

        elif (choice == 7):
            print()
            pacientDocument = input("Qual o documento do paciente?: ")
            print()
            data = DAO.getPrescriptions(pacientDocument)
            if(len(data) < 1):
                print("O paciente não tem hisórico de medicações")
            else:
                for prescription in data:
                    print(f"Data de inicio da medicação: {prescription["start_date"]}")  
                    print(f"Data de fim da medicação: {prescription["end_date"]}")  
                    print(f"Duração: {calculateDuration(prescription["start_date"],prescription["end_date"])} dias")
                    print(f"Nome do médico: {prescription["doctor_name"]}")  
                    print(f"CRM do médico: {prescription["doctor_document"]}")    
                    print(f"Medicação: {prescription["medicine"]}")    
                    print(f"Princípio ativo: {prescription["active_principle"]}")  
                    print()
                    print()  

        elif (choice == 8):
            print()
            pacientDocument = input("Qual o documento do paciente?: ")
            data = DAO.getSurgeries(pacientDocument)
            if(len(data) < 1):
                print("O paciente não tem hisórico de exames")
            else:
                for surgery in data:
                    print(f"Data da consulta: {surgery["date"]}")  
                    print(f"Nome do médico do exame: {surgery["doctor_name"]}")  
                    print(f"CRM do médico: {surgery["doctor_document"]}")  
                    print(f"Cirurgia de : {surgery["name"]}")  
                    print(f"Razão da cirurgia: {surgery["reason"]}")    
                    print(f"Hospital da cirurgia: {surgery["hospital"]}")  
                    print()
                    print()

        elif (choice == 9):
            break
        
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
    
        doctorExists = DAO.getDoctorByDocument(document)

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
        
        doctorExist = DAO.getDoctorByDocument(document)
        if(doctorExist == False):
            doctor = {
                "document": document,
                "name": name,
                "email": email, 
                "telephone": telephone,
                "password": password,
                "birthDate": birthDate
            }
            DAO.saveDoctor(doctor)
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
