
  create view "healthcare_pipeline_db"."medical_data"."admissions__dbt_tmp"
    
    
  as (
    SELECT * FROM medical_data.admissionscorepopulatedtable
  );