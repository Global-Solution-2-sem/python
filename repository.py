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
        if(appointment["pacient_document"] == document):
            output.append(appointment)

        for data in output:
            doctor = getDoctorByDocument(data["doctor_document"])
            data.update({"doctor_name":doctor["name"]})
    return appointments

def savePacient(pacient):
    pacients = []
    with open('./database/pacients.json', 'r', encoding='UTF-8') as file:
        pacients = json.load(file)
    pacients.append(pacient)
    with open('./database/pacients.json', 'w', encoding='UTF-8') as file:
        json.dump(pacients, file)  


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
