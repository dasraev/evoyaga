--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

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
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL,
    code smallint,
    CONSTRAINT auth_group_code_check CHECK ((code >= 0))
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: district; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.district (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    name character varying(255) NOT NULL,
    soato character varying(9) NOT NULL,
    mvd_profilactic_district_id integer,
    created_by_id bigint,
    region_id_id uuid,
    updated_by_id bigint
);


ALTER TABLE public.district OWNER TO postgres;

--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: juvenile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.juvenile (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    father_name character varying(255) NOT NULL,
    birth_date date NOT NULL,
    photo character varying(100),
    gender character varying(1) NOT NULL,
    address character varying(255) NOT NULL,
    school_name character varying(255),
    arrived_date timestamp with time zone,
    issue_date timestamp with time zone,
    destination character varying(500),
    marital_status character varying(60),
    passport_seria character varying(255),
    arrived_reason_file character varying(100),
    passport_type character varying(30) NOT NULL,
    reference_type character varying(100),
    pinfl character varying(14) NOT NULL,
    count_came_back_to_center character varying(60),
    school_type character varying(60),
    prophylactic_list boolean,
    distribution_type character varying(60),
    level_kinkdship character varying(60),
    basis_distribution character varying(60),
    type_guardianship character varying(60),
    itm_direction character varying(60),
    itm_name character varying(255),
    rotm_type character varying(60),
    basis_sending_file character varying(100),
    is_out boolean NOT NULL,
    address_district_id uuid,
    arrived_reason character varying(60),
    birth_district_id uuid,
    created_by_id bigint,
    determined_location character varying(60),
    inspector_id uuid,
    itm_district_id uuid,
    markaz_id uuid,
    school_district_id uuid,
    updated_by_id bigint,
    convicted_list character varying(60),
    have_been_in_itm_reason character varying(60),
    have_been_in_rotm_reason character varying(60),
    status character varying(60),
    health_condition character varying(255),
    organization_coach_name character varying(255),
    organization_directors_name character varying(255),
    organization_psyhologs_name character varying(255),
    psyhology_condition character varying(255),
    skills_hobbies character varying(255)
);


ALTER TABLE public.juvenile OWNER TO postgres;

--
-- Name: juvenile_medical_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.juvenile_medical_list (
    id bigint NOT NULL,
    juvenile_id uuid NOT NULL,
    medical_list_id uuid NOT NULL
);


ALTER TABLE public.juvenile_medical_list OWNER TO postgres;

--
-- Name: juvenile_medical_list_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.juvenile_medical_list_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.juvenile_medical_list_id_seq OWNER TO postgres;

--
-- Name: juvenile_medical_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.juvenile_medical_list_id_seq OWNED BY public.juvenile_medical_list.id;


--
-- Name: markaz; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.markaz (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    name character varying(255) NOT NULL,
    created_by_id bigint,
    region_id uuid,
    updated_by_id bigint
);


ALTER TABLE public.markaz OWNER TO postgres;

--
-- Name: medical_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medical_list (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    title character varying(255),
    created_by_id bigint,
    updated_by_id bigint
);


ALTER TABLE public.medical_list OWNER TO postgres;

--
-- Name: parent_juvenile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parent_juvenile (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    father_name character varying(255) NOT NULL,
    birth_date date NOT NULL,
    employment text,
    created_by_id bigint,
    updated_by_id bigint,
    pinfl character varying(14) NOT NULL
);


ALTER TABLE public.parent_juvenile OWNER TO postgres;

--
-- Name: prophylactic_inspector; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prophylactic_inspector (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    first_name character varying(255),
    last_name character varying(255),
    father_name character varying(255),
    inspector_id integer,
    pinfl character varying(14) NOT NULL,
    inspector_type character varying(30),
    created_by_id bigint,
    updated_by_id bigint
);


ALTER TABLE public.prophylactic_inspector OWNER TO postgres;

--
-- Name: region; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.region (
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    id uuid NOT NULL,
    name character varying(255) NOT NULL,
    soato character varying(9) NOT NULL,
    mvd_profilactic_region_id integer,
    created_by_id bigint,
    updated_by_id bigint
);


ALTER TABLE public.region OWNER TO postgres;

--
-- Name: relationship; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.relationship (
    id bigint NOT NULL,
    parent_type character varying(60),
    juvenile_id uuid NOT NULL,
    parent_id uuid NOT NULL
);


ALTER TABLE public.relationship OWNER TO postgres;

--
-- Name: relationship_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.relationship_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.relationship_id_seq OWNER TO postgres;

--
-- Name: relationship_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.relationship_id_seq OWNED BY public.relationship.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    email character varying(254) NOT NULL,
    login character varying(255) NOT NULL,
    username character varying(200) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    father_name character varying(150) NOT NULL,
    photo character varying(100),
    birth_date date,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    markaz_id uuid
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- Name: user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_groups (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.user_groups OWNER TO postgres;

--
-- Name: user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_groups_id_seq OWNER TO postgres;

--
-- Name: user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_groups_id_seq OWNED BY public.user_groups.id;


--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_user_permissions (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.user_user_permissions OWNER TO postgres;

--
-- Name: user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_user_permissions_id_seq OWNED BY public.user_user_permissions.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: juvenile_medical_list id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile_medical_list ALTER COLUMN id SET DEFAULT nextval('public.juvenile_medical_list_id_seq'::regclass);


--
-- Name: relationship id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.relationship ALTER COLUMN id SET DEFAULT nextval('public.relationship_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_groups ALTER COLUMN id SET DEFAULT nextval('public.user_groups_id_seq'::regclass);


--
-- Name: user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.user_user_permissions_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name, code) FROM stdin;
1	Navbatchi	3
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	1	6
7	1	7
8	1	8
9	1	9
10	1	10
11	1	11
12	1	12
13	1	13
14	1	14
15	1	15
16	1	16
17	1	17
18	1	18
19	1	19
20	1	20
21	1	21
22	1	22
23	1	23
24	1	24
25	1	25
26	1	26
27	1	27
28	1	28
29	1	29
30	1	30
31	1	31
32	1	32
33	1	33
34	1	34
35	1	35
36	1	36
37	1	37
38	1	38
39	1	39
40	1	40
41	1	41
42	1	42
43	1	43
44	1	44
45	1	45
46	1	46
47	1	47
48	1	48
49	1	49
50	1	50
51	1	51
52	1	52
53	1	53
54	1	54
55	1	55
56	1	56
57	1	57
58	1	58
59	1	59
60	1	60
61	1	61
62	1	62
63	1	63
64	1	64
65	1	65
66	1	66
67	1	67
68	1	68
69	1	69
70	1	70
71	1	71
72	1	72
73	1	73
74	1	74
75	1	75
76	1	76
77	1	77
78	1	78
79	1	79
80	1	80
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add school type	6	add_schooltype
22	Can change school type	6	change_schooltype
23	Can delete school type	6	delete_schooltype
24	Can view school type	6	view_schooltype
25	Can add region	7	add_region
26	Can change region	7	change_region
27	Can delete region	7	delete_region
28	Can view region	7	view_region
29	Can add markaz	8	add_markaz
30	Can change markaz	8	change_markaz
31	Can delete markaz	8	delete_markaz
32	Can view markaz	8	view_markaz
33	Can add district	9	add_district
34	Can change district	9	change_district
35	Can delete district	9	delete_district
36	Can view district	9	view_district
37	Can add determined location	10	add_determinedlocation
38	Can change determined location	10	change_determinedlocation
39	Can delete determined location	10	delete_determinedlocation
40	Can view determined location	10	view_determinedlocation
41	Can add arrived reason	11	add_arrivedreason
42	Can change arrived reason	11	change_arrivedreason
43	Can delete arrived reason	11	delete_arrivedreason
44	Can view arrived reason	11	view_arrivedreason
45	Can add custom user	12	add_customuser
46	Can change custom user	12	change_customuser
47	Can delete custom user	12	delete_customuser
48	Can view custom user	12	view_customuser
49	Can add convicted list	13	add_convictedlist
50	Can change convicted list	13	change_convictedlist
51	Can delete convicted list	13	delete_convictedlist
52	Can view convicted list	13	view_convictedlist
53	Can add juvenile	14	add_juvenile
54	Can change juvenile	14	change_juvenile
55	Can delete juvenile	14	delete_juvenile
56	Can view juvenile	14	view_juvenile
57	Can add juvenile parent	15	add_juvenileparent
58	Can change juvenile parent	15	change_juvenileparent
59	Can delete juvenile parent	15	delete_juvenileparent
60	Can view juvenile parent	15	view_juvenileparent
61	Can add relationship	16	add_relationship
62	Can change relationship	16	change_relationship
63	Can delete relationship	16	delete_relationship
64	Can view relationship	16	view_relationship
65	Can add prophylactic inspector	17	add_prophylacticinspector
66	Can change prophylactic inspector	17	change_prophylacticinspector
67	Can delete prophylactic inspector	17	delete_prophylacticinspector
68	Can view prophylactic inspector	17	view_prophylacticinspector
69	Can add medical list	18	add_medicallist
70	Can change medical list	18	change_medicallist
71	Can delete medical list	18	delete_medicallist
72	Can view medical list	18	view_medicallist
73	Can add juvenile medical list	19	add_juvenilemedicallist
74	Can change juvenile medical list	19	change_juvenilemedicallist
75	Can delete juvenile medical list	19	delete_juvenilemedicallist
76	Can view juvenile medical list	19	view_juvenilemedicallist
77	Can add juvenile convicted list	20	add_juvenileconvictedlist
78	Can change juvenile convicted list	20	change_juvenileconvictedlist
79	Can delete juvenile convicted list	20	delete_juvenileconvictedlist
80	Can view juvenile convicted list	20	view_juvenileconvictedlist
\.


--
-- Data for Name: district; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.district (id, created_at, updated_at, name, soato, mvd_profilactic_district_id, created_by_id, region_id_id, updated_by_id) FROM stdin;
106ac452-53ee-443d-a236-3842eea2114c	2022-03-30 07:08:53.051073+00	2022-03-30 07:08:53.051073+00	Oltinko'l tumani	1703202	9	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
33a425e3-5152-4dbd-8c62-5638ea4383dd	2022-03-30 07:08:53.056059+00	2022-03-30 07:08:53.056059+00	Andijon tumani	1703203	15	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
4ecf74f6-542f-4d84-8590-dda9b6cb2573	2022-03-30 07:08:53.057033+00	2022-03-30 07:08:53.057033+00	Andijon shahri	1703401	14	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
2e639992-13a1-4d5e-b7cb-a0889977df8a	2022-03-30 07:08:53.057033+00	2022-03-30 07:08:53.057033+00	Baliqchi tumani	1703206	1	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
9cb26ea5-1442-4908-a319-68223edbe07b	2022-03-30 07:08:53.05803+00	2022-03-30 07:08:53.05803+00	Bo'z tumani	1703209	2	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
7bc4f9bc-4305-4c77-99dc-e3c37628d401	2022-03-30 07:08:53.05803+00	2022-03-30 07:08:53.059028+00	Buloqboshi tumani	1703210	3	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
5be4dbe0-2bf6-446d-b7f5-8534644e24ca	2022-03-30 07:08:53.060026+00	2022-03-30 07:08:53.060026+00	Jalaquduq tumani	1703211	5	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
86c411cd-f2de-4062-b941-cab2f19ac4a0	2022-03-30 07:08:53.061029+00	2022-03-30 07:08:53.061029+00	Izboskan tumani	1703214	4	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
3c04e9d9-22f6-47f8-9277-52b07568b410	2022-03-30 07:08:53.062045+00	2022-03-30 07:08:53.062045+00	Ulug'nor tumani	1703217	13	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
18ce6ae8-ac8d-4588-8f42-4922cc80d2f3	2022-03-30 07:08:53.062045+00	2022-03-30 07:08:53.062045+00	Qo'rg'ontepa tumani	1703220	11	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
6f06de86-ab48-4028-bf29-e76b3999c860	2022-03-30 07:08:53.063028+00	2022-03-30 07:08:53.063028+00	Asaka tumani	1703224	16	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
f9e2d512-4d31-4fb7-beb8-fa2669a0c31c	2022-03-30 07:08:53.063028+00	2022-03-30 07:08:53.063028+00	Marxamat tumani	1703227	8	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
64d23b04-a333-4663-a327-457239b68d5c	2022-03-30 07:08:53.064038+00	2022-03-30 07:08:53.064038+00	Shaxrixon tumani	1703230	12	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
14f20497-3740-4d7e-8621-7068fe019293	2022-03-30 07:08:53.064038+00	2022-03-30 07:08:53.064038+00	Paxtaobod tumani	1703232	10	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
dec31eb5-af0e-4e56-8133-ab6479302829	2022-03-30 07:08:53.065038+00	2022-03-30 07:08:53.065038+00	Xo'jaobod tumani	1703236	7	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
31c8b8ef-916c-4668-8d2c-6e241bcc28ee	2022-03-30 07:08:53.065038+00	2022-03-30 07:08:53.065038+00	Olot tumani	1706204	23	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
2ed219d3-d9f8-4c59-8e3d-eb451408b10e	2022-03-30 07:08:53.066033+00	2022-03-30 07:08:53.066033+00	Buxoro tumani	1706207	18	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
24b8567b-c442-4ba8-b114-1687eb0ff3c2	2022-03-30 07:08:53.066033+00	2022-03-30 07:08:53.066033+00	Vobkent tumani	1706212	29	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
f37fae9d-6394-4c54-bfe7-71d490e9373b	2022-03-30 07:08:53.067033+00	2022-03-30 07:08:53.067033+00	G'ijduvon tumani	1706215	19	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
ffd45ed2-06bc-4823-a4d3-d6b0013eb8ed	2022-03-30 07:08:53.067033+00	2022-03-30 07:08:53.068003+00	Kogon tumani	1706219	22	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
286e95fa-0bf2-4e74-b774-a062ec903060	2022-03-30 07:08:53.068003+00	2022-03-30 07:08:53.068003+00	Qorako'l tumani	1706230	25	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
79977b67-fc00-4976-b5b1-32bd45dabca8	2022-03-30 07:08:53.068003+00	2022-03-30 07:08:53.068003+00	Qorovulbozor tumani	1706232	26	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
e0e95c84-9a21-49e3-9b48-763bb83559bd	2022-03-30 07:08:53.069001+00	2022-03-30 07:08:53.069001+00	Xonobod shahri	1703408	6	\N	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	\N
0e2207a7-658e-4c80-9a2a-1b6ce331502e	2022-03-30 07:08:53.069001+00	2022-03-30 07:08:53.069001+00	Peshku tumani	1706240	24	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
7537559f-0478-497e-86b1-56c83f8b05cd	2022-03-30 07:08:53.069998+00	2022-03-30 07:08:53.069998+00	Romitan tumani	1706242	27	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
b10b94ef-33d2-4299-8b04-c8679891d58b	2022-03-30 07:08:53.069998+00	2022-03-30 07:08:53.069998+00	Jondor tumani	1706246	20	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
53b0cc00-5301-4db3-925c-2c839a91f440	2022-03-30 07:08:53.070995+00	2022-03-30 07:08:53.070995+00	Shofirkon tumani	1706258	28	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
afdf51af-4e7f-4271-b5fb-76678679a7d0	2022-03-30 07:08:53.070995+00	2022-03-30 07:08:53.070995+00	Arnasoy tumani	1708201	49	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
94eab72e-ff6b-458e-a988-80dfe2e18e04	2022-03-30 07:08:53.071993+00	2022-03-30 07:08:53.071993+00	Baxmal tumani	1708204	50	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
dc1aeed3-8f8c-4b31-91f0-3a3c7b857cba	2022-03-30 07:08:53.07299+00	2022-03-30 07:08:53.07299+00	G'allaorol tumani	1708209	53	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
2b341f41-43e4-48eb-bc72-83b9fc4f14fd	2022-03-30 07:08:53.07299+00	2022-03-30 07:08:53.07299+00	Sharof Rashidov tumani	1708212	57	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
edea2c79-080e-44d4-ba2a-985ff5f05128	2022-03-30 07:08:53.073987+00	2022-03-30 07:08:53.073987+00	Do'stlik tumani	1708215	51	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
2f375be4-c231-422c-ba3d-5954c5869641	2022-03-30 07:08:53.073987+00	2022-03-30 07:08:53.073987+00	Zomin tumani	1708218	61	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
be1fdb7b-97e5-46c3-9ab0-8809ecfeacc3	2022-03-30 07:08:53.074985+00	2022-03-30 07:08:53.074985+00	Zarbdor tumani	1708220	60	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
9bb90b34-1e67-43c9-bfbe-14cf059f2095	2022-03-30 07:08:53.075984+00	2022-03-30 07:08:53.075984+00	Mirzacho'l tumani	1708223	55	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
6598a9a9-aa83-4e39-86f9-7b50d2fe13d2	2022-03-30 07:08:53.076981+00	2022-03-30 07:08:53.076981+00	Zafarobod tumani	1708225	59	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
68e79615-67d7-4b4b-ab30-0a2adaebc462	2022-03-30 07:08:53.076981+00	2022-03-30 07:08:53.076981+00	Paxtakor tumani	1708228	56	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
294023e7-c151-4121-b442-16d616627023	2022-03-30 07:08:53.077978+00	2022-03-30 07:08:53.077978+00	Forish tumani	1708235	52	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
38893d2a-39d7-4f7b-865d-6c242ef31fff	2022-03-30 07:08:53.077978+00	2022-03-30 07:08:53.077978+00	Yangiobod tumani	1708237	58	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
0dbe07b4-ee7a-4145-81d0-1b3af059a090	2022-03-30 07:08:53.078974+00	2022-03-30 07:08:53.078974+00	G'uzor tumani	1710207	65	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
102141c4-6054-4723-a4b7-d70aca016181	2022-03-30 07:08:53.078974+00	2022-03-30 07:08:53.078974+00	Dehqonobod tumani	1710212	64	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
5758ed26-bfdc-4079-8dc0-fee622dcb555	2022-03-30 07:08:53.079971+00	2022-03-30 07:08:53.079971+00	Qamashi tumani	1710220	72	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
e9710f52-8bb1-439b-93fb-1039fb6ce470	2022-03-30 07:08:53.079971+00	2022-03-30 07:08:53.079971+00	Qarshi tumani	1710224	74	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
d836756c-342a-439f-a7f6-9391fe3986bc	2022-03-30 07:08:53.080969+00	2022-03-30 07:08:53.080969+00	Koson tumani	1710229	68	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
6c3814f8-5456-447b-b4c9-cb09567bbc42	2022-03-30 07:08:53.080969+00	2022-03-30 07:08:53.080969+00	Kitob tumani	1710232	67	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
15c75748-2c9a-4155-8585-7e858516bb23	2022-03-30 07:08:53.081966+00	2022-03-30 07:08:53.081966+00	Mirishkor tumani	1710233	69	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
c448bfcd-a866-4bba-a093-215b32052aa9	2022-03-30 07:08:53.081966+00	2022-03-30 07:08:53.081966+00	Muborak tumani	1710234	70	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
85ed226d-3ca8-4564-bdba-88931829fa59	2022-03-30 07:08:53.082964+00	2022-03-30 07:08:53.082964+00	Nishon tumani	1710235	71	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
c262642f-0845-4ded-8215-af3ee5c491f4	2022-03-30 07:08:53.082964+00	2022-03-30 07:08:53.082964+00	Kasbi tumani	1710237	66	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
6e274f41-4e18-4155-970c-47e1e11a7234	2022-03-30 07:08:53.083961+00	2022-03-30 07:08:53.083961+00	Chiroqchi tumani	1710242	63	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
463a960a-33e3-4986-84a8-d2b67e809ae3	2022-03-30 07:08:53.083961+00	2022-03-30 07:08:53.083961+00	Shahrisabz tumani	1710245	76	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
cfdadb24-cc6f-4a22-a875-7ad0cf64a70e	2022-03-30 07:08:53.084959+00	2022-03-30 07:08:53.084959+00	Yakkabog' tumani	1710250	77	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
b0ddca6c-be51-4f11-8c6d-183497fe6fe4	2022-03-30 07:08:53.084959+00	2022-03-30 07:08:53.084959+00	Konimex tumani	1712211	106	\N	c7dcf9ef-5b8a-4a58-b440-38503c26be25	\N
d783930f-02f8-46e5-b6b1-b4a767f2624c	2022-03-30 07:08:53.085955+00	2022-03-30 07:08:53.085955+00	Qiziltepa tumani	1712216	110	\N	c7dcf9ef-5b8a-4a58-b440-38503c26be25	\N
a0bed818-327c-46af-8683-5e80c54b7480	2022-03-30 07:08:53.085955+00	2022-03-30 07:08:53.085955+00	Navbahor tumani	1712230	107	\N	c7dcf9ef-5b8a-4a58-b440-38503c26be25	\N
196086dd-5cb3-49e4-8119-ddff23e213f9	2022-03-30 07:08:53.086953+00	2022-03-30 07:08:53.086953+00	Karmana tumani	1712234	104	\N	c7dcf9ef-5b8a-4a58-b440-38503c26be25	\N
5436a8d4-2c75-492f-be40-21bc3da274ca	2022-03-30 07:08:53.086953+00	2022-03-30 07:08:53.086953+00	Nurota tumani	1712238	109	\N	c7dcf9ef-5b8a-4a58-b440-38503c26be25	\N
96e68087-c002-4eb0-aa20-cfdd6443f7b4	2022-03-30 07:08:53.086953+00	2022-03-30 07:08:53.086953+00	Tomdi tumani	1712244	111	\N	c7dcf9ef-5b8a-4a58-b440-38503c26be25	\N
8d900b7b-2d8b-404f-9db7-299eba13fb7b	2022-03-30 07:08:53.08795+00	2022-03-30 07:08:53.08795+00	Uchquduq tumani	1712248	112	\N	c7dcf9ef-5b8a-4a58-b440-38503c26be25	\N
8344c29d-e486-432f-a8fa-af540d2fdb55	2022-03-30 07:08:53.08795+00	2022-03-30 07:08:53.08795+00	Xatirchi tumani	1712251	105	\N	c7dcf9ef-5b8a-4a58-b440-38503c26be25	\N
952b6a37-40ff-46ce-bea3-50baf7301f5a	2022-03-30 07:08:53.088947+00	2022-03-30 07:08:53.088947+00	Mingbuloq tumani	1714204	94	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
42d26993-cfb1-4d55-81f6-e2757f03f2f1	2022-03-30 07:08:53.088947+00	2022-03-30 07:08:53.088947+00	Kosonsoy tumani	1714207	93	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
ee651a56-b4df-4494-b76f-1eed0bc6fd04	2022-03-30 07:08:53.088947+00	2022-03-30 07:08:53.088947+00	Namangan tumani	1714212	96	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
73f16a87-7472-4a3b-91d3-c7c0f2f3e9b4	2022-03-30 07:08:53.089945+00	2022-03-30 07:08:53.089945+00	Norin tumani	1714216	97	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
6f78be4a-d9d9-4f49-bc88-8f9859d215fc	2022-03-30 07:08:53.089945+00	2022-03-30 07:08:53.089945+00	Pop tumani	1714219	98	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
ab0941fa-c7b8-49ce-a712-73c5bb16674f	2022-03-30 07:08:53.090942+00	2022-03-30 07:08:53.090942+00	To'raqo'rg'on tumani	1714224	99	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
90b8ddf7-f348-444a-9595-e43e1e2d824b	2022-03-30 07:08:53.090942+00	2022-03-30 07:08:53.090942+00	Uychi tumani	1714229	101	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
aefcc34f-abab-4bf7-9c9f-de2e56c1eddb	2022-03-30 07:08:53.091939+00	2022-03-30 07:08:53.091939+00	Uchqo'rg'on tumani	1714234	100	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
ee1ce271-aada-4ee2-bbf7-b0bd2db433ed	2022-03-30 07:08:53.092938+00	2022-03-30 07:08:53.092938+00	Chortoq tumani	1714236	91	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
82d9f3ba-b1f2-459d-8cbe-e3ea70ecd8b6	2022-03-30 07:08:53.093935+00	2022-03-30 07:08:53.093935+00	Chust tumani	1714237	92	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
07dcaf2a-9efd-490a-a085-7f1139e2a3ad	2022-03-30 07:08:53.093935+00	2022-03-30 07:08:53.093935+00	Yangiqo'rg'on tumani	1714242	102	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
4dc66db1-3256-4805-9c80-43faeb5bd35a	2022-03-30 07:08:53.095937+00	2022-03-30 07:08:53.095937+00	Oqdaryo tumani	1718203	138	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
7ad9a71f-924f-4454-bd1d-9f7fdf90148c	2022-03-30 07:08:53.095937+00	2022-03-30 07:08:53.095937+00	Bulung'ur tumani	1718206	131	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
4ea1c5f9-5ce7-4f8c-873e-84b03a88fd1d	2022-03-30 07:08:53.096927+00	2022-03-30 07:08:53.096927+00	Jomboy tumani	1718209	133	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
027d5668-e351-4081-98a1-bd565ed4dfe6	2022-03-30 07:08:53.096927+00	2022-03-30 07:08:53.096927+00	Ishtixon tumani	1718212	132	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
1dabdd90-de3e-49ea-9c21-6e8cfd6295eb	2022-03-30 07:08:53.097954+00	2022-03-30 07:08:53.097954+00	Kattaqo'rg'on tumani	1718215	135	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
15b8b5a5-7555-4f62-ae92-0fddcf37704d	2022-03-30 07:08:53.097954+00	2022-03-30 07:08:53.097954+00	'shrabot tumani	1718216	142	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
9971637b-add2-41fa-b0e5-c1bbdc89ce83	2022-03-30 07:08:53.098949+00	2022-03-30 07:08:53.098949+00	pay tumani	1718218	136	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
3848a889-dd23-44ea-bfda-c92560c710a1	2022-03-30 07:08:53.098949+00	2022-03-30 07:08:53.098949+00	Payariq tumani	1718224	141	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
2b22886d-951b-42a7-9077-143142d97b80	2022-03-30 07:08:53.099925+00	2022-03-30 07:08:53.099925+00	Pastdarg'om tumani	1718227	140	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
760a2270-a22f-4882-8b88-46e7403df2f2	2022-03-30 07:08:53.099925+00	2022-03-30 07:08:53.099925+00	Paxtachi tumani	1718230	139	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
06899166-8cd7-4edf-bdab-3e412c702c3f	2022-03-30 07:08:53.100948+00	2022-03-30 07:08:53.100948+00	Samarqand tumani	1718233	144	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
71961a83-ea97-4c85-a464-8e83b6e3aad7	2022-03-30 07:08:53.100948+00	2022-03-30 07:08:53.100948+00	Nurobod tumani	1718235	137	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
6b14735b-88e5-4ca9-91ac-dc2675d509e4	2022-03-30 07:08:53.101943+00	2022-03-30 07:08:53.101943+00	Urgut tumani	1718236	146	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
c38f67ca-28bf-4eb5-bca4-ffd1ca18ddd3	2022-03-30 07:08:53.101943+00	2022-03-30 07:08:53.101943+00	Tayloq tumani	1718238	145	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
9b08e8e7-f541-4121-ad30-41a18f983f2c	2022-03-30 07:08:53.102943+00	2022-03-30 07:08:53.102943+00	Oltinsoy tumani	1722201	151	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
7457db35-e5c4-4e47-b3af-38cdaf6e4de2	2022-03-30 07:08:53.102943+00	2022-03-30 07:08:53.102943+00	Angor tumani	1722202	160	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
04d55369-470c-4e1a-9105-2e3d2a9d35e7	2022-03-30 07:08:53.103908+00	2022-03-30 07:08:53.103908+00	Boysun tumani	1722204	147	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
66391151-870e-456c-99df-c3d0cb705b88	2022-03-30 07:08:53.103908+00	2022-03-30 07:08:53.103908+00	Muzrabot tumani	1722207	150	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
09343ef8-d923-4913-be08-d34a5afecbc1	2022-03-30 07:08:53.104905+00	2022-03-30 07:08:53.104905+00	Denov tumani	1722210	148	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
5f05c5c7-6000-4501-ba83-4f0f4cc50efd	2022-03-30 07:08:53.104905+00	2022-03-30 07:08:53.104905+00	Jarqo'rg'on tumani	1722212	149	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
1554f098-589b-4a95-a0aa-21c7a0bf77f0	2022-03-30 07:08:53.105902+00	2022-03-30 07:08:53.105902+00	Qumqo'rg'on tumani	1722214	153	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
0f5c2202-ea54-4165-a255-980b89fc30d9	2022-03-30 07:08:53.105902+00	2022-03-30 07:08:53.105902+00	Qiziriq tumani	1722215	152	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
c65598c5-877c-46f1-a084-b6e5219b489c	2022-03-30 07:08:53.1069+00	2022-03-30 07:08:53.1069+00	Sariosiyo tumani	1722217	154	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
b0b05aff-22a3-4a4f-9f38-e51d5df8004d	2022-03-30 07:08:53.1069+00	2022-03-30 07:08:53.1069+00	Termiz tumani	1722220	158	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
d1b32afe-f469-4fa2-8153-850a877900a2	2022-03-30 07:08:53.107897+00	2022-03-30 07:08:53.107897+00	Uzun tumani	1722221	159	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
e040f16f-9692-48c6-9a8a-0c7cb4e4a587	2022-03-30 07:08:53.107897+00	2022-03-30 07:08:53.107897+00	Sherobod tumani	1722223	155	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
a1f8f1cd-2d0a-4ccf-9eff-9e7634969da2	2022-03-30 07:08:53.108907+00	2022-03-30 07:08:53.108907+00	Sho'rchi tumani	1722226	156	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
35fd5c37-6315-4aa8-980d-b55ff694ca9d	2022-03-30 07:08:53.109914+00	2022-03-30 07:08:53.109914+00	Oqoltin tumani	1724206	167	\N	e6b1d31b-2614-4b8a-b073-5e0734b6b63e	\N
81832afd-7179-4645-8f69-a53f7306b5b5	2022-03-30 07:08:53.109914+00	2022-03-30 07:08:53.109914+00	Boyovut tumani	1724212	162	\N	e6b1d31b-2614-4b8a-b073-5e0734b6b63e	\N
793e3c35-7016-4ccf-b2aa-809e71eb82fa	2022-03-30 07:08:53.110889+00	2022-03-30 07:08:53.110889+00	Sayxunobod tumani	1724216	169	\N	e6b1d31b-2614-4b8a-b073-5e0734b6b63e	\N
7fe8234a-5690-4e81-8d92-f647432001ab	2022-03-30 07:08:53.110889+00	2022-03-30 07:08:53.110889+00	Guliston tumani	1724220	164	\N	e6b1d31b-2614-4b8a-b073-5e0734b6b63e	\N
31008a61-45f6-41ee-a10d-f1f9430f5d28	2022-03-30 07:08:53.111887+00	2022-03-30 07:08:53.111887+00	Sardoba tumani	1724226	168	\N	e6b1d31b-2614-4b8a-b073-5e0734b6b63e	\N
eb68733e-0e3a-4b88-934b-599b3833d13c	2022-03-30 07:08:53.111887+00	2022-03-30 07:08:53.111887+00	Mirzaobod tumani	1724228	166	\N	e6b1d31b-2614-4b8a-b073-5e0734b6b63e	\N
ab03ec95-0d97-4ed4-ab55-88d48af80bac	2022-03-30 07:08:53.112908+00	2022-03-30 07:08:53.112908+00	Sirdaryo tumani	1724231	171	\N	e6b1d31b-2614-4b8a-b073-5e0734b6b63e	\N
2591a727-8965-45c1-9627-471f81839ab0	2022-03-30 07:08:53.112908+00	2022-03-30 07:08:53.112908+00	Xovos tumani	1724235	165	\N	e6b1d31b-2614-4b8a-b073-5e0734b6b63e	\N
17817232-b631-43f3-8902-e298acdbaf62	2022-03-30 07:08:53.113905+00	2022-03-30 07:08:53.113905+00	Oqqo'rg'on tumani	1727206	195	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
11ad5b84-8465-45e0-bfae-348a640520fa	2022-03-30 07:08:53.113905+00	2022-03-30 07:08:53.113905+00	Ohangaron tumani	1727212	193	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
393a29cc-e65b-4874-b5e1-39c41c57ad67	2022-03-30 07:08:53.114903+00	2022-03-30 07:08:53.114903+00	Bekobod tumani	1727220	186	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
b8fc5d21-34c5-4619-97ae-e88a649acdfb	2022-03-30 07:08:53.114903+00	2022-03-30 07:08:53.114903+00	Bo'stonliq tumani	1727224	188	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
27597854-0c0b-4059-b8af-c396e03de607	2022-03-30 07:08:53.115876+00	2022-03-30 07:08:53.115876+00	Bo'ka tumani	1727228	187	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
cd51cba1-77ea-44c7-9c92-68a81070988f	2022-03-30 07:08:53.115876+00	2022-03-30 07:08:53.115876+00	Qiyichirchiq tumani	1727233	200	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
7127a6de-3a67-41e6-a78b-33b2e30f3786	2022-03-30 07:08:53.116897+00	2022-03-30 07:08:53.116897+00	Zangiota tumani	1727237	204	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
e1000770-69fc-4490-b597-eb94f709cf31	2022-03-30 07:08:53.116897+00	2022-03-30 07:08:53.116897+00	Yuqorichirchiq tumani	1727239	203	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
d711d812-fba3-4af4-976a-f5bf8ef9e237	2022-03-30 07:08:53.117871+00	2022-03-30 07:08:53.117871+00	Qibray tumani	1727248	199	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
50984f89-3d0d-4bb6-bf7b-7e2bea2ff359	2022-03-30 07:08:53.117871+00	2022-03-30 07:08:53.117871+00	Parkent tumani	1727249	197	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
8ceea632-ab56-4963-a688-83f9d0ef6ff0	2022-03-30 07:08:53.118892+00	2022-03-30 07:08:53.118892+00	Pskent tumani	1727250	198	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
4f4ad408-1770-4fa0-8a4d-92b7b5367e70	2022-03-30 07:08:53.118892+00	2022-03-30 07:08:53.118892+00	O'rtachirchiq tumani	1727253	196	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
620e35b0-96a8-4ee5-98db-a2d596c50449	2022-03-30 07:08:53.119891+00	2022-03-30 07:08:53.119891+00	Chinoz tumani	1727256	189	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
5393cdb2-0780-4ccc-bd70-c88c9ac30fc7	2022-03-30 07:08:53.119891+00	2022-03-30 07:08:53.119891+00	yo'l tumani	1727259	202	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
8af309e4-6ee2-41c5-aa89-3d60a8695ae8	2022-03-30 07:08:53.120881+00	2022-03-30 07:08:53.120881+00	Toshkent tumani	1727265	206	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
e13b3204-f7f6-4ba9-b3e9-c7b05f50f446	2022-03-30 07:08:53.120881+00	2022-03-30 07:08:53.120881+00	Oltiariq tumani	1730203	39	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
7d473518-516a-42fb-a776-3de06b1bbef6	2022-03-30 07:08:53.12186+00	2022-03-30 07:08:53.12186+00	Qo'shtepa tumani	1730206	40	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
efc392e2-10bd-4e32-8d50-8a97055aa7a4	2022-03-30 07:08:53.12186+00	2022-03-30 07:08:53.12186+00	Bog'dod tumani	1730209	31	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
1098d309-b81a-4391-9e9b-0b2b836eceaa	2022-03-30 07:08:53.122857+00	2022-03-30 07:08:53.122857+00	Buvayda tumani	1730212	32	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
a2aba29c-659b-4c6e-b1a9-c8bbc8490a76	2022-03-30 07:08:53.122857+00	2022-03-30 07:08:53.122857+00	Beshariq tumani	1730215	30	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
bc59bad3-20b7-465d-8073-29c3d50a112f	2022-03-30 07:08:53.123855+00	2022-03-30 07:08:53.123855+00	Quva tumani	1730218	41	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
8bf5ef07-ff19-4b0b-8bb3-87d61b6c9d96	2022-03-30 07:08:53.123855+00	2022-03-30 07:08:53.123855+00	Uchko'prik tumani	1730221	46	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
5633c441-9b73-46ba-a20e-76b9d2ed62a1	2022-03-30 07:08:53.124851+00	2022-03-30 07:08:53.124851+00	Rishton tumani	1730224	43	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
74df8958-81e6-407d-ac04-7ba8ab9343ab	2022-03-30 07:08:53.124851+00	2022-03-30 07:08:53.124851+00	So'x tumani	1730226	44	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
28db9f6d-b080-4af1-8549-a63e3dc2282c	2022-03-30 07:08:53.125874+00	2022-03-30 07:08:53.125874+00	Toshloq tumani	1730227	45	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
11fd0b70-5d1a-48d9-8cb8-5fb5b0c3997c	2022-03-30 07:08:53.126873+00	2022-03-30 07:08:53.126873+00	O'zbekiston tumani	1730230	47	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
e5abd60a-2206-4074-814c-d630121ac0dc	2022-03-30 07:08:53.127844+00	2022-03-30 07:08:53.127844+00	Farg' tumani	1730233	35	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
613592a5-cc49-4dd3-ae96-476d30224c5d	2022-03-30 07:08:53.127844+00	2022-03-30 07:08:53.127844+00	Dang'ara tumani	1730236	33	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
3da75039-68b9-40d9-a805-a1b62d796b40	2022-03-30 07:08:53.128868+00	2022-03-30 07:08:53.128868+00	Furqat tumani	1730238	36	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
1d06f4b7-0c2f-4a04-a037-4ba0945880ca	2022-03-30 07:08:53.128868+00	2022-03-30 07:08:53.128868+00	Yozyovon tumani	1730242	48	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
791e0d97-fc76-4c66-8991-4fb3db9c828f	2022-03-30 07:08:53.129862+00	2022-03-30 07:08:53.129862+00	Bog'ot tumani	1733204	78	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
f4809c41-57c0-4e8e-aff6-a5c4c4a4d0b3	2022-03-30 07:08:53.129862+00	2022-03-30 07:08:53.129862+00	Gurlan tumani	1733208	79	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
99c66032-250d-4f56-9c78-36bb1c63e7cc	2022-03-30 07:08:53.130859+00	2022-03-30 07:08:53.130859+00	Qo'shko'pir tumani	1733212	84	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
765fb9d2-4a7c-4052-b428-933bf45959b1	2022-03-30 07:08:53.130859+00	2022-03-30 07:08:53.130859+00	Urganch tumani	1733217	88	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
ca6da729-3070-4f6c-8122-432426bf9db8	2022-03-30 07:08:53.131833+00	2022-03-30 07:08:53.131833+00	Xazorasp tumani	1733220	80	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
dab2d606-ab07-47e2-8c6b-b50fd49146df	2022-03-30 07:08:53.131833+00	2022-03-30 07:08:53.131833+00	Xonqa tumani	1733223	83	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
7c277e24-395b-4094-b725-61456cfd71d0	2022-03-30 07:08:53.13283+00	2022-03-30 07:08:53.13283+00	Xiva tumani	1733226	82	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
86356aa8-a74d-4edf-a996-daf9372883b9	2022-03-30 07:08:53.13283+00	2022-03-30 07:08:53.13283+00	Shovot tumani	1733230	85	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
0becf60d-e893-4af9-82da-d080700deef8	2022-03-30 07:08:53.133827+00	2022-03-30 07:08:53.133827+00	Yangiariq tumani	1733233	89	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
5cb8ffcd-65c2-432a-8032-a47c1d178f13	2022-03-30 07:08:53.133827+00	2022-03-30 07:08:53.133827+00	Yangibozor tumani	1733236	90	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
95f9fb1d-f3e2-4230-aedd-990f2a10dbc6	2022-03-30 07:08:53.134825+00	2022-03-30 07:08:53.134825+00	Amudaryo tumani	1735204	128	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
1f367f29-f2c4-432e-92b5-1d59db149c4c	2022-03-30 07:08:53.134825+00	2022-03-30 07:08:53.134825+00	Beruniy tumani	1735207	114	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
6a939644-be17-4de1-b2d1-9e590eb358b6	2022-03-30 07:08:53.135822+00	2022-03-30 07:08:53.135822+00	Qorao'zak tumani	1735211	122	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
d5b01e6f-3a37-463b-b7e1-04a6f69f1a9d	2022-03-30 07:08:53.135822+00	2022-03-30 07:08:53.135822+00	Kegeyli tumani	1735212	117	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
1f88afc3-21ec-4201-9ddf-e7444e5b7ba5	2022-03-30 07:08:53.135822+00	2022-03-30 07:08:53.135822+00	Qo'ng'irot tumani	1735215	123	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
307fb1c6-6030-45b7-a8b6-2678959c9204	2022-03-30 07:08:53.13682+00	2022-03-30 07:08:53.13682+00	Qanlikoʻl tumani	1735218	124	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
69969ecf-95b7-44c2-8ec4-9df6d3d79803	2022-03-30 07:08:53.13682+00	2022-03-30 07:08:53.13682+00	Mo'ynoq tumani	1735222	119	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
23a88418-1cdf-48ea-9863-684a1279ca9f	2022-03-30 07:08:53.137817+00	2022-03-30 07:08:53.137817+00	Nukus tumani	1735225	121	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
5ed24b33-301c-4d80-a747-f5cb9b197006	2022-03-30 07:08:53.137817+00	2022-03-30 07:08:53.137817+00	Taxiatosh tumani	1735228	130	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
2c791704-cbcf-4bf2-817a-a23cde80daf8	2022-03-30 07:08:53.138814+00	2022-03-30 07:08:53.138814+00	Taxtako'pir tumani	1735230	126	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
5dfeaa31-f676-410a-9f39-461b22913858	2022-03-30 07:08:53.138814+00	2022-03-30 07:08:53.138814+00	To'rtko'l tumani	1735233	127	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
19676be0-9806-4324-92da-33673b7d0164	2022-03-30 07:08:53.139812+00	2022-03-30 07:08:53.139812+00	Xo'jayli tumani	1735236	118	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
77810c7d-6321-442f-877a-f35923394478	2022-03-30 07:08:53.139812+00	2022-03-30 07:08:53.139812+00	Chimboy tumani	1735240	115	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
f25b2317-ae14-4843-9986-9144cd67b93d	2022-03-30 07:08:53.140809+00	2022-03-30 07:08:53.140809+00	Shumanay tumani	1735243	125	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
17850b0f-d2c5-49e5-b52f-9ad396daa4a7	2022-03-30 07:08:53.140809+00	2022-03-30 07:08:53.140809+00	Ellikkala tumani	1735250	116	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
fd19e2be-afa1-431a-8097-4f8f903f9144	2022-03-30 07:08:53.141806+00	2022-03-30 07:08:53.141806+00	Uchtepa tumani	1726262	179	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
03437285-84ea-4ef8-9cd4-353178a0720b	2022-03-30 07:08:53.141806+00	2022-03-30 07:08:53.141806+00	Bektemir tumani	1726264	173	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
0d837f85-688b-4fb2-bc7d-3cb240ae140e	2022-03-30 07:08:53.142805+00	2022-03-30 07:08:53.142805+00	Yunusobod tumani	1726266	183	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
2146e645-4cdd-40d6-afac-543f07265b9d	2022-03-30 07:08:53.143802+00	2022-03-30 07:08:53.143802+00	Mirzo Ulug'bek tumani	1726269	184	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
c74e957a-1ee8-478e-93a6-09caf98cb5a3	2022-03-30 07:08:53.143802+00	2022-03-30 07:08:53.143802+00	Mirobod tumani	1726273	175	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
9816fe54-c737-4a80-b95c-200c5f2c09d6	2022-03-30 07:08:53.144799+00	2022-03-30 07:08:53.144799+00	Shayxontoxur tumani	1726277	178	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
a6650d8c-547c-4041-92e6-5ae4455d8f7d	2022-03-30 07:08:53.144799+00	2022-03-30 07:08:53.144799+00	Olmazor tumani	1726280	176	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
caa81d01-9940-483e-92d7-efaa50753ae8	2022-03-30 07:08:53.145796+00	2022-03-30 07:08:53.145796+00	Sirg'ali tumani	1726283	177	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
2fe8c5d9-bfcf-44ef-a56e-604bb4963a7b	2022-03-30 07:08:53.146793+00	2022-03-30 07:08:53.146793+00	Yakkasaroy tumani	1726287	180	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
cff2808c-f2b0-45e7-983b-9dbde2737c56	2022-03-30 07:08:53.146793+00	2022-03-30 07:08:53.146793+00	Yashnobod tumani	1726290	182	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
145d3e1d-4c4a-4501-8e2c-44376887e7c9	2022-03-30 07:08:53.146793+00	2022-03-30 07:08:53.146793+00	Chilonzor tumani	1726294	174	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
a45e9209-7692-4a5c-a5f6-7cd542574a68	2022-03-30 07:08:53.147791+00	2022-03-30 07:08:53.147791+00	Buxoro shahri	1706401	17	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
3bdd1562-54dd-4a7e-a8ca-e48427dce37f	2022-03-30 07:08:53.147791+00	2022-03-30 07:08:53.148788+00	Jizzax shahri	1708401	54	\N	737c72e9-80a0-44d3-94f7-64d07a2e519f	\N
55a07368-8e6a-4e27-9ed0-9cd2bd916973	2022-03-30 07:08:53.148788+00	2022-03-30 07:08:53.148788+00	Qarshi shahri	1710401	73	\N	c18fea69-5fc0-48eb-98d1-b795a8874987	\N
558a296d-49ee-4444-ba33-8d85472e2bc0	2022-03-30 07:08:53.148788+00	2022-03-30 07:08:53.148788+00	Navoiy shahri	1712401	108	\N	c7dcf9ef-5b8a-4a58-b440-38503c26be25	\N
9c4853d9-8c0c-4b5a-836e-6a635a1f8716	2022-03-30 07:08:53.149785+00	2022-03-30 07:08:53.149785+00	Namangan shahri	1714401	95	\N	6eb6232a-9b2b-4255-9c5a-74faa0e68595	\N
d0356a14-436d-453c-9eb3-d87b397fe2a2	2022-03-30 07:08:53.149785+00	2022-03-30 07:08:53.149785+00	Samarqand shahri	1718401	143	\N	597f143c-d890-4c9b-bbce-972c4a9e3f64	\N
fc3ae53b-9038-45cb-a986-3859ef595b2c	2022-03-30 07:08:53.150812+00	2022-03-30 07:08:53.150812+00	Termiz shahri	1722401	157	\N	7830817e-a9cc-4422-8d14-2ff8d3a7c383	\N
a053ab5e-bbb1-46d4-911a-6fc3af1afecc	2022-03-30 07:08:53.150812+00	2022-03-30 07:08:53.150812+00	Guliston shahri	1724401	163	\N	e6b1d31b-2614-4b8a-b073-5e0734b6b63e	\N
930802cb-0650-47a8-adf2-50483cec36c1	2022-03-30 07:08:53.151812+00	2022-03-30 07:08:53.151812+00	Olmaliq shahri	1727404	194	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
61648524-3981-4148-9957-119e9c954cf4	2022-03-30 07:08:53.151812+00	2022-03-30 07:08:53.151812+00	Angren shahri	1727407	205	\N	39becd44-a06e-4a3a-b0e3-fe07ba781171	\N
170974b5-0d26-4c37-b25c-2620c6fa9d0a	2022-03-30 07:08:53.151812+00	2022-03-30 07:08:53.151812+00	Farg'ona shahri	1730401	34	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
373bbad2-9698-47a8-887d-98e70e7ba35f	2022-03-30 07:08:53.152836+00	2022-03-30 07:08:53.152836+00	Qo'qon shahri	1730405	37	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
cde637a0-0f44-4e94-9b12-ac8e968b18bf	2022-03-30 07:08:53.153807+00	2022-03-30 07:08:53.153807+00	Urganch shahri	1733401	87	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
42ee2fb0-9016-4085-af69-64a7396a34c5	2022-03-30 07:08:53.153807+00	2022-03-30 07:08:53.153807+00	Xiva shahri	1733406	81	\N	83ecce49-d9cb-4115-ae89-79a69ce26462	\N
5d0dd511-713e-45e0-9e7a-b209d596dcc4	2022-03-30 07:08:53.154804+00	2022-03-30 07:08:53.154804+00	Nukus shahri	1735401	120	\N	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	\N
c345a33d-7c0e-4e40-a991-70dfb78ea238	2022-03-30 07:08:53.154804+00	2022-03-30 07:08:53.154804+00	Kogon shahri	1706403	21	\N	8b559524-d92a-4ba9-a7a0-9190bd7083d0	\N
bf6e7186-97d4-47d4-bd15-20925b1d9525	2022-03-30 07:08:53.155801+00	2022-03-30 07:08:53.155801+00	Marg'ilon shahri	1730412	38	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
05ee2d9d-707d-4232-94a5-2699ef2f8e92	2022-03-30 07:08:53.155801+00	2022-03-30 07:08:53.155801+00	Quvasoy shahri	1730408	42	\N	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	\N
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2022-03-30 07:10:17.299366+00	b2abc5e5-4d32-4aa9-b9ab-ec7f4be43e73	Toshkent markazi	1	[{"added": {}}]	8	1
2	2022-03-30 07:10:30.712354+00	519d616f-3b52-420f-b74a-d0d7f95507e0	Ko'cha	1	[{"added": {}}]	10	1
3	2022-03-30 07:10:34.169735+00	e72a344e-67df-457c-a022-94807e6d8b19	Bozor	1	[{"added": {}}]	10	1
4	2022-03-30 07:10:43.424438+00	8c66cf79-6720-49fd-97c0-ecc87642d645	Yer to'la	1	[{"added": {}}]	10	1
5	2022-03-30 07:11:05.207795+00	7d7ae6b4-f189-451e-9f99-2d348b86c100	Sil kasalliklar dispanser	1	[{"added": {}}]	18	1
6	2022-03-30 07:11:09.536308+00	b85257a4-3ebd-4cdb-bf88-e12f2ce50796	Teri-tanosil kasalliklar dispanser	1	[{"added": {}}]	18	1
7	2022-03-30 07:21:22.946655+00	d658b9d2-dee9-4e46-868e-8b68b97c298b	Sud ajrimi	1	[{"added": {}}]	11	1
8	2022-03-30 07:21:34.800182+00	df720d82-7498-4eb3-98a2-adabaf977b0e	IIB qarori	1	[{"added": {}}]	11	1
9	2022-03-30 07:21:52.510842+00	01954048-8e6b-4229-bef9-154cb89f6662	Shartli	1	[{"added": {}}]	13	1
10	2022-03-30 07:21:56.80616+00	6618ddc6-a43b-4639-bb01-deb76551d7e9	Sinov	1	[{"added": {}}]	13	1
11	2022-03-30 07:23:47.453554+00	1	Navbatchi	1	[{"added": {}}]	3	1
12	2022-03-30 07:23:57.747543+00	2	doniyor  	2	[{"changed": {"fields": ["Superuser status", "Groups", "Birth date", "Markaz"]}}]	12	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	info	schooltype
7	info	region
8	info	markaz
9	info	district
10	info	determinedlocation
11	info	arrivedreason
12	accounts	customuser
13	juvenile	convictedlist
14	juvenile	juvenile
15	juvenile	juvenileparent
16	juvenile	relationship
17	juvenile	prophylacticinspector
18	juvenile	medicallist
19	juvenile	juvenilemedicallist
20	juvenile	juvenileconvictedlist
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-03-30 06:18:35.215064+00
2	contenttypes	0002_remove_content_type_name	2022-03-30 06:18:35.226036+00
3	auth	0001_initial	2022-03-30 06:18:35.279891+00
4	auth	0002_alter_permission_name_max_length	2022-03-30 06:18:35.283879+00
5	auth	0003_alter_user_email_max_length	2022-03-30 06:18:35.287869+00
6	auth	0004_alter_user_username_opts	2022-03-30 06:18:35.292856+00
7	auth	0005_alter_user_last_login_null	2022-03-30 06:18:35.296844+00
8	auth	0006_require_contenttypes_0002	2022-03-30 06:18:35.297842+00
9	auth	0007_alter_validators_add_error_messages	2022-03-30 06:18:35.301854+00
10	auth	0008_alter_user_username_max_length	2022-03-30 06:18:35.305823+00
11	auth	0009_alter_user_last_name_max_length	2022-03-30 06:18:35.309837+00
12	auth	0010_alter_group_name_max_length	2022-03-30 06:18:35.317816+00
13	auth	0011_update_proxy_permissions	2022-03-30 06:18:35.32178+00
14	auth	0012_alter_user_first_name_max_length	2022-03-30 06:18:35.326764+00
15	auth	0013_group_code	2022-03-30 06:18:35.330754+00
16	accounts	0001_initial	2022-03-30 06:18:35.376633+00
17	info	0001_initial	2022-03-30 06:18:35.488334+00
18	accounts	0002_customuser_markaz	2022-03-30 06:18:35.500301+00
19	admin	0001_initial	2022-03-30 06:18:35.521246+00
20	admin	0002_logentry_remove_auto_add	2022-03-30 06:18:35.533213+00
21	admin	0003_logentry_add_action_flag_choices	2022-03-30 06:18:35.561138+00
22	juvenile	0001_initial	2022-03-30 06:18:35.855397+00
23	juvenile	0002_juvenileparent_pinfl	2022-03-30 06:18:35.868362+00
24	juvenile	0003_alter_juvenile_arrived_date	2022-03-30 06:18:35.884319+00
25	sessions	0001_initial	2022-03-30 06:18:35.896287+00
26	juvenile	0004_auto_20220330_1548	2022-03-30 10:48:54.371747+00
27	juvenile	0005_alter_juvenile_convicted_list	2022-03-30 10:56:36.529065+00
28	juvenile	0006_alter_juvenile_arrived_reason	2022-03-31 04:59:24.803543+00
29	info	0002_delete_arrivedreason	2022-03-31 04:59:24.84044+00
30	juvenile	0007_alter_juvenile_determined_location	2022-03-31 05:08:03.702522+00
31	info	0003_delete_determinedlocation	2022-03-31 05:08:03.716485+00
32	juvenile	0008_auto_20220331_1102	2022-03-31 06:02:27.348614+00
33	juvenile	0009_juvenile_status	2022-03-31 06:08:38.677746+00
34	juvenile	0010_auto_20220405_1200	2022-04-05 07:00:06.014421+00
35	juvenile	0011_auto_20220405_1540	2022-04-05 10:40:33.754804+00
36	info	0004_delete_schooltype	2022-04-07 04:23:45.439638+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
f5dd3dxut3hqc7glyj5lku4ofs3mjf12	.eJxVjDsOwjAQBe_iGln-yMRLSc8ZrN31GgeQI8VJhbg7iZQC2pl5760SrktNa5c5jVldlFWnX0bIT2m7yA9s90nz1JZ5JL0n-rBd36Ysr-vR_h1U7HVbkwRbbCxsAA2yA0-mgPhA3kaMDB6tGwIbEecZwxlgY2Ww5F10kNXnC-6IN9A:1nZSSO:FVvq2l7B84Qsi35AmxLL-gyp79oeCD5JATuyXUbBjEw	2022-04-13 07:09:28.7004+00
\.


--
-- Data for Name: juvenile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.juvenile (id, created_at, updated_at, first_name, last_name, father_name, birth_date, photo, gender, address, school_name, arrived_date, issue_date, destination, marital_status, passport_seria, arrived_reason_file, passport_type, reference_type, pinfl, count_came_back_to_center, school_type, prophylactic_list, distribution_type, level_kinkdship, basis_distribution, type_guardianship, itm_direction, itm_name, rotm_type, basis_sending_file, is_out, address_district_id, arrived_reason, birth_district_id, created_by_id, determined_location, inspector_id, itm_district_id, markaz_id, school_district_id, updated_by_id, convicted_list, have_been_in_itm_reason, have_been_in_rotm_reason, status, health_condition, organization_coach_name, organization_directors_name, organization_psyhologs_name, psyhology_condition, skills_hobbies) FROM stdin;
000718ba-cdff-4d76-8717-e2e471104baa	2022-04-07 07:11:56.44154+00	2022-04-07 07:59:31.999958+00	dasasd	asada	asd	2018-04-06	juveniles/evants_myxwV94.jpg	M	2edsdas	23edsad	2022-04-05 19:00:00+00	\N	\N	1	adsdas	arrived_reason_file/photo_2022-03-31_12-37-25_daRgZTl.jpg	1		wddasdasdasd22	1	2	f	2	\N	1	3	\N	\N	\N	basis_sending_file/lex_TeyThHT.jpeg	f	5393cdb2-0780-4ccc-bd70-c88c9ac30fc7	1	196086dd-5cb3-49e4-8119-ddff23e213f9	2	1	a6debcc4-fd58-44f1-81cb-399ae0e49d99	\N	b2abc5e5-4d32-4aa9-b9ab-ec7f4be43e73	5cb8ffcd-65c2-432a-8032-a47c1d178f13	\N	1	1	1	3	edcsas	\N	\N	\N	adasasd	dasda
2e4f551d-4849-4957-b22f-4063189ee3c6	2022-04-08 05:08:23.764954+00	2022-04-08 05:08:23.770937+00	Umidjon	Odilov	Sultonmurod o'g'li	2004-04-08	juveniles/TFK_0884_bJnhh9n.jpg	M	Chilonzor-12-3a-17	TRT va AKHK	\N	\N	\N	1	AB4197101		1		13123123123123	\N	4	f	\N	\N	\N	\N	\N	\N	\N		f	fd19e2be-afa1-431a-8097-4f8f903f9144	\N	fd19e2be-afa1-431a-8097-4f8f903f9144	2	\N	\N	\N	b2abc5e5-4d32-4aa9-b9ab-ec7f4be43e73	fd19e2be-afa1-431a-8097-4f8f903f9144	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N
2eea2ef1-7155-46d2-8282-3bbb89015b50	2022-04-08 05:02:56.262063+00	2022-04-08 05:36:08.700782+00	Diyor	Xoshimov	Xoshimjonovich	2009-04-01	juveniles/image_XL2r4ss.jpg	M	Qorasu 3 1/72	7	2022-04-06 19:00:00+00	\N	\N	1	AA1000001	arrived_reason_file/image.jpg	2		13131313213131	1	1	t	1	2	3	\N	\N	\N	\N	basis_sending_file/image.jpg	f	2146e645-4cdd-40d6-afac-543f07265b9d	1	2146e645-4cdd-40d6-afac-543f07265b9d	2	1	a4c27086-8e60-43dc-ae94-837cf59c6448	\N	b2abc5e5-4d32-4aa9-b9ab-ec7f4be43e73	2146e645-4cdd-40d6-afac-543f07265b9d	\N	3	1	1	3	yaxshi	\N	\N	\N	\N	\N
\.


--
-- Data for Name: juvenile_medical_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.juvenile_medical_list (id, juvenile_id, medical_list_id) FROM stdin;
7	000718ba-cdff-4d76-8717-e2e471104baa	b85257a4-3ebd-4cdb-bf88-e12f2ce50796
8	2eea2ef1-7155-46d2-8282-3bbb89015b50	b85257a4-3ebd-4cdb-bf88-e12f2ce50796
\.


--
-- Data for Name: markaz; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.markaz (id, created_at, updated_at, name, created_by_id, region_id, updated_by_id) FROM stdin;
b2abc5e5-4d32-4aa9-b9ab-ec7f4be43e73	2022-03-30 07:10:17.298341+00	2022-03-30 07:10:17.298341+00	Toshkent markazi	\N	c19341b2-ddf0-4250-8933-a5a3296998d4	\N
\.


--
-- Data for Name: medical_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.medical_list (id, created_at, updated_at, title, created_by_id, updated_by_id) FROM stdin;
7d7ae6b4-f189-451e-9f99-2d348b86c100	2022-03-30 07:11:05.206798+00	2022-03-30 07:11:05.206798+00	Sil kasalliklar dispanser	\N	\N
b85257a4-3ebd-4cdb-bf88-e12f2ce50796	2022-03-30 07:11:09.535311+00	2022-03-30 07:11:09.535311+00	Teri-tanosil kasalliklar dispanser	\N	\N
\.


--
-- Data for Name: parent_juvenile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.parent_juvenile (id, created_at, updated_at, first_name, last_name, father_name, birth_date, employment, created_by_id, updated_by_id, pinfl) FROM stdin;
15cbeaa7-bcf6-4f4b-b495-027c0a325110	2022-04-07 07:11:56.450517+00	2022-04-07 07:11:56.451514+00	sdsa	dsadsadas	qasdsaas	2004-01-01	edasdasdasd	\N	\N	2edfdfasd22322
64d9e31d-6559-449f-8659-a16f11b71a59	2022-04-08 05:02:56.270035+00	2022-04-08 05:02:56.270035+00	Xoshim	Xoshimjonov	Xoshimovich	2003-01-01	+9989744444444	\N	\N	31313131313131
4623abc8-f343-4d1e-a8dc-b707d06c0bb4	2022-04-08 05:08:23.766949+00	2022-04-08 05:08:23.766949+00	Sultonmurod	Adilov	To'xtamurodovich	1962-09-21	Lorem ipsum dolor sit amet.	\N	\N	13123123123123
\.


--
-- Data for Name: prophylactic_inspector; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.prophylactic_inspector (id, created_at, updated_at, first_name, last_name, father_name, inspector_id, pinfl, inspector_type, created_by_id, updated_by_id) FROM stdin;
e572a50e-b502-443c-8bd1-11ef01aa946a	2022-04-07 07:32:27.895063+00	2022-04-07 07:32:27.895063+00	dasasdsda	dadasdasads	edd2322	\N	wsdadsdasdasdd	2	\N	\N
e196b2a5-a61c-4988-ae96-730b5dd5eb36	2022-04-07 07:39:15.079267+00	2022-04-07 07:39:15.079267+00	dasdas	3wedasdasdasdas	dfasdasd	\N	edfcaszxdsadad	2	\N	\N
a6debcc4-fd58-44f1-81cb-399ae0e49d99	2022-04-07 07:42:38.890321+00	2022-04-07 07:42:38.890321+00	asdjlk	adjasdkjasd	asdlkjasd	\N	62341231231312	2	\N	\N
a4c27086-8e60-43dc-ae94-837cf59c6448	2022-04-08 05:35:11.653459+00	2022-04-08 05:35:11.653459+00	Shaxboz	Alimov	Xalilliloyevich	\N	32302910560300	2	\N	\N
\.


--
-- Data for Name: region; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.region (created_at, updated_at, id, name, soato, mvd_profilactic_region_id, created_by_id, updated_by_id) FROM stdin;
2022-03-30 07:08:37.543304+00	2022-03-30 07:08:37.543304+00	597f143c-d890-4c9b-bbce-972c4a9e3f64	Samarqand viloyati	1718	10	\N	\N
2022-03-30 07:08:37.54829+00	2022-03-30 07:08:37.54829+00	6eb6232a-9b2b-4255-9c5a-74faa0e68595	Namangan viloyati	1714	7	\N	\N
2022-03-30 07:08:37.549287+00	2022-03-30 07:08:37.549287+00	f7ec9963-bca8-4ebb-9b6a-1d2eed3d6ccf	Andijon viloyati	1703	1	\N	\N
2022-03-30 07:08:37.549287+00	2022-03-30 07:08:37.549287+00	8b559524-d92a-4ba9-a7a0-9190bd7083d0	Buxoro viloyati	1706	2	\N	\N
2022-03-30 07:08:37.550284+00	2022-03-30 07:08:37.550284+00	737c72e9-80a0-44d3-94f7-64d07a2e519f	Jizzax viloyati	1708	4	\N	\N
2022-03-30 07:08:37.550284+00	2022-03-30 07:08:37.550284+00	c18fea69-5fc0-48eb-98d1-b795a8874987	Qashqadaryo viloyati	1710	5	\N	\N
2022-03-30 07:08:37.551282+00	2022-03-30 07:08:37.551282+00	c7dcf9ef-5b8a-4a58-b440-38503c26be25	Navoiy viloyati	1712	8	\N	\N
2022-03-30 07:08:37.551282+00	2022-03-30 07:08:37.551282+00	7830817e-a9cc-4422-8d14-2ff8d3a7c383	Surxandaryo viloyati	1722	11	\N	\N
2022-03-30 07:08:37.552279+00	2022-03-30 07:08:37.552279+00	e6b1d31b-2614-4b8a-b073-5e0734b6b63e	Sirdaryo viloyati	1724	12	\N	\N
2022-03-30 07:08:37.552279+00	2022-03-30 07:08:37.552279+00	39becd44-a06e-4a3a-b0e3-fe07ba781171	Toshkent viloyati	1727	14	\N	\N
2022-03-30 07:08:37.553277+00	2022-03-30 07:08:37.553277+00	3b24baf4-0a1d-4ecd-86fd-c3c31488f842	Farg'ona viloyati	1730	3	\N	\N
2022-03-30 07:08:37.553277+00	2022-03-30 07:08:37.553277+00	83ecce49-d9cb-4115-ae89-79a69ce26462	Xorazm viloyati	1733	6	\N	\N
2022-03-30 07:08:37.554274+00	2022-03-30 07:08:37.554274+00	3d1dfe83-e667-4273-ae5e-dc29fd2d8c78	Qoraqalpog'iston Respublikasi	1735	9	\N	\N
2022-03-30 07:08:37.555272+00	2022-03-30 07:08:37.555272+00	c19341b2-ddf0-4250-8933-a5a3296998d4	Toshkent shahri	1726	13	\N	\N
\.


--
-- Data for Name: relationship; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.relationship (id, parent_type, juvenile_id, parent_id) FROM stdin;
10	1	000718ba-cdff-4d76-8717-e2e471104baa	15cbeaa7-bcf6-4f4b-b495-027c0a325110
11	1	2eea2ef1-7155-46d2-8282-3bbb89015b50	64d9e31d-6559-449f-8659-a16f11b71a59
12	1	2e4f551d-4849-4957-b22f-4063189ee3c6	4623abc8-f343-4d1e-a8dc-b707d06c0bb4
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, password, last_login, is_superuser, email, login, username, first_name, last_name, father_name, photo, birth_date, is_staff, is_active, markaz_id) FROM stdin;
1	pbkdf2_sha256$260000$hpT5HiPhJJ0LLhn6ii53yX$HKX9bf3nr0ooypBR8dSO02X5idhnOHvnFnlJ0wLQf08=	2022-03-30 07:09:28.699364+00	t	superuser@gmail.com	superuser	superuser	superuser				\N	t	t	\N
2	pbkdf2_sha256$260000$h65JiLxyiyNBabWvL2FIYw$mnfthy/g7wu+vlISFNQOu41imlZGLF5XFPzqda5Ucrg=	\N	f	doniyor@gmail.com	doniyor_123	doniyor	doniyor				2022-03-30	t	t	b2abc5e5-4d32-4aa9-b9ab-ec7f4be43e73
\.


--
-- Data for Name: user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_groups (id, customuser_id, group_id) FROM stdin;
1	2	1
\.


--
-- Data for Name: user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_user_permissions (id, customuser_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 80, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 80, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 12, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 20, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 36, true);


--
-- Name: juvenile_medical_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.juvenile_medical_list_id_seq', 8, true);


--
-- Name: relationship_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.relationship_id_seq', 12, true);


--
-- Name: user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_groups_id_seq', 1, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 2, true);


--
-- Name: user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_user_permissions_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: district district_mvd_profilactic_district_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.district
    ADD CONSTRAINT district_mvd_profilactic_district_id_key UNIQUE (mvd_profilactic_district_id);


--
-- Name: district district_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.district
    ADD CONSTRAINT district_name_key UNIQUE (name);


--
-- Name: district district_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.district
    ADD CONSTRAINT district_pkey PRIMARY KEY (id);


--
-- Name: district district_soato_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.district
    ADD CONSTRAINT district_soato_key UNIQUE (soato);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: juvenile_medical_list juvenile_medical_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile_medical_list
    ADD CONSTRAINT juvenile_medical_list_pkey PRIMARY KEY (id);


--
-- Name: juvenile juvenile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile
    ADD CONSTRAINT juvenile_pkey PRIMARY KEY (id);


--
-- Name: markaz markaz_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.markaz
    ADD CONSTRAINT markaz_name_key UNIQUE (name);


--
-- Name: markaz markaz_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.markaz
    ADD CONSTRAINT markaz_pkey PRIMARY KEY (id);


--
-- Name: medical_list medical_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_list
    ADD CONSTRAINT medical_list_pkey PRIMARY KEY (id);


--
-- Name: parent_juvenile parent_juvenile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parent_juvenile
    ADD CONSTRAINT parent_juvenile_pkey PRIMARY KEY (id);


--
-- Name: prophylactic_inspector prophylactic_inspector_inspector_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prophylactic_inspector
    ADD CONSTRAINT prophylactic_inspector_inspector_id_key UNIQUE (inspector_id);


--
-- Name: prophylactic_inspector prophylactic_inspector_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prophylactic_inspector
    ADD CONSTRAINT prophylactic_inspector_pkey PRIMARY KEY (id);


--
-- Name: region region_mvd_profilactic_region_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.region
    ADD CONSTRAINT region_mvd_profilactic_region_id_key UNIQUE (mvd_profilactic_region_id);


--
-- Name: region region_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.region
    ADD CONSTRAINT region_name_key UNIQUE (name);


--
-- Name: region region_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.region
    ADD CONSTRAINT region_pkey PRIMARY KEY (id);


--
-- Name: region region_soato_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.region
    ADD CONSTRAINT region_soato_key UNIQUE (soato);


--
-- Name: relationship relationship_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.relationship
    ADD CONSTRAINT relationship_pkey PRIMARY KEY (id);


--
-- Name: user user_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user_groups user_groups_customuser_id_group_id_69b568ae_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_groups
    ADD CONSTRAINT user_groups_customuser_id_group_id_69b568ae_uniq UNIQUE (customuser_id, group_id);


--
-- Name: user_groups user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_groups
    ADD CONSTRAINT user_groups_pkey PRIMARY KEY (id);


--
-- Name: user user_login_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_login_key UNIQUE (login);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user_user_permissions user_user_permissions_customuser_id_permission_id_2f47aad7_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_permissions
    ADD CONSTRAINT user_user_permissions_customuser_id_permission_id_2f47aad7_uniq UNIQUE (customuser_id, permission_id);


--
-- Name: user_user_permissions user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_permissions
    ADD CONSTRAINT user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: user user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: district_created_by_id_8bddb121; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX district_created_by_id_8bddb121 ON public.district USING btree (created_by_id);


--
-- Name: district_name_839f005c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX district_name_839f005c_like ON public.district USING btree (name varchar_pattern_ops);


--
-- Name: district_region_id_id_ac67679a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX district_region_id_id_ac67679a ON public.district USING btree (region_id_id);


--
-- Name: district_soato_a6e9a131_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX district_soato_a6e9a131_like ON public.district USING btree (soato varchar_pattern_ops);


--
-- Name: district_updated_by_id_84a22115; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX district_updated_by_id_84a22115 ON public.district USING btree (updated_by_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: juvenile_address_district_id_120b5633; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX juvenile_address_district_id_120b5633 ON public.juvenile USING btree (address_district_id);


--
-- Name: juvenile_birth_district_id_ab58e31d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX juvenile_birth_district_id_ab58e31d ON public.juvenile USING btree (birth_district_id);


--
-- Name: juvenile_created_by_id_3e2e60f7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX juvenile_created_by_id_3e2e60f7 ON public.juvenile USING btree (created_by_id);


--
-- Name: juvenile_inspector_id_c7d57a95; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX juvenile_inspector_id_c7d57a95 ON public.juvenile USING btree (inspector_id);


--
-- Name: juvenile_itm_district_id_c874f528; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX juvenile_itm_district_id_c874f528 ON public.juvenile USING btree (itm_district_id);


--
-- Name: juvenile_markaz_id_aee5e3e7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX juvenile_markaz_id_aee5e3e7 ON public.juvenile USING btree (markaz_id);


--
-- Name: juvenile_medical_list_juvenile_id_cfc4002d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX juvenile_medical_list_juvenile_id_cfc4002d ON public.juvenile_medical_list USING btree (juvenile_id);


--
-- Name: juvenile_medical_list_medical_list_id_1b726390; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX juvenile_medical_list_medical_list_id_1b726390 ON public.juvenile_medical_list USING btree (medical_list_id);


--
-- Name: juvenile_school_district_id_d466279b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX juvenile_school_district_id_d466279b ON public.juvenile USING btree (school_district_id);


--
-- Name: juvenile_updated_by_id_cd84b4da; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX juvenile_updated_by_id_cd84b4da ON public.juvenile USING btree (updated_by_id);


--
-- Name: markaz_created_by_id_8111df1a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX markaz_created_by_id_8111df1a ON public.markaz USING btree (created_by_id);


--
-- Name: markaz_name_7ad80bc5_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX markaz_name_7ad80bc5_like ON public.markaz USING btree (name varchar_pattern_ops);


--
-- Name: markaz_region_id_2d701b82; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX markaz_region_id_2d701b82 ON public.markaz USING btree (region_id);


--
-- Name: markaz_updated_by_id_b6d3a738; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX markaz_updated_by_id_b6d3a738 ON public.markaz USING btree (updated_by_id);


--
-- Name: medical_list_created_by_id_8db72593; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX medical_list_created_by_id_8db72593 ON public.medical_list USING btree (created_by_id);


--
-- Name: medical_list_updated_by_id_366ac6b3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX medical_list_updated_by_id_366ac6b3 ON public.medical_list USING btree (updated_by_id);


--
-- Name: parent_juvenile_created_by_id_44aa5a12; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX parent_juvenile_created_by_id_44aa5a12 ON public.parent_juvenile USING btree (created_by_id);


--
-- Name: parent_juvenile_updated_by_id_092b2b27; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX parent_juvenile_updated_by_id_092b2b27 ON public.parent_juvenile USING btree (updated_by_id);


--
-- Name: prophylactic_inspector_created_by_id_2deeb50e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX prophylactic_inspector_created_by_id_2deeb50e ON public.prophylactic_inspector USING btree (created_by_id);


--
-- Name: prophylactic_inspector_updated_by_id_5f0e25d5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX prophylactic_inspector_updated_by_id_5f0e25d5 ON public.prophylactic_inspector USING btree (updated_by_id);


--
-- Name: region_created_by_id_72ce079f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX region_created_by_id_72ce079f ON public.region USING btree (created_by_id);


--
-- Name: region_name_5fc567df_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX region_name_5fc567df_like ON public.region USING btree (name varchar_pattern_ops);


--
-- Name: region_soato_c090c3c8_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX region_soato_c090c3c8_like ON public.region USING btree (soato varchar_pattern_ops);


--
-- Name: region_updated_by_id_8d32397f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX region_updated_by_id_8d32397f ON public.region USING btree (updated_by_id);


--
-- Name: relationship_juvenile_id_afef9100; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX relationship_juvenile_id_afef9100 ON public.relationship USING btree (juvenile_id);


--
-- Name: relationship_parent_id_0df66cc0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX relationship_parent_id_0df66cc0 ON public.relationship USING btree (parent_id);


--
-- Name: user_email_54dc62b2_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_email_54dc62b2_like ON public."user" USING btree (email varchar_pattern_ops);


--
-- Name: user_groups_customuser_id_246bd336; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_groups_customuser_id_246bd336 ON public.user_groups USING btree (customuser_id);


--
-- Name: user_groups_group_id_b76f8aba; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_groups_group_id_b76f8aba ON public.user_groups USING btree (group_id);


--
-- Name: user_login_7eec5484_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_login_7eec5484_like ON public."user" USING btree (login varchar_pattern_ops);


--
-- Name: user_markaz_id_61d2ab12; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_markaz_id_61d2ab12 ON public."user" USING btree (markaz_id);


--
-- Name: user_user_permissions_customuser_id_3b468234; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_permissions_customuser_id_3b468234 ON public.user_user_permissions USING btree (customuser_id);


--
-- Name: user_user_permissions_permission_id_9deb68a3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_permissions_permission_id_9deb68a3 ON public.user_user_permissions USING btree (permission_id);


--
-- Name: user_username_cf016618_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_username_cf016618_like ON public."user" USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: district district_created_by_id_8bddb121_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.district
    ADD CONSTRAINT district_created_by_id_8bddb121_fk_user_id FOREIGN KEY (created_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: district district_region_id_id_ac67679a_fk_region_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.district
    ADD CONSTRAINT district_region_id_id_ac67679a_fk_region_id FOREIGN KEY (region_id_id) REFERENCES public.region(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: district district_updated_by_id_84a22115_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.district
    ADD CONSTRAINT district_updated_by_id_84a22115_fk_user_id FOREIGN KEY (updated_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_user_id FOREIGN KEY (user_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: juvenile juvenile_address_district_id_120b5633_fk_district_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile
    ADD CONSTRAINT juvenile_address_district_id_120b5633_fk_district_id FOREIGN KEY (address_district_id) REFERENCES public.district(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: juvenile juvenile_birth_district_id_ab58e31d_fk_district_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile
    ADD CONSTRAINT juvenile_birth_district_id_ab58e31d_fk_district_id FOREIGN KEY (birth_district_id) REFERENCES public.district(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: juvenile juvenile_created_by_id_3e2e60f7_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile
    ADD CONSTRAINT juvenile_created_by_id_3e2e60f7_fk_user_id FOREIGN KEY (created_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: juvenile juvenile_inspector_id_c7d57a95_fk_prophylactic_inspector_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile
    ADD CONSTRAINT juvenile_inspector_id_c7d57a95_fk_prophylactic_inspector_id FOREIGN KEY (inspector_id) REFERENCES public.prophylactic_inspector(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: juvenile juvenile_itm_district_id_c874f528_fk_district_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile
    ADD CONSTRAINT juvenile_itm_district_id_c874f528_fk_district_id FOREIGN KEY (itm_district_id) REFERENCES public.district(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: juvenile juvenile_markaz_id_aee5e3e7_fk_markaz_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile
    ADD CONSTRAINT juvenile_markaz_id_aee5e3e7_fk_markaz_id FOREIGN KEY (markaz_id) REFERENCES public.markaz(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: juvenile_medical_list juvenile_medical_lis_medical_list_id_1b726390_fk_medical_l; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile_medical_list
    ADD CONSTRAINT juvenile_medical_lis_medical_list_id_1b726390_fk_medical_l FOREIGN KEY (medical_list_id) REFERENCES public.medical_list(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: juvenile_medical_list juvenile_medical_list_juvenile_id_cfc4002d_fk_juvenile_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile_medical_list
    ADD CONSTRAINT juvenile_medical_list_juvenile_id_cfc4002d_fk_juvenile_id FOREIGN KEY (juvenile_id) REFERENCES public.juvenile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: juvenile juvenile_school_district_id_d466279b_fk_district_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile
    ADD CONSTRAINT juvenile_school_district_id_d466279b_fk_district_id FOREIGN KEY (school_district_id) REFERENCES public.district(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: juvenile juvenile_updated_by_id_cd84b4da_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juvenile
    ADD CONSTRAINT juvenile_updated_by_id_cd84b4da_fk_user_id FOREIGN KEY (updated_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: markaz markaz_created_by_id_8111df1a_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.markaz
    ADD CONSTRAINT markaz_created_by_id_8111df1a_fk_user_id FOREIGN KEY (created_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: markaz markaz_region_id_2d701b82_fk_region_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.markaz
    ADD CONSTRAINT markaz_region_id_2d701b82_fk_region_id FOREIGN KEY (region_id) REFERENCES public.region(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: markaz markaz_updated_by_id_b6d3a738_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.markaz
    ADD CONSTRAINT markaz_updated_by_id_b6d3a738_fk_user_id FOREIGN KEY (updated_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_list medical_list_created_by_id_8db72593_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_list
    ADD CONSTRAINT medical_list_created_by_id_8db72593_fk_user_id FOREIGN KEY (created_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_list medical_list_updated_by_id_366ac6b3_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_list
    ADD CONSTRAINT medical_list_updated_by_id_366ac6b3_fk_user_id FOREIGN KEY (updated_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: parent_juvenile parent_juvenile_created_by_id_44aa5a12_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parent_juvenile
    ADD CONSTRAINT parent_juvenile_created_by_id_44aa5a12_fk_user_id FOREIGN KEY (created_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: parent_juvenile parent_juvenile_updated_by_id_092b2b27_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parent_juvenile
    ADD CONSTRAINT parent_juvenile_updated_by_id_092b2b27_fk_user_id FOREIGN KEY (updated_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: prophylactic_inspector prophylactic_inspector_created_by_id_2deeb50e_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prophylactic_inspector
    ADD CONSTRAINT prophylactic_inspector_created_by_id_2deeb50e_fk_user_id FOREIGN KEY (created_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: prophylactic_inspector prophylactic_inspector_updated_by_id_5f0e25d5_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prophylactic_inspector
    ADD CONSTRAINT prophylactic_inspector_updated_by_id_5f0e25d5_fk_user_id FOREIGN KEY (updated_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: region region_created_by_id_72ce079f_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.region
    ADD CONSTRAINT region_created_by_id_72ce079f_fk_user_id FOREIGN KEY (created_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: region region_updated_by_id_8d32397f_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.region
    ADD CONSTRAINT region_updated_by_id_8d32397f_fk_user_id FOREIGN KEY (updated_by_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: relationship relationship_juvenile_id_afef9100_fk_juvenile_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.relationship
    ADD CONSTRAINT relationship_juvenile_id_afef9100_fk_juvenile_id FOREIGN KEY (juvenile_id) REFERENCES public.juvenile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: relationship relationship_parent_id_0df66cc0_fk_parent_juvenile_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.relationship
    ADD CONSTRAINT relationship_parent_id_0df66cc0_fk_parent_juvenile_id FOREIGN KEY (parent_id) REFERENCES public.parent_juvenile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_groups user_groups_customuser_id_246bd336_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_groups
    ADD CONSTRAINT user_groups_customuser_id_246bd336_fk_user_id FOREIGN KEY (customuser_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_groups user_groups_group_id_b76f8aba_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_groups
    ADD CONSTRAINT user_groups_group_id_b76f8aba_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user user_markaz_id_61d2ab12_fk_markaz_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_markaz_id_61d2ab12_fk_markaz_id FOREIGN KEY (markaz_id) REFERENCES public.markaz(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_permissions user_user_permission_permission_id_9deb68a3_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_permissions
    ADD CONSTRAINT user_user_permission_permission_id_9deb68a3_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_permissions user_user_permissions_customuser_id_3b468234_fk_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_permissions
    ADD CONSTRAINT user_user_permissions_customuser_id_3b468234_fk_user_id FOREIGN KEY (customuser_id) REFERENCES public."user"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

