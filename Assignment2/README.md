# Doctor's Aid - Patient Management System

This Python script, Doctor's Aid, serves as a patient management system designed for medical professionals. It allows doctors to manage patient records efficiently, calculate probabilities of diseases, and provide treatment recommendations based on available data.

## Features

### Patient Management:

Add new patients with their diagnosis and treatment information.
Remove existing patients from the system.

### Patient Information Listing:

Display a formatted list of patients including their diagnosis accuracy, diseases, and treatments.

### Disease Probability Calculation:

Calculate the probability of a patient having a specific disease based on diagnosis accuracy and disease incidence.

### Treatment Recommendation:

Provide a recommendation on whether a patient should undergo treatment based on calculated disease probability and treatment risk.

## Usage

To utilize Doctor's Aid, follow these steps:

### Input File:

Prepare an input file named doctors_aid_inputs.txt. Each line in this file represents a command to be executed by the system. Commands should be in the following format:

create Patient_Name, Diagnosis_Accuracy, Disease_Name, Disease_Incidence, Treatment_Name, Treatment_Risk

remove Patient_Name

probability Patient_Name

recommendation Patient_Name

### Example:

create John Doe, 0.85, Influenza, 20/100, Antiviral Medication, 15/100
remove Jane Smith
probability John Doe
recommendation John Doe

### Execute Script:

Run the Python script (doctor_aid.py).

## Output:

The script will generate an output file named doctors_aid_outputs.txt, containing the results of the executed commands and any error messages encountered during processing.

## Notes

Ensure that input data is correctly formatted to prevent errors during processing.
Adjust the input and output file paths as necessary to match your system configuration.

This script was developed as an assignment for the BBM 103 Course.
