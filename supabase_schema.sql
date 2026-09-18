-- UniAttend database schema
-- Run this in Supabase -> SQL Editor -> New query -> Run
-- Column names here match exactly what src/database/db.py expects.

create table if not exists teachers (
  teacher_id bigint generated always as identity primary key,
  username   text unique not null,
  password   text not null,          -- bcrypt hash, never plain text
  name       text,
  created_at timestamptz default now()
);

create table if not exists students (
  student_id      bigint generated always as identity primary key,
  name            text not null,
  face_embedding  jsonb,             -- 128-dim dlib vector
  voice_embedding jsonb,             -- 256-dim Resemblyzer vector
  created_at      timestamptz default now()
);

create table if not exists subjects (
  subject_id   bigint generated always as identity primary key,
  subject_code text unique not null, -- also used as the QR / join code
  name         text not null,
  section      text,
  teacher_id   bigint references teachers(teacher_id) on delete cascade,
  created_at   timestamptz default now()
);

create table if not exists subject_students (
  id         bigint generated always as identity primary key,
  student_id bigint references students(student_id) on delete cascade,
  subject_id bigint references subjects(subject_id) on delete cascade,
  unique (student_id, subject_id)
);

create table if not exists attendance_logs (
  id         bigint generated always as identity primary key,
  student_id bigint references students(student_id) on delete cascade,
  subject_id bigint references subjects(subject_id) on delete cascade,
  timestamp  timestamptz,
  is_present boolean default false
);

-- Supabase turns Row Level Security ON by default. With RLS on and no
-- policies, every query returns empty and every insert fails silently.
-- The app uses the anon key with no Supabase Auth, so turn RLS off.
-- NOTE: this makes the anon key able to read/write everything. Fine for a
-- college demo, not safe for real student data.

alter table teachers         disable row level security;
alter table students         disable row level security;
alter table subjects         disable row level security;
alter table subject_students disable row level security;
alter table attendance_logs  disable row level security;
