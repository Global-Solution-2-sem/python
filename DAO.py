import json

def getAllPacient():
    with open('./database/pacients.json', 'r', encoding='UTF-8') as file:
        return json.load(file)
    
def getPacientByDocument(document):
    pacients = []
    with open('./database/pacients.json', 'r', encoding='UTF-8') as file:
        pacients = json.load(file)

    for pacient in pacients:
        if(pacient["document"] == document):
            return pacient    
    return False

def getAppoitments(document):
    appointments = []
    with open('./database/appointments.json', 'r', encoding='UTF-8') as file:
        appointments = json.load(file)

    output = []
    for appointment in appointments:
        if appointment["pacient_document"] == document:
            doctor = getDoctorByDocument(appointment["doctor_document"])
            appointment.update({"doctor_name": doctor["name"]})
            output.append(appointment)

    return output

def getExams(document):
    exams = []
    with open('./database/exams.json', 'r', encoding='UTF-8') as file:
        exams = json.load(file)

    output = []
    for exam in exams:
        if exam["pacient_document"] == document:
            doctor = getDoctorByDocument(exam["doctor_document"])
            exam.update({"doctor_name": doctor["name"]})
            output.append(exam)

    return output

def getPrescriptions(document):
    prescriptions = []
    with open('./database/prescriptions.json', 'r', encoding='UTF-8') as file:
        prescriptions = json.load(file)

    output = []
    for prescription in prescriptions:
        if prescription["pacient_document"] == document:
            doctor = getDoctorByDocument(prescription["doctor_document"])
            prescription.update({"doctor_name": doctor["name"]})
            output.append(prescription)

    return output

def getSurgeries(document):
    surgeries = []
    with open('./database/surgeries.json', 'r', encoding='UTF-8') as file:
        surgeries = json.load(file)

    output = []
    for surgery in surgeries:
        if surgery["pacient_document"] == document:
            doctor = getDoctorByDocument(surgery["doctor_document"])
            surgery.update({"doctor_name": doctor["name"]})
            output.append(surgery)

    return output 

def savePacient(pacient):
    pacients = []
    with open('./database/pacients.json', 'r', encoding='UTF-8') as file:
        pacients = json.load(file)
    pacients.append(pacient)
    with open('./database/pacients.json', 'w', encoding='UTF-8') as file:
        json.dump(pacients, file)  

def updatePacient(pacient):
    pacients = []
    with open('./database/pacients.json', 'r', encoding='UTF-8') as file:
        pacients = json.load(file)
    for i in range(len(pacients)):
        if(pacients[i]["document"] == pacient["document"]):
            pacients[i] = pacient
            break
    else:
        print("CPF do paciente não encontado")
    with open('./database/pacients.json', 'w', encoding='UTF-8') as file:
        json.dump(pacients, file)    

def saveKinship(kinship):
    kinships = []
    with open('./database/kinships.json', 'r', encoding='UTF-8') as file:
        kinships = json.load(file)
    kinships.append(kinship)
    with open('./database/kinships.json', 'w', encoding='UTF-8') as file:
        json.dump(kinships, file) 


def getAllDoctors():
    with open('./database/doctors.json', 'r', encoding='UTF-8') as file:
        return json.load(file)
 
def getDoctorByDocument(document):
    doctors = []
    with open('./database/doctors.json', 'r', encoding='UTF-8') as file:
        doctors = json.load(file)

    for doctor in doctors:
        if(doctor["document"] == document):
            return doctor    
    return False 

def saveDoctor(pacient):
    doctors = []
    with open('./database/doctors.json', 'r', encoding='UTF-8') as file:
        doctors = json.load(file)
    doctors.append(pacient)
    with open('./database/doctors.json', 'w', encoding='UTF-8') as file:
        json.dump(doctors, file)  

def saveAppoitment(appointment):
    appointments = []
    with open('./database/appointments.json', 'r', encoding='UTF-8') as file:
        appointments = json.load(file) 
    appointments.append(appointment)
    with open('./database/appointments.json', 'w', encoding='UTF-8') as file:
        json.dump(appointments, file)  

def saveExam(exam):
    exams = []
    with open('./database/exams.json', 'r', encoding='UTF-8') as file:
        exams = json.load(file) 
    exams.append(exam)
    with open('./database/exams.json', 'w', encoding='UTF-8') as file:
        json.dump(exams, file)  

def savePrescription(prescription):
    prescriptions = []
    with open('./database/prescriptions.json', 'r', encoding='UTF-8') as file:
        prescriptions = json.load(file) 
    prescriptions.append(prescription)
    with open('./database/prescriptions.json', 'w', encoding='UTF-8') as file:
        json.dump(prescriptions, file)

def saveSurgery(surgery):
    surgeries = []
    with open('./database/surgeries.json', 'r', encoding='UTF-8') as file:
        surgeries = json.load(file) 
    surgeries.append(surgery)
    with open('./database/surgeries.json', 'w', encoding='UTF-8') as file:
        json.dump(surgeries, file)
