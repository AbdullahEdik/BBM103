# BBM 103 Lecture - Assignment 2: Doctor’s Aid

# Check whether patient is in patients_list. If patient is not in list, return -1;
# else return index of patient.
def is_patient_in_list(patient_name):
    for i in range(len(patients_list)):
        if patients_list[i][0] == patient_name:
            return i
    return -1


# Required number of tabs calculater for list_patients function.
def tab_calculate(necessary_length, length):
    num_of_tabs = ((necessary_length - length) // 4)
    if (necessary_length - length) % 4 != 0:
        num_of_tabs += 1

    return num_of_tabs


# Create patient from given string and add patient information to patients_list.
def create_patient(patient_info):
    p_info = patient_info.split(", ")
    if is_patient_in_list(p_info[0]) > -1:
        w_file.write(f"Patient {p_info[0]} cannot be recorded due to duplication.\n")

    else:
        patients_list.append(p_info)
        w_file.write(f"Patient {p_info[0]} is recorded.\n")


# Remove patient from patients_list.
def remove_patient(patient_name):
    i = is_patient_in_list(patient_name)
    if i > -1:
        patients_list.pop(i)
        w_file.write(f"Patient {patient_name} is removed.\n")
    else:
        w_file.write(f"Patient {patient_name} cannot be removed due to absence.\n")


# List information of patients from patients_list.
def list_patients():
    w_file.write("Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment\n")
    w_file.write("Name\tAccuracy\tName\t\t\tIncidence\tName\t\t\tRisk\n")
    w_file.write("-------------------------------------------------------------------------\n")
    for patient in patients_list:
        d_accuracy = float(patient[1]) * 100
        d_accuracy = "{:.2f}".format(d_accuracy)
        t_risk = int(float(patient[5]) * 100)

        w_file.write(f"{patient[0]}" +
                     ("\t" * tab_calculate(8, len(patient[0]))) + f"{d_accuracy}%\t\t{patient[2]}" +
                     ("\t" * tab_calculate(16, len(patient[2]))) + f"{patient[3]}\t{patient[4]}" +
                     ("\t" * tab_calculate(16, len(patient[4]))) + f"{t_risk}%\n")


# Calculate probability of patient's having disease.
def probability(patient_name):
    i = is_patient_in_list(patient_name)
    if i > -1:
        patient = patients_list[i]
        disease_incidence_list = patient[3].split("/")
        disease_incidence = float(disease_incidence_list[0]) / float(disease_incidence_list[1])
        diagnosis_accuracy = float(patient[1])
        prob = round(float(disease_incidence / ((1 - diagnosis_accuracy) + disease_incidence) * 100), 2)
        if prob % 10 == 0:
            prob = round(prob)
        w_file.write(f"Patient {patient_name} has a probability of {prob}% of having {patient[2].lower()}.\n")

    else:
        w_file.write(f"Probability for {patient_name} cannot be calculated due to absence.\n")


# Recommendation for patient to have treatment or not.
def recommendation(patient_name):
    i = is_patient_in_list(patient_name)
    if i > -1:
        patient = patients_list[i]
        disease_incidence_list = patient[3].split("/")
        disease_incidence = float(disease_incidence_list[0]) / float(disease_incidence_list[1])
        diagnosis_accuracy = float(patient[1])
        prob = round(float(disease_incidence / ((1 - diagnosis_accuracy) + disease_incidence) * 100), 2)
        t_risk = int(float(patient[5]) * 100)

        if prob > t_risk:
            w_file.write(f"System suggests {patient_name} to have the treatment.\n")

        else:
            w_file.write(f"System suggests {patient_name} NOT to have the treatment.\n")

    else:
        w_file.write(f"Recommendation for {patient_name} cannot be calculated due to absence.\n")


# Open files
r_file = open("doctors_aid_inputs.txt", "r")
w_file = open("doctors_aid_outputs.txt", "w", encoding="utf-8")

patients_list = []

# Get commands from input file
lines = r_file.read()
r_file.close()
lines = lines.split("\n")

# Apply commands
for line in lines:
    if line.count(" ") > 0:
        line_list = line.split(" ", 1)

        if line_list[0] == "create":
            create_patient(line_list[1])

        elif line_list[0] == "remove":
            remove_patient(line_list[1])

        elif line_list[0] == "probability":
            probability(line_list[1])

        elif line_list[0] == "recommendation":
            recommendation(line_list[1])

        else:
            w_file.write("Error: Incorrect command.\n")

    else:
        list_patients()

w_file.close()
