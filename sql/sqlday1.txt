SELECT * FROM doctors;
SELECT * FROM doctors WHERE department_id = 1;
SELECT * FROM doctors ORDER BY name;
SELECT * FROM doctors LIMIT 2;
SELECT DISTINCT department_id FROM doctors;
SELECT * FROM patients WHERE date_of_birth > '2000-12-31';
SELECT * FROM patients WHERE email IS NOT NULL;
SELECT * FROM patients WHERE email IS NULL;
SELECT * FROM patients WHERE date_of_birth > '2000-12-31' AND email IS NULL;
SELECT * FROM patients WHERE date_of_birth > '2000-12-31' OR email IS NULL;
-- Day 2: SELECT practice on OnCall Assist (doctors, patients)

-- 1. All doctors
-- Expect:
SELECT * FROM doctors;

-- 2. Doctors in department 2
-- Expect:
SELECT * FROM doctors WHERE department_id = 2;

-- 3. Patients born after 2000
-- Expect:
SELECT * FROM patients WHERE date_of_birth > '2000-12-31';

-- 4. Patients with no email
-- Expect:
SELECT * FROM patients WHERE email IS NULL;

-- 5. Doctors sorted by name
-- Expect:
SELECT * FROM doctors ORDER BY name;

-- 6. The first 2 patients
-- Expect:
SELECT * FROM patients ORDER BY id LIMIT 2;

-- 7. Doctor names without repeats
-- Expect:
SELECT DISTINCT name FROM doctors;

-- 8. Patients who have an email
-- Expect:
SELECT * FROM patients WHERE email IS NOT NULL;

-- 9. Doctors in department 1 or 3
-- Expect:
SELECT * FROM doctors WHERE department_id = 1 OR department_id = 3;

-- 10. Patients named peter with no date of birth
-- Expect:
SELECT * FROM patients WHERE name = 'peter' AND date_of_birth IS NULL;