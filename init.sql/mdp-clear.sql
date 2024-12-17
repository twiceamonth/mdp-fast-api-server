--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: mdp; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA mdp;


ALTER SCHEMA mdp OWNER TO pg_database_owner;

--
-- Name: SCHEMA mdp; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA mdp IS 'standard public schema';


--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA mdp;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Biometrics; Type: TABLE; Schema: mdp; Owner: postgres
--

CREATE TABLE mdp."Biometrics" (
    photo_id uuid DEFAULT gen_random_uuid() NOT NULL,
    upload_date date DEFAULT CURRENT_DATE NOT NULL,
    photo_path text NOT NULL,
    employee_id uuid NOT NULL
);


ALTER TABLE mdp."Biometrics" OWNER TO postgres;

--
-- Name: Department; Type: TABLE; Schema: mdp; Owner: postgres
--

CREATE TABLE mdp."Department" (
    department_id uuid DEFAULT gen_random_uuid() NOT NULL,
    name text NOT NULL
);


ALTER TABLE mdp."Department" OWNER TO postgres;

--
-- Name: Employee; Type: TABLE; Schema: mdp; Owner: postgres
--

CREATE TABLE mdp."Employee" (
    employee_id uuid DEFAULT gen_random_uuid() NOT NULL,
    first_name character varying(100) NOT NULL,
    second_name character varying(100) NOT NULL,
    patronymic character varying(100),
    position_id uuid NOT NULL,
    department_id uuid NOT NULL,
    employee_photo text NOT NULL
);


ALTER TABLE mdp."Employee" OWNER TO postgres;

--
-- Name: Event; Type: TABLE; Schema: mdp; Owner: postgres
--

CREATE TABLE mdp."Event" (
    event_id uuid DEFAULT gen_random_uuid() NOT NULL,
    event_name character varying(500) NOT NULL,
    event_date date NOT NULL,
    start_time time without time zone NOT NULL,
    end_time time without time zone NOT NULL,
    description text NOT NULL,
    event_video text
);


ALTER TABLE mdp."Event" OWNER TO postgres;

--
-- Name: Invitation; Type: TABLE; Schema: mdp; Owner: postgres
--

CREATE TABLE mdp."Invitation" (
    event_id uuid NOT NULL,
    employee_id uuid NOT NULL
);


ALTER TABLE mdp."Invitation" OWNER TO postgres;

--
-- Name: Position; Type: TABLE; Schema: mdp; Owner: postgres
--

CREATE TABLE mdp."Position" (
    position_id uuid DEFAULT gen_random_uuid() NOT NULL,
    name text NOT NULL
);


ALTER TABLE mdp."Position" OWNER TO postgres;

--
-- Name: User; Type: TABLE; Schema: mdp; Owner: postgres
--

CREATE TABLE mdp."User" (
    login character varying(50) NOT NULL,
    password_hash text NOT NULL
);


ALTER TABLE mdp."User" OWNER TO postgres;

--
-- Name: Visit; Type: TABLE; Schema: mdp; Owner: postgres
--

CREATE TABLE mdp."Visit" (
    visit_id uuid DEFAULT gen_random_uuid() NOT NULL,
    employee_id uuid,
    event_id uuid NOT NULL
);


ALTER TABLE mdp."Visit" OWNER TO postgres;

--
-- Name: VisitMark; Type: TABLE; Schema: mdp; Owner: postgres
--

CREATE TABLE mdp."VisitMark" (
    mark_id uuid DEFAULT gen_random_uuid() NOT NULL,
    fixation_time time without time zone DEFAULT CURRENT_TIME NOT NULL,
    photo_path text NOT NULL,
    visit_id uuid NOT NULL
);


ALTER TABLE mdp."VisitMark" OWNER TO postgres;


--
-- Data for Name: User; Type: TABLE DATA; Schema: mdp; Owner: postgres
--

COPY mdp."User" (login, password_hash) FROM stdin;
string	$2b$12$xH9FiVdL8xbjZtowPtNe7.VClOb2m2pxhHuB8U48F2Mb9Hqgy3iWm
\.

--
-- Name: Biometrics biometrics_pk; Type: CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Biometrics"
    ADD CONSTRAINT biometrics_pk PRIMARY KEY (photo_id);


--
-- Name: Department department_pk; Type: CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Department"
    ADD CONSTRAINT department_pk PRIMARY KEY (department_id);


--
-- Name: Employee employee_pk; Type: CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Employee"
    ADD CONSTRAINT employee_pk PRIMARY KEY (employee_id);


--
-- Name: Event event_pk; Type: CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Event"
    ADD CONSTRAINT event_pk PRIMARY KEY (event_id);


--
-- Name: Invitation invitation_pk; Type: CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Invitation"
    ADD CONSTRAINT invitation_pk PRIMARY KEY (event_id, employee_id);


--
-- Name: Position position_pk; Type: CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Position"
    ADD CONSTRAINT position_pk PRIMARY KEY (position_id);


--
-- Name: User user_pk; Type: CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."User"
    ADD CONSTRAINT user_pk PRIMARY KEY (login);


--
-- Name: Visit visit_pk; Type: CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Visit"
    ADD CONSTRAINT visit_pk PRIMARY KEY (visit_id);


--
-- Name: VisitMark visitmark_pk; Type: CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."VisitMark"
    ADD CONSTRAINT visitmark_pk PRIMARY KEY (mark_id);


--
-- Name: Biometrics biometrics_employee_fk; Type: FK CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Biometrics"
    ADD CONSTRAINT biometrics_employee_fk FOREIGN KEY (employee_id) REFERENCES mdp."Employee"(employee_id);


--
-- Name: Employee employee_department_fk; Type: FK CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Employee"
    ADD CONSTRAINT employee_department_fk FOREIGN KEY (department_id) REFERENCES mdp."Department"(department_id);


--
-- Name: Employee employee_position_fk; Type: FK CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Employee"
    ADD CONSTRAINT employee_position_fk FOREIGN KEY (position_id) REFERENCES mdp."Position"(position_id);


--
-- Name: Invitation invitation_employee_fk; Type: FK CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Invitation"
    ADD CONSTRAINT invitation_employee_fk FOREIGN KEY (employee_id) REFERENCES mdp."Employee"(employee_id);


--
-- Name: Invitation invitation_event_fk; Type: FK CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Invitation"
    ADD CONSTRAINT invitation_event_fk FOREIGN KEY (event_id) REFERENCES mdp."Event"(event_id);


--
-- Name: Visit visit_employee_fk; Type: FK CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Visit"
    ADD CONSTRAINT visit_employee_fk FOREIGN KEY (employee_id) REFERENCES mdp."Employee"(employee_id);


--
-- Name: Visit visit_event_fk; Type: FK CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."Visit"
    ADD CONSTRAINT visit_event_fk FOREIGN KEY (event_id) REFERENCES mdp."Event"(event_id);


--
-- Name: VisitMark visitmark_visit_fk; Type: FK CONSTRAINT; Schema: mdp; Owner: postgres
--

ALTER TABLE ONLY mdp."VisitMark"
    ADD CONSTRAINT visitmark_visit_fk FOREIGN KEY (visit_id) REFERENCES mdp."Visit"(visit_id);


--
-- PostgreSQL database dump complete
--

