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
-- Name: Visit; Type: TABLE; Schema: mdp; Owner: postgres
--

CREATE TABLE mdp."Visit" (
    visit_id uuid DEFAULT gen_random_uuid() NOT NULL,
    employee_id uuid NOT NULL,
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
-- Data for Name: Biometrics; Type: TABLE DATA; Schema: mdp; Owner: postgres
--

COPY mdp."Biometrics" (photo_id, upload_date, photo_path, employee_id) FROM stdin;
8438f860-a4b8-4fba-b4e5-7b26602101de	2023-10-15	https://imgur.com/i6yuuCS	5c78cf38-2eb7-4125-82fa-fa3fca77ebd4
fbee3678-9b14-4298-8427-fcfdeecefa01	2023-11-20	https://imgur.com/3yjxuWr	eda4a48b-c1f4-4c0f-9bdc-bb0dd3432e5e
0f644e95-0a00-44f8-8447-09ead6f41883	2023-12-05	https://imgur.com/JeFNqSk	24c965b2-9ce4-4109-8216-7b1fbbdb101f
370e7ed3-b650-4bae-ad3a-38523b43ab78	2024-01-10	https://imgur.com/3yjxuWr	0664492a-4ca0-4ae5-9776-151d87b21f62
3ecbe40d-7127-4a7d-944c-f12372e0f0e4	2024-02-15	https://imgur.com/xIuuU8G	115373c4-5df7-43a8-9168-f0338642e253
b27a6780-4bd3-4ae3-9849-c5456ddb5669	2024-03-20	https://imgur.com/3yjxuWr	c85488a3-ea95-425b-bde5-71ddcfd76472
9961c25e-49bc-45b7-a9e3-eea0b283a82a	2024-04-25	https://imgur.com/3yjxuWr	f30f0634-f986-450c-be2f-46de6b10e1a7
81f3f96f-22ad-484f-813b-5940baecac43	2024-05-30	https://imgur.com/oXDJNom	909e356a-9621-4dcf-abbd-156f29e9025d
27b7d597-3bec-4136-8ec2-1f8ec7c8a034	2024-06-15	https://imgur.com/oXDJNom	c13c5e24-e767-4057-8f20-c9a63f7406e0
38d79385-6619-48dd-956c-70a940fd3fe5	2024-07-20	https://imgur.com/NHu7HEk	0f7d334a-ced4-4213-812f-1be595992ef7
4be30605-2a1a-411f-a5fd-8717953e91e1	2024-08-05	https://imgur.com/xIuuU8G	e41a4546-cd21-42d3-ad39-df715c96e9d0
53bd13d5-ff2c-4607-b81d-c813286100c7	2024-09-10	https://imgur.com/xIuuU8G	523fc5a7-5e1a-46f2-8594-618add9af3b3
7eedafec-1b72-4c2d-a4e2-17280983dfd4	2024-10-15	https://imgur.com/i6yuuCS	4bed6660-610b-41ae-b4e7-c15657953e6c
ba3be14c-8eff-4334-8f7d-59b1911d8f06	2024-11-20	https://imgur.com/xIuuU8G	80ec9ca4-ca01-488a-a8c1-ccf3ac9581d8
ee3f6ed9-149a-49d8-ba30-7a4e75e83b3f	2024-12-05	https://imgur.com/JeFNqSk	de7baed7-9ec0-422b-85f7-daa2556dfd11
\.


--
-- Data for Name: Department; Type: TABLE DATA; Schema: mdp; Owner: postgres
--

COPY mdp."Department" (department_id, name) FROM stdin;
fcfdf499-6c8d-4f7f-b18b-7b721fd8f780	Отдел разработки программного обеспечения
a876c5f3-7870-4277-a908-861efc855ac7	Отдел тестирования и качества
9aeac09d-f6f3-4206-8be8-77038fa2454b	Отдел IT-инфраструктуры
adafca3c-3b4c-4bec-9f6e-f2f15cbbf377	Отдел кибербезопасности
cff6d724-eae5-4ee8-a27e-c62184ff2605	Отдел поддержки пользователей
56b06060-d28d-4b29-aec1-46f8dd4e1b3d	Отдел проектного менеджмента
7c855f73-03e2-43f5-be86-45298c681af4	Отдел аналитики и данных
6a93c094-d80c-4576-a1b0-afd7584771af	Отдел маркетинга и продаж
a9f0b5f6-063b-4c47-a6da-96907c4c626c	Отдел обучения и развития
ed72c0f6-05c2-43e4-8c2c-d1e66f3bd192	Отдел исследований и разработок (R&D)
\.


--
-- Data for Name: Employee; Type: TABLE DATA; Schema: mdp; Owner: postgres
--

COPY mdp."Employee" (employee_id, first_name, second_name, patronymic, position_id, department_id, employee_photo) FROM stdin;
5c78cf38-2eb7-4125-82fa-fa3fca77ebd4	Иван	Иванов	Иванович	3193608f-3099-4ea9-8e76-94dfea689c85	fcfdf499-6c8d-4f7f-b18b-7b721fd8f780	https://avatars.githubusercontent.com/u/145202278?v=4
eda4a48b-c1f4-4c0f-9bdc-bb0dd3432e5e	Анна	Петрова	Сергеевна	ba958717-081a-4557-8f1f-8bc2cfd8a192	a876c5f3-7870-4277-a908-861efc855ac7	https://avatars.githubusercontent.com/u/145202278?v=4
24c965b2-9ce4-4109-8216-7b1fbbdb101f	Сергей	Смирнов	Александрович	86c833d7-6b52-4208-8e20-30d6321da99f	9aeac09d-f6f3-4206-8be8-77038fa2454b	https://avatars.githubusercontent.com/u/145202278?v=4
0664492a-4ca0-4ae5-9776-151d87b21f62	Елена	Кузнецова	Владимировна	a8c528ec-3be3-487a-b6a4-9041c8b2862e	adafca3c-3b4c-4bec-9f6e-f2f15cbbf377	https://avatars.githubusercontent.com/u/145202278?v=4
115373c4-5df7-43a8-9168-f0338642e253	Дмитрий	Попов	Михайлович	b3b0b850-6364-4873-b577-88380b8fd636	56b06060-d28d-4b29-aec1-46f8dd4e1b3d	https://avatars.githubusercontent.com/u/145202278?v=4
c85488a3-ea95-425b-bde5-71ddcfd76472	Ольга	Васильева	Алексеевна	777ff69a-47fd-48b0-b655-58de7002b29f	7c855f73-03e2-43f5-be86-45298c681af4	https://avatars.githubusercontent.com/u/145202278?v=4
f30f0634-f986-450c-be2f-46de6b10e1a7	Алексей	Соколов	Дмитриевич	36adbee8-dfa7-4e38-ae78-5517bd4e6e1a	6a93c094-d80c-4576-a1b0-afd7584771af	https://avatars.githubusercontent.com/u/145202278?v=4
909e356a-9621-4dcf-abbd-156f29e9025d	Мария	Михайлова	Сергеевна	7e1a8c6a-d127-4ef5-be41-90f9d098ce3e	6a93c094-d80c-4576-a1b0-afd7584771af	https://avatars.githubusercontent.com/u/145202278?v=4
c13c5e24-e767-4057-8f20-c9a63f7406e0	Николай	Фёдоров	Игоревич	a0469a89-f7c8-4ca5-945c-5721d3003a52	a9f0b5f6-063b-4c47-a6da-96907c4c626c	https://avatars.githubusercontent.com/u/145202278?v=4
0f7d334a-ced4-4213-812f-1be595992ef7	Екатерина	Морозова	Александровна	a43e5324-87be-4f56-929a-553352418144	9aeac09d-f6f3-4206-8be8-77038fa2454b	https://avatars.githubusercontent.com/u/145202278?v=4
e41a4546-cd21-42d3-ad39-df715c96e9d0	Павел	Волков	Викторович	29524e26-41c2-4938-9fc2-0fa1ea0e32f2	fcfdf499-6c8d-4f7f-b18b-7b721fd8f780	https://avatars.githubusercontent.com/u/145202278?v=4
523fc5a7-5e1a-46f2-8594-618add9af3b3	Наталья	Алексеева	Владимировна	11cfda93-3db7-4d94-9e1c-7ec7ef86327d	fcfdf499-6c8d-4f7f-b18b-7b721fd8f780	https://avatars.githubusercontent.com/u/145202278?v=4
4bed6660-610b-41ae-b4e7-c15657953e6c	Андрей	Лебедев	Сергеевич	f6b50278-8f93-47b3-8f95-db578aa5cc13	ed72c0f6-05c2-43e4-8c2c-d1e66f3bd192	https://avatars.githubusercontent.com/u/145202278?v=4
80ec9ca4-ca01-488a-a8c1-ccf3ac9581d8	Татьяна	Семёнова	Александровна	f2c0ff7e-697a-4ef1-adca-9e968bc6a666	cff6d724-eae5-4ee8-a27e-c62184ff2605	https://avatars.githubusercontent.com/u/145202278?v=4
de7baed7-9ec0-422b-85f7-daa2556dfd11	Михаил	Ефимов	Дмитриевич	e790069b-ed81-4399-a872-8d30c247d9a6	9aeac09d-f6f3-4206-8be8-77038fa2454b	https://avatars.githubusercontent.com/u/145202278?v=4
\.


--
-- Data for Name: Event; Type: TABLE DATA; Schema: mdp; Owner: postgres
--

COPY mdp."Event" (event_id, event_name, event_date, start_time, end_time, description, event_video) FROM stdin;
29e93696-5cbd-4743-8fb9-ad65ca9780e6	Конференция по ИИ и компьютерному зрению	2023-10-15	09:00:00	12:00:00	Конференция, посвященная последним достижениям в области искусственного интеллекта и компьютерного зрения. Участники обсудят новейшие алгоритмы и технологии, а также их применение в различных отраслях.	\N
db08e6d1-3e2f-45e2-b522-28d127b9f271	Семинар по биометрической безопасности	2023-11-20	10:30:00	13:30:00	Семинар, направленный на изучение современных методов биометрической безопасности. Участники узнают о новых технологиях и подходах к защите данных и личности.	\N
b98d0ed9-63f6-42ce-ad6e-e86f2bcb50e8	Вебинар по распознаванию лиц	2023-12-05	14:00:00	17:00:00	Вебинар, посвященный технологиям распознавания лиц. Участники узнают о принципах работы систем распознавания лиц, их применении и текущих вызовах.	\N
4ce9903a-a31f-4294-99b9-fee7b644e44f	Форум по инновациям в видеонаблюдении	2024-01-10	16:00:00	19:00:00	Форум, на котором будут обсуждаться инновации в области видеонаблюдения. Участники смогут узнать о новых технологиях и решениях, которые делают видеонаблюдение более эффективным и безопасным.	\N
bc741f01-e667-4dfb-96e1-4d63352ff6a4	Мастер-класс по разработке веб-приложений	2024-02-15	08:45:00	12:45:00	Мастер-класс, направленный на обучение разработке веб-приложений. Участники научатся создавать современные и функциональные веб-приложения с использованием передовых технологий.	\N
ca496de9-8fae-413c-a002-5d463089b774	Тренинг по использованию систем распознавания лиц	2024-03-20	11:15:00	14:15:00	Тренинг, направленный на обучение использованию систем распознавания лиц. Участники научатся настраивать и использовать системы распознавания лиц для различных задач.	\N
26e53c42-fa7b-419a-934e-6d69998fef7f	Встреча с экспертами по кибербезопасности	2024-04-25	15:30:00	18:30:00	Встреча с ведущими экспертами в области кибербезопасности. Участники смогут задать вопросы и обсудить актуальные проблемы и решения в области кибербезопасности.	\N
f32d36d8-5fa8-43aa-8463-0e6af7c2e4b9	Лекция по современным методам видеоаналитики	2024-05-30	17:00:00	20:00:00	Лекция, посвященная современным методам видеоаналитики. Участники узнают о новых подходах и технологиях, которые используются для анализа видеоданных.	\N
823abe72-9ea8-455f-9e8f-7b5b935dad9f	Вебинар по интеграции биометрических данных в веб-приложения	2024-06-15	09:30:00	12:30:00	Вебинар, посвященный интеграции биометрических данных в веб-приложения. Участники узнают о методах и инструментах, которые позволяют эффективно использовать биометрические данные в веб-приложениях.	\N
82297428-a227-47b0-bae5-eabe1cdd8043	string	2024-11-10	14:31:58.742	14:31:58.742	string	videos/82297428-a227-47b0-bae5-eabe1cdd8043.mp4
db165fc7-3365-4b1b-9542-77cb69c91f3a	Обучающий семинар по работе с видеопотоками	2024-07-20	13:00:00	16:00:00	Обучающий семинар, направленный на изучение работы с видеопотоками. Участники научатся обрабатывать и анализировать видеопотоки с использованием современных технологий.	\N
\.


--
-- Data for Name: Invitation; Type: TABLE DATA; Schema: mdp; Owner: postgres
--

COPY mdp."Invitation" (event_id, employee_id) FROM stdin;
29e93696-5cbd-4743-8fb9-ad65ca9780e6	5c78cf38-2eb7-4125-82fa-fa3fca77ebd4
b98d0ed9-63f6-42ce-ad6e-e86f2bcb50e8	24c965b2-9ce4-4109-8216-7b1fbbdb101f
4ce9903a-a31f-4294-99b9-fee7b644e44f	0664492a-4ca0-4ae5-9776-151d87b21f62
bc741f01-e667-4dfb-96e1-4d63352ff6a4	115373c4-5df7-43a8-9168-f0338642e253
ca496de9-8fae-413c-a002-5d463089b774	c85488a3-ea95-425b-bde5-71ddcfd76472
26e53c42-fa7b-419a-934e-6d69998fef7f	f30f0634-f986-450c-be2f-46de6b10e1a7
f32d36d8-5fa8-43aa-8463-0e6af7c2e4b9	909e356a-9621-4dcf-abbd-156f29e9025d
823abe72-9ea8-455f-9e8f-7b5b935dad9f	c13c5e24-e767-4057-8f20-c9a63f7406e0
db165fc7-3365-4b1b-9542-77cb69c91f3a	0f7d334a-ced4-4213-812f-1be595992ef7
29e93696-5cbd-4743-8fb9-ad65ca9780e6	0f7d334a-ced4-4213-812f-1be595992ef7
db08e6d1-3e2f-45e2-b522-28d127b9f271	e41a4546-cd21-42d3-ad39-df715c96e9d0
b98d0ed9-63f6-42ce-ad6e-e86f2bcb50e8	523fc5a7-5e1a-46f2-8594-618add9af3b3
4ce9903a-a31f-4294-99b9-fee7b644e44f	4bed6660-610b-41ae-b4e7-c15657953e6c
bc741f01-e667-4dfb-96e1-4d63352ff6a4	80ec9ca4-ca01-488a-a8c1-ccf3ac9581d8
ca496de9-8fae-413c-a002-5d463089b774	de7baed7-9ec0-422b-85f7-daa2556dfd11
4ce9903a-a31f-4294-99b9-fee7b644e44f	80ec9ca4-ca01-488a-a8c1-ccf3ac9581d8
ca496de9-8fae-413c-a002-5d463089b774	f30f0634-f986-450c-be2f-46de6b10e1a7
26e53c42-fa7b-419a-934e-6d69998fef7f	eda4a48b-c1f4-4c0f-9bdc-bb0dd3432e5e
823abe72-9ea8-455f-9e8f-7b5b935dad9f	0664492a-4ca0-4ae5-9776-151d87b21f62
db08e6d1-3e2f-45e2-b522-28d127b9f271	eda4a48b-c1f4-4c0f-9bdc-bb0dd3432e5e
\.


--
-- Data for Name: Position; Type: TABLE DATA; Schema: mdp; Owner: postgres
--

COPY mdp."Position" (position_id, name) FROM stdin;
3193608f-3099-4ea9-8e76-94dfea689c85	Разработчик программного обеспечения
ba958717-081a-4557-8f1f-8bc2cfd8a192	Тестировщик
86c833d7-6b52-4208-8e20-30d6321da99f	Системный администратор
a8c528ec-3be3-487a-b6a4-9041c8b2862e	Специалист по кибербезопасности
b3b0b850-6364-4873-b577-88380b8fd636	Проектный менеджер
777ff69a-47fd-48b0-b655-58de7002b29f	Аналитик данных
36adbee8-dfa7-4e38-ae78-5517bd4e6e1a	Маркетолог
7e1a8c6a-d127-4ef5-be41-90f9d098ce3e	Менеджер по продажам
a0469a89-f7c8-4ca5-945c-5721d3003a52	Тренер по обучению
a43e5324-87be-4f56-929a-553352418144	DevOps-инженер
29524e26-41c2-4938-9fc2-0fa1ea0e32f2	UX/UI дизайнер
11cfda93-3db7-4d94-9e1c-7ec7ef86327d	Архитектор программного обеспечения
f6b50278-8f93-47b3-8f95-db578aa5cc13	Специалист по машинному обучению
f2c0ff7e-697a-4ef1-adca-9e968bc6a666	Специалист технической поддержки
e790069b-ed81-4399-a872-8d30c247d9a6	Специалист по IT-поддержке
\.


--
-- Data for Name: Visit; Type: TABLE DATA; Schema: mdp; Owner: postgres
--

COPY mdp."Visit" (visit_id, employee_id, event_id) FROM stdin;
e3348584-7613-4225-8f31-3845fa191680	5c78cf38-2eb7-4125-82fa-fa3fca77ebd4	29e93696-5cbd-4743-8fb9-ad65ca9780e6
f9aed24d-e83d-4026-a337-3d886a6aa184	eda4a48b-c1f4-4c0f-9bdc-bb0dd3432e5e	db08e6d1-3e2f-45e2-b522-28d127b9f271
cf5e65ab-328d-4ad4-93a2-e8ea33e1fe27	24c965b2-9ce4-4109-8216-7b1fbbdb101f	b98d0ed9-63f6-42ce-ad6e-e86f2bcb50e8
419e7d6c-4957-49ae-953f-d24ad7136083	0664492a-4ca0-4ae5-9776-151d87b21f62	4ce9903a-a31f-4294-99b9-fee7b644e44f
b0185313-d968-4a21-baaf-e13797a320cc	115373c4-5df7-43a8-9168-f0338642e253	bc741f01-e667-4dfb-96e1-4d63352ff6a4
2559c0d6-01e7-4a86-a65c-5551ea9eef48	c85488a3-ea95-425b-bde5-71ddcfd76472	ca496de9-8fae-413c-a002-5d463089b774
5b3ed998-fe3d-4b5b-a2d6-6839a7701196	f30f0634-f986-450c-be2f-46de6b10e1a7	26e53c42-fa7b-419a-934e-6d69998fef7f
6a47b221-ec95-420b-994d-7c7d7e291edf	909e356a-9621-4dcf-abbd-156f29e9025d	f32d36d8-5fa8-43aa-8463-0e6af7c2e4b9
d1e53fb2-de7b-4344-a67a-8ade69d4095d	c13c5e24-e767-4057-8f20-c9a63f7406e0	823abe72-9ea8-455f-9e8f-7b5b935dad9f
a38e92b5-a87f-4ec7-8005-5bc25bc74f88	0f7d334a-ced4-4213-812f-1be595992ef7	db165fc7-3365-4b1b-9542-77cb69c91f3a
52108de8-ba02-4a04-88a5-64b2fe4b0a48	0f7d334a-ced4-4213-812f-1be595992ef7	29e93696-5cbd-4743-8fb9-ad65ca9780e6
999c0a06-b68b-41c3-b679-101a5b642887	e41a4546-cd21-42d3-ad39-df715c96e9d0	db08e6d1-3e2f-45e2-b522-28d127b9f271
38e18b1e-693b-461e-a7ad-f3bff9fde768	523fc5a7-5e1a-46f2-8594-618add9af3b3	b98d0ed9-63f6-42ce-ad6e-e86f2bcb50e8
b7432b89-af6f-4974-8da0-9e1e1906a1f8	4bed6660-610b-41ae-b4e7-c15657953e6c	4ce9903a-a31f-4294-99b9-fee7b644e44f
8118b986-81ff-4ef4-b481-008e13a3337e	80ec9ca4-ca01-488a-a8c1-ccf3ac9581d8	bc741f01-e667-4dfb-96e1-4d63352ff6a4
\.


--
-- Data for Name: VisitMark; Type: TABLE DATA; Schema: mdp; Owner: postgres
--

COPY mdp."VisitMark" (mark_id, fixation_time, photo_path, visit_id) FROM stdin;
5a631ebf-c52b-4199-a7b3-7a15b2d87d63	08:30:00	https://imgur.com/undefined	e3348584-7613-4225-8f31-3845fa191680
db716856-734f-4a69-ac00-ab103fc776f3	09:45:00	https://imgur.com/undefined\r\n	f9aed24d-e83d-4026-a337-3d886a6aa184
966a12dc-823f-43e6-8fc3-fb508dfe7ca2	10:15:00	https://imgur.com/undefined\r\n	cf5e65ab-328d-4ad4-93a2-e8ea33e1fe27
e38f99b3-6469-4d29-a83a-a4139c99f610	11:30:00	https://imgur.com/undefined	419e7d6c-4957-49ae-953f-d24ad7136083
c988c50e-97cf-4e4a-94a3-4d14740b71da	12:45:00	https://imgur.com/undefined\r\n	b0185313-d968-4a21-baaf-e13797a320cc
cf7e96fd-01a2-4709-adf4-8e5f1aa54fb0	13:00:00	https://imgur.com/undefined\r\n	2559c0d6-01e7-4a86-a65c-5551ea9eef48
f0b23994-a410-4a94-8620-12539505aaf0	14:15:00	https://imgur.com/undefined\r\n	5b3ed998-fe3d-4b5b-a2d6-6839a7701196
8a598f69-f76e-4a44-acda-ee9d30cf9bf8	15:30:00	https://imgur.com/undefined\r\n	6a47b221-ec95-420b-994d-7c7d7e291edf
15f15bee-f02a-4acb-8f73-2005829c5bbd	16:45:00	https://imgur.com/undefined\r\n	d1e53fb2-de7b-4344-a67a-8ade69d4095d
419da49a-d588-4be0-b184-cdbe59226013	17:00:00	https://imgur.com/undefined\r\n	a38e92b5-a87f-4ec7-8005-5bc25bc74f88
d5022cec-70dd-4ff7-a695-4fd64a945046	18:15:00	https://imgur.com/undefined\r\n	52108de8-ba02-4a04-88a5-64b2fe4b0a48
0ef21bb7-af45-487e-beb9-c98fe6e5b825	19:30:00	https://imgur.com/undefined\r\n	999c0a06-b68b-41c3-b679-101a5b642887
7aa06f2a-fd3f-4673-ac4f-0d108e056f8a	20:45:00	https://imgur.com/undefined\r\n	38e18b1e-693b-461e-a7ad-f3bff9fde768
dc8df4d5-31e3-47d0-ae2f-df6c1bdc48b4	21:00:00	https://imgur.com/undefined\r\n	b7432b89-af6f-4974-8da0-9e1e1906a1f8
52c2d225-4e37-4bff-b386-b44e67913eeb	22:15:00	https://imgur.com/undefined\r\n	8118b986-81ff-4ef4-b481-008e13a3337e
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

