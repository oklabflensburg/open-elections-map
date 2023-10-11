--
-- PostgreSQL database dump
--

-- Dumped from database version 14.7 (Ubuntu 14.7-1.pgdg22.04+1)
-- Dumped by pg_dump version 15.2 (Ubuntu 15.2-1.pgdg22.04+1)

-- Started on 2023-05-18 17:47:30 CEST

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 213 (class 1259 OID 26602)
-- Name: votes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.votes (
    id integer NOT NULL,
    created_at timestamp with time zone DEFAULT now(),
    gemeinde character varying(255) NOT NULL,
    wahlkreisnummer character varying(255) NOT NULL,
    erfassungsgebietsnummer character varying(255) NOT NULL,
    erfassungsgebietsart character varying(255) NOT NULL,
    ausgezaehlt_abweichend_gebiet character varying(255) NOT NULL,
    ausgezaehlt_abweichend_ags character varying(255),
    ausbleibend character varying(10),
    wahlberechtigte_gesamt integer,
    wahlberechtigte_ohne_wahlschein integer,
    wahlberechtigte_mit_wahlschein integer,
    wahlberechtigte_nicht_im_wvz integer,
    waehlende_gesamt integer,
    waehlende_ohne_wahlschein integer,
    waehlende_mit_wahlschein integer,
    urnenwaehlende_mit_wahlschein_in_urnenwahllokal integer,
    briefwaehlende_mit_wahlschein_in_urnenwahllokal integer,
    stimmen_ungueltige integer,
    stimmen_gueltige integer,
    d1 integer,
    d2 integer,
    d3 integer,
    d4 integer,
    d5 integer,
    d6 integer,
    d7 integer,
    d8 integer,
    d9 integer,
    d10 integer,
    d11 integer,
    d12 integer,
    d13 integer,
    d14 integer,
    d15 integer,
    d17 integer,
    d18 integer,
    d19 integer,
    d20 integer,
    d21 integer,
    d22 integer,
    d23 integer
);


ALTER TABLE public.votes OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 26601)
-- Name: votes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.votes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.votes_id_seq OWNER TO postgres;

--
-- TOC entry 3373 (class 0 OID 0)
-- Dependencies: 212
-- Name: votes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.votes_id_seq OWNED BY public.votes.id;


--
-- TOC entry 3223 (class 2604 OID 26605)
-- Name: votes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.votes ALTER COLUMN id SET DEFAULT nextval('public.votes_id_seq'::regclass);


--
-- TOC entry 3367 (class 0 OID 26602)
-- Dependencies: 213
-- Data for Name: votes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.votes (id, created_at, gemeinde, wahlkreisnummer, erfassungsgebietsnummer, erfassungsgebietsart, ausgezaehlt_abweichend_gebiet, ausgezaehlt_abweichend_ags, ausbleibend, wahlberechtigte_gesamt, wahlberechtigte_ohne_wahlschein, wahlberechtigte_mit_wahlschein, wahlberechtigte_nicht_im_wvz, waehlende_gesamt, waehlende_ohne_wahlschein, waehlende_mit_wahlschein, urnenwaehlende_mit_wahlschein_in_urnenwahllokal, briefwaehlende_mit_wahlschein_in_urnenwahllokal, stimmen_ungueltige, stimmen_gueltige, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d17, d18, d19, d20, d21, d22, d23) FROM stdin;
\.


--
-- TOC entry 3374 (class 0 OID 0)
-- Dependencies: 212
-- Name: votes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.votes_id_seq', 2648, true);


--
-- TOC entry 3226 (class 2606 OID 26610)
-- Name: votes votes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.votes
    ADD CONSTRAINT votes_pkey PRIMARY KEY (id);


-- Completed on 2023-05-18 17:47:32 CEST

--
-- PostgreSQL database dump complete
--

