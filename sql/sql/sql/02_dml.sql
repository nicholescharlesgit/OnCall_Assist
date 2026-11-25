-- ===== sql/02_dml.sql : practice table slots_table =====


-- ---------- INSERTS ----------
-- expect: (you fill in)
insert into slots_table(doctor_id, start_time)
values (1, '2026-10-09 10:00:00+05:30');

-- expect: (you fill in)
insert into slots_table(doctor_id, start_time, status)
values (2, '2026-08-01 10:00:00+5:30', 'booked') returning id;

-- expect: (you fill in)
insert into slots_table(doctor_id, start_time)
values (2, '2026-08-01 10:20:00+5:30'),
       (3, '2026-02-22 10:00:00+3:40'),
       (4, '2026-03-02 11:00:00+5:30') returning id;

-- expect: (you fill in)
insert into slots_table(doctor_id, start_time)
values (3, '2026-11-04 04:00:00+5:30') returning id;

-- ---------- CHECK ----------
select * from slots_table;

-- ---------- UPDATES ----------
-- expect: (you fill in)
update slots_table set start_time = '2026-12-12 12:00:00+5:30' where id = 1;

-- expect: (you fill in)
update slots_table set status = 'booked' where id = 6;

-- ---------- DELETE ----------
-- expect: (you fill in)
delete from slots_table where id = 6;

select * from slots_table;

-- ---------- BREAKING THE RULES ON PURPOSE ----------

-- 1) UNIQUE: same doctor, same start time
-- expect: (you fill in)
insert into slots_table(doctor_id, start_time)
values (2, '2026-08-01 10:00:00+5:30');
-- ERROR:  duplicate key value violates unique constraint "unique_doc_app"
-- DETAIL:  Key (doctor_id, start_time)=(2, 2026-08-01 04:30:00+00) already exists.

-- 2) CHECK: status not allowed
-- expect: (you fill in)
update slots_table set status = 'bodoked' where id = 6;
-- ERROR:  new row for relation "slots_table" violates check constraint "slots_table_status_check"
-- DETAIL:  Failing row contains (6, 4, 2026-03-02 05:30:00+00, bodoked).

-- 3) NOT NULL: doctor_id missing
-- expect: (you fill in)
insert into slots_table(start_time, status)
values ('2026-09-02 09:20:00+5:30', 'booked');
-- ERROR:  null value in column "doctor_id" of relation "slots_table" violates not-null constraint
-- DETAIL:  Failing row contains (8, null, 2026-09-02 03:50:00+00, booked).

