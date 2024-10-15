import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate patients
def generate_patients(num_patients):
    patients = []
    for i in range(num_patients):
        patients.append({
            "PatientID": i + 1,
            "PatientGender": random.choice(["Male", "Female"]),
            "PatientDateOfBirth": (datetime.now() - timedelta(days=random.randint(365*20, 365*90))).strftime('%Y-%m-%d'),
            "PatientRace": random.choice(["African American", "Asian", "White"]),
            "PatientMaritalStatus": random.choice(["Single", "Married", "Divorced", "Separated", "Widowed"]),
            "PatientLanguage": random.choice(["English", "Icelandic", "Spanish"]),
            "PatientPopulationPercentageBelowPoverty": round(random.uniform(0, 100), 2)
        })
    return pd.DataFrame(patients)

# Function to generate admissions
def generate_admissions(num_admissions, patient_ids):
    admissions = []
    for i in range(num_admissions):
        start_date = datetime.now() - timedelta(days=random.randint(0, 365*2))
        end_date = start_date + timedelta(days=random.randint(1, 14))
        admissions.append({
            "PatientID": random.choice(patient_ids),
            "AdmissionID": i + 1,
            "AdmissionStartDate": start_date.strftime('%Y-%m-%d'),
            "AdmissionEndDate": end_date.strftime('%Y-%m-%d')
        })
    return pd.DataFrame(admissions)

# Function to generate diagnoses
def generate_diagnoses(num_diagnoses, patient_ids, admission_ids):
    icd10_codes = ['A00', 'B01', 'C12', 'D34', 'E56', 'F78']
    diagnoses = []
    for i in range(num_diagnoses):
        diagnoses.append({
            "PatientID": random.choice(patient_ids),
            "AdmissionID": random.choice(admission_ids),
            "PrimaryDiagnosisCode": random.choice(icd10_codes),
            "PrimaryDiagnosisDescription": "Sample Diagnosis Description"
        })
    return pd.DataFrame(diagnoses)

# Function to generate labs
def generate_labs(num_labs, patient_ids, admission_ids):
    lab_names = [
        "CBC: WHITE BLOOD CELL COUNT", "CBC: RED BLOOD CELL COUNT", "METABOLIC: SODIUM",
        "METABOLIC: POTASSIUM", "URINALYSIS: PH", "URINALYSIS: WHITE BLOOD CELLS"
    ]
    lab_units = ["10^9/L", "g/L", "mmol/L", "mmol/L", "pH", "cells/μL"]
    
    labs = []
    for i in range(num_labs):
        labs.append({
            "PatientID": random.choice(patient_ids),
            "AdmissionID": random.choice(admission_ids),
            "LabName": random.choice(lab_names),
            "LabValue": round(random.uniform(3.5, 15.5), 2),
            "LabUnits": random.choice(lab_units),
            "LabDateTime": (datetime.now() - timedelta(days=random.randint(0, 365*2))).strftime('%Y-%m-%d')
        })
    return pd.DataFrame(labs)

# Generate patient data
df_patients = generate_patients(100000)
df_patients.to_csv('data/raw/patients.csv', index=False)

# Generate admissions data
patient_ids = df_patients['PatientID'].tolist()
df_admissions = generate_admissions(50000, patient_ids)
df_admissions.to_csv('data/raw/admissions.csv', index=False)

# Generate diagnoses data
admission_ids = df_admissions['AdmissionID'].tolist()
df_diagnoses = generate_diagnoses(50000, patient_ids, admission_ids)
df_diagnoses.to_csv('data/raw/diagnoses.csv', index=False)

# Generate labs data
df_labs = generate_labs(100000, patient_ids, admission_ids)
df_labs.to_csv('data/raw/labs.csv', index=False)

print("Data generation completed successfully.")