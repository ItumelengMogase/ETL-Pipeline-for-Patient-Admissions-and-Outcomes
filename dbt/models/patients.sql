-- This model cleans and transforms the PatientCorePopulatedTable data.

WITH raw_patients AS (
    -- Select raw patient data from PostgreSQL
    SELECT 
        PatientID,
        PatientGender,
        PatientDateOfBirth,
        PatientRace,
        PatientMaritalStatus,
        PatientLanguage,
        PatientPopulationPercentageBelowPoverty
    FROM {{ source('medical_data', 'patientcorepopulatedtable') }}
),

cleaned_patients AS (
    -- Clean and transform the data
    SELECT 
        -- Retain the original patient ID
        PatientID,
        
        -- Clean the gender field, ensuring it follows a consistent format
        CASE 
            WHEN LOWER(PatientGender) = 'male' THEN 'Male'
            WHEN LOWER(PatientGender) = 'female' THEN 'Female'
            ELSE 'Unknown'
        END AS PatientGender,
        
        -- Convert PatientDateOfBirth to date format
        TO_DATE(PatientDateOfBirth, 'YYYY-MM-DD') AS PatientDateOfBirth,
        
        -- Normalize the race field for consistency
        CASE 
            WHEN LOWER(PatientRace) = 'african american' THEN 'African American'
            WHEN LOWER(PatientRace) = 'asian' THEN 'Asian'
            WHEN LOWER(PatientRace) = 'white' THEN 'White'
            ELSE 'Other'
        END AS PatientRace,
        
        -- Clean up the marital status to ensure consistency
        CASE 
            WHEN LOWER(PatientMaritalStatus) = 'single' THEN 'Single'
            WHEN LOWER(PatientMaritalStatus) = 'married' THEN 'Married'
            WHEN LOWER(PatientMaritalStatus) = 'divorced' THEN 'Divorced'
            WHEN LOWER(PatientMaritalStatus) = 'separated' THEN 'Separated'
            WHEN LOWER(PatientMaritalStatus) = 'widowed' THEN 'Widowed'
            ELSE 'Unknown'
        END AS PatientMaritalStatus,
        
        -- Clean and normalize the language field
        CASE 
            WHEN LOWER(PatientLanguage) = 'english' THEN 'English'
            WHEN LOWER(PatientLanguage) = 'icelandic' THEN 'Icelandic'
            WHEN LOWER(PatientLanguage) = 'spanish' THEN 'Spanish'
            ELSE 'Other'
        END AS PatientLanguage,
        
        -- Ensure the population percentage below poverty is within a valid range (0-100%)
        CASE 
            WHEN PatientPopulationPercentageBelowPoverty >= 0 AND PatientPopulationPercentageBelowPoverty <= 100 
                THEN PatientPopulationPercentageBelowPoverty
            ELSE NULL -- Set invalid values to NULL
        END AS PatientPopulationPercentageBelowPoverty
    FROM raw_patients
)

SELECT * FROM cleaned_patients;
