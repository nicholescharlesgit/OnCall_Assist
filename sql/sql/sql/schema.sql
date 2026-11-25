CREATE TABLE departments (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);
-- Prevent deleting a department while doctors still belong to it.
CREATE TABLE doctors (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INTEGER NOT NULL
        REFERENCES departments(id)
        ON DELETE RESTRICT
);
CREATE TABLE patients (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    patient_number VARCHAR(20) NOT NULL UNIQUE
);

create table slots(id integer generated always as IDENTITY primary key,doctor_id integer not null references doctors(id) 
on delete restrict
,start_time timestamptz not null,status text not null default 'free' 
check( status in ('free','booked')),constraint unique_doc unique(doctor_id,start_time));

create table appointments(id integer  generated always as identity primary key,patient_id integer not null references patients(id) on
delete restrict,slot_id integer not null references slots(id) on delete restrict,status text not null check(status in
('booked','cancelled')),created_at timestamptz not null default now(),idempotency_key text unique);