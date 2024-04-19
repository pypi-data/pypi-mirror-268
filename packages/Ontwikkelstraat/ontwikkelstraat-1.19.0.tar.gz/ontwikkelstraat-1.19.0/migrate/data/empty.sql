
--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5
-- Dumped by pg_dump version 14.5

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

DROP DATABASE backend;
--
-- Name: backend; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE backend WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


ALTER DATABASE backend OWNER TO postgres;

\connect backend

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
-- Name: click; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA click;


ALTER SCHEMA click OWNER TO postgres;

--
-- Name: signal; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA signal;


ALTER SCHEMA signal OWNER TO postgres;

--
-- Name: SCHEMA signal; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA signal IS 'Alles over signalen';


--
-- Name: pg_trgm; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pg_trgm WITH SCHEMA public;


--
-- Name: EXTENSION pg_trgm; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_trgm IS 'text similarity measurement and index searching based on trigrams';


--
-- Name: tablefunc; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS tablefunc WITH SCHEMA public;


--
-- Name: EXTENSION tablefunc; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION tablefunc IS 'functions that manipulate whole tables, including crosstab';


--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: event; Type: TABLE; Schema: click; Owner: postgres
--

CREATE TABLE click.event (
    id integer NOT NULL,
    short_code character(20) NOT NULL,
    session_gid_hash character(20),
    from_item_gid character(36),
    ts timestamp without time zone
);


ALTER TABLE click.event OWNER TO postgres;

--
-- Name: event_id_seq; Type: SEQUENCE; Schema: click; Owner: postgres
--

CREATE SEQUENCE click.event_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE click.event_id_seq OWNER TO postgres;

--
-- Name: event_id_seq; Type: SEQUENCE OWNED BY; Schema: click; Owner: postgres
--

ALTER SEQUENCE click.event_id_seq OWNED BY click.event.id;


--
-- Name: url; Type: TABLE; Schema: click; Owner: postgres
--

CREATE TABLE click.url (
    id integer NOT NULL,
    short_code character(20) NOT NULL,
    long_url character varying
);


ALTER TABLE click.url OWNER TO postgres;

--
-- Name: url_id_seq; Type: SEQUENCE; Schema: click; Owner: postgres
--

CREATE SEQUENCE click.url_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE click.url_id_seq OWNER TO postgres;

--
-- Name: url_id_seq; Type: SEQUENCE OWNED BY; Schema: click; Owner: postgres
--

ALTER SEQUENCE click.url_id_seq OWNED BY click.url.id;


--
-- Name: aanbieder; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aanbieder (
    id integer NOT NULL,
    naam character varying(512),
    website character varying(512),
    beschrijving text,
    kvk integer,
    adres character varying(512),
    locaties text,
    commercieel character(1)
);


ALTER TABLE public.aanbieder OWNER TO postgres;

--
-- Name: aanbieder_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aanbieder_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.aanbieder_id_seq OWNER TO postgres;

--
-- Name: aanbieder_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aanbieder_id_seq OWNED BY public.aanbieder.id;


--
-- Name: aanbod; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aanbod (
    id integer NOT NULL,
    aanbieder_id integer,
    type character varying(512),
    status character varying(512),
    titel character varying(512),
    teaser text,
    tldr text,
    taal character varying(512),
    niveaus text,
    beschrijving text,
    cta text,
    cta_url character varying(512),
    is_online character(1),
    is_offline character(1),
    is_thuiswerk character varying(20)
);


ALTER TABLE public.aanbod OWNER TO postgres;

--
-- Name: aanbod_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aanbod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.aanbod_id_seq OWNER TO postgres;

--
-- Name: aanbod_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aanbod_id_seq OWNED BY public.aanbod.id;


--
-- Name: api_activity; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_activity (
    gid uuid NOT NULL,
    input json,
    output json,
    id integer NOT NULL,
    is_dirty boolean
);


ALTER TABLE public.api_activity OWNER TO postgres;

--
-- Name: TABLE api_activity; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.api_activity IS 'Input and output from the GraphQL API';


--
-- Name: api_activity_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_activity_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.api_activity_id_seq OWNER TO postgres;

--
-- Name: api_activity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_activity_id_seq OWNED BY public.api_activity.id;


--
-- Name: attachment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attachment (
    id integer NOT NULL,
    platform character varying(512),
    gid character varying(512),
    attachment character varying(512),
    filename character varying(512),
    purpose character varying(512),
    ts_uploaded timestamp without time zone,
    owner_gid character varying(512),
    b2_uri character varying(1024)
);


ALTER TABLE public.attachment OWNER TO postgres;

--
-- Name: attachment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.attachment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.attachment_id_seq OWNER TO postgres;

--
-- Name: attachment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.attachment_id_seq OWNED BY public.attachment.id;


--
-- Name: change; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.change (
    change_order integer NOT NULL,
    from_gid character varying(512),
    to_gid character varying(512)
);


ALTER TABLE public.change OWNER TO postgres;

--
-- Name: change_change_order_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.change_change_order_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.change_change_order_seq OWNER TO postgres;

--
-- Name: change_change_order_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.change_change_order_seq OWNED BY public.change.change_order;


--
-- Name: comment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comment (
    id integer NOT NULL,
    platform character varying(512),
    author character varying(512),
    gid character varying(512),
    concerning character varying(512),
    in_response_to character varying(512),
    body character varying(512),
    ts_created timestamp without time zone,
    ts_last_change timestamp without time zone
);


ALTER TABLE public.comment OWNER TO postgres;

--
-- Name: comment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.comment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comment_id_seq OWNER TO postgres;

--
-- Name: comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.comment_id_seq OWNED BY public.comment.id;


--
-- Name: counts_per_minute; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.counts_per_minute (
    id integer NOT NULL,
    gid character varying(36),
    ts timestamp without time zone,
    name character varying(512),
    evidence_id integer,
    evidence_gid character varying(36),
    count integer
);


ALTER TABLE public.counts_per_minute OWNER TO postgres;

--
-- Name: counts_per_minute_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.counts_per_minute_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.counts_per_minute_id_seq OWNER TO postgres;

--
-- Name: counts_per_minute_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.counts_per_minute_id_seq OWNED BY public.counts_per_minute.id;


--
-- Name: cursus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cursus (
    id integer NOT NULL,
    aanbod_id integer
);


ALTER TABLE public.cursus OWNER TO postgres;

--
-- Name: cursus_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cursus_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cursus_id_seq OWNER TO postgres;

--
-- Name: cursus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cursus_id_seq OWNED BY public.cursus.id;


--
-- Name: email_domain; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.email_domain (
    id integer NOT NULL,
    platform character varying(512),
    gid character varying(512),
    org_gid character varying(512),
    domain character varying(512),
    is_new_user_allowed character(1)
);


ALTER TABLE public.email_domain OWNER TO postgres;

--
-- Name: email_domain_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.email_domain_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.email_domain_id_seq OWNER TO postgres;

--
-- Name: email_domain_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.email_domain_id_seq OWNED BY public.email_domain.id;


--
-- Name: ervaring; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ervaring (
    id integer NOT NULL,
    aanbod_id integer,
    titel character varying(512),
    tldr text,
    beschrijving text,
    auteur character varying(512),
    geplaatst_op timestamp without time zone,
    opgedaan_op timestamp without time zone
);


ALTER TABLE public.ervaring OWNER TO postgres;

--
-- Name: ervaring_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ervaring_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ervaring_id_seq OWNER TO postgres;

--
-- Name: ervaring_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ervaring_id_seq OWNED BY public.ervaring.id;


--
-- Name: evenement; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.evenement (
    id integer NOT NULL,
    aanbod_id integer,
    aanvang timestamp without time zone,
    einde timestamp without time zone
);


ALTER TABLE public.evenement OWNER TO postgres;

--
-- Name: evenement_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.evenement_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.evenement_id_seq OWNER TO postgres;

--
-- Name: evenement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.evenement_id_seq OWNED BY public.evenement.id;


--
-- Name: event_stream; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.event_stream (
    id integer NOT NULL,
    gid character varying(512),
    platform character varying(512),
    user_gid character varying(512),
    subject_gid character varying(512),
    subject_type character varying(512),
    ts timestamp without time zone,
    title character varying(512),
    msg character varying(512),
    crud character varying(1),
    session_token character varying(512),
    doc bytea
);


ALTER TABLE public.event_stream OWNER TO postgres;

--
-- Name: COLUMN event_stream.doc; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.event_stream.doc IS 'pickled version of the before item';


--
-- Name: event_stream_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.event_stream_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.event_stream_id_seq OWNER TO postgres;

--
-- Name: event_stream_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.event_stream_id_seq OWNED BY public.event_stream.id;


--
-- Name: evidence; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.evidence (
    id integer NOT NULL,
    gid uuid,
    session_gid uuid,
    source json,
    sha1_digest character varying(40)
);


ALTER TABLE public.evidence OWNER TO postgres;

--
-- Name: evidence_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.evidence_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.evidence_id_seq OWNER TO postgres;

--
-- Name: evidence_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.evidence_id_seq OWNED BY public.evidence.id;


--
-- Name: ewh_implemented_features; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ewh_implemented_features (
    id integer NOT NULL,
    name character varying(512),
    installed character(1),
    last_update_dttm timestamp without time zone
);


ALTER TABLE public.ewh_implemented_features OWNER TO postgres;

--
-- Name: ewh_implemented_features_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ewh_implemented_features_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ewh_implemented_features_id_seq OWNER TO postgres;

--
-- Name: ewh_implemented_features_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ewh_implemented_features_id_seq OWNED BY public.ewh_implemented_features.id;


--
-- Name: fav_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fav_list (
    id integer NOT NULL,
    platform character varying(512),
    gid character varying(512),
    name character varying(512),
    slug character varying(512)
);


ALTER TABLE public.fav_list OWNER TO postgres;

--
-- Name: fav_list_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fav_list_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fav_list_id_seq OWNER TO postgres;

--
-- Name: fav_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fav_list_id_seq OWNED BY public.fav_list.id;


--
-- Name: fav_list_member; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fav_list_member (
    id integer NOT NULL,
    platform character varying(512),
    gid character varying(512),
    list_gid character varying(512),
    user_gid character varying(512),
    ts timestamp without time zone,
    list_role character varying(512)
);


ALTER TABLE public.fav_list_member OWNER TO postgres;

--
-- Name: fav_list_member_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fav_list_member_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fav_list_member_id_seq OWNER TO postgres;

--
-- Name: fav_list_member_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fav_list_member_id_seq OWNED BY public.fav_list_member.id;


--
-- Name: gastles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gastles (
    id integer NOT NULL,
    aanbod_id integer
);


ALTER TABLE public.gastles OWNER TO postgres;

--
-- Name: gastles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.gastles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gastles_id_seq OWNER TO postgres;

--
-- Name: gastles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.gastles_id_seq OWNED BY public.gastles.id;


--
-- Name: item; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.item (
    id integer NOT NULL,
    platform character varying(512),
    author character varying(512),
    name character varying(512),
    gid character varying(512),
    thumbnail character varying(512),
    short_description text,
    ts_changed timestamp without time zone,
    tags text,
    slug character varying(512),
    alternatives text,
    backgrounds text,
    attachments text,
    since_when date,
    upto_when date,
    video_urls text
);


ALTER TABLE public.item OWNER TO postgres;

--
-- Name: item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_id_seq OWNER TO postgres;

--
-- Name: item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.item_id_seq OWNED BY public.item.id;


--
-- Name: leering2020_attachments_en_backgrounds; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.leering2020_attachments_en_backgrounds (
    gid character varying(512),
    backgrounds text,
    attachments text
);


ALTER TABLE public.leering2020_attachments_en_backgrounds OWNER TO postgres;

--
-- Name: mark; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mark (
    id integer NOT NULL,
    platform character varying(512),
    gid character varying(512),
    user_gid character varying(512),
    subject_gid character varying(512),
    subject_type character varying(512),
    list_gid character varying(512),
    mark integer,
    name character varying(512),
    ts timestamp without time zone
);


ALTER TABLE public.mark OWNER TO postgres;

--
-- Name: mark_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mark_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mark_id_seq OWNER TO postgres;

--
-- Name: mark_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mark_id_seq OWNED BY public.mark.id;


--
-- Name: tag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    platform character varying(512),
    gid character varying(512),
    name character varying(512),
    slug character varying(512),
    parents text,
    description character varying(512),
    meta_tags text,
    children text
);


ALTER TABLE public.tag OWNER TO postgres;

--
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    platform text,
    name character varying(512),
    email character varying(512),
    password character varying(512),
    gid character varying(512),
    api_token character varying(512),
    has_validated_email character(1),
    email_verification_code integer,
    property_bag json,
    avatar character varying(512),
    reset_key character varying(20),
    firstname character varying(128) DEFAULT NULL::character varying,
    lastname character varying(128) DEFAULT NULL::character varying,
    user_provided_organisation character varying(256) DEFAULT NULL::character varying,
    user_provided_primary_organisational_role character varying(128) DEFAULT NULL::character varying,
    user_provided_organisation_location character varying(128) DEFAULT NULL::character varying
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- Name: mv__item_tags; Type: MATERIALIZED VIEW; Schema: public; Owner: postgres
--

CREATE MATERIALIZED VIEW public.mv__item_tags AS
 WITH item_tags AS (
         SELECT item.gid,
            array_remove(regexp_split_to_array(item.tags, '\|'::text), ''::text) AS tags
           FROM public.item
        ), used_items AS (
         SELECT item.gid,
            item.name
           FROM (public.item
             JOIN public."user" ON ((((item.author)::text = ("user".gid)::text) AND (("user".email)::text !~~ '%@roc.nl'::text))))
        )
 SELECT (item_tags.gid)::uuid AS item_gid,
    (tag.gid)::uuid AS tag_gid,
    used_items.name AS item_name,
    tag.name AS tag_name
   FROM ((item_tags
     JOIN public.tag ON (((tag.gid)::text = ANY (item_tags.tags))))
     JOIN used_items ON (((item_tags.gid)::text = (used_items.gid)::text)))
  WITH NO DATA;


ALTER TABLE public.mv__item_tags OWNER TO postgres;

--
-- Name: mv__tag_arrays; Type: MATERIALIZED VIEW; Schema: public; Owner: postgres
--

CREATE MATERIALIZED VIEW public.mv__tag_arrays AS
 SELECT tag.id,
    (tag.gid)::uuid AS gid,
    tag.name AS search,
    (array_remove(regexp_split_to_array(tag.children, '\|'::text), ''::text))::uuid[] AS children,
    (array_remove(regexp_split_to_array(tag.parents, '\|'::text), ''::text))::uuid[] AS parents,
    (array_remove(regexp_split_to_array(tag.meta_tags, '\|'::text), ''::text))::uuid[] AS meta_tags
   FROM public.tag
  WITH NO DATA;


ALTER TABLE public.mv__tag_arrays OWNER TO postgres;

--
-- Name: opdracht; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.opdracht (
    id integer NOT NULL,
    aanbod_id integer
);


ALTER TABLE public.opdracht OWNER TO postgres;

--
-- Name: opdracht_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.opdracht_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.opdracht_id_seq OWNER TO postgres;

--
-- Name: opdracht_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.opdracht_id_seq OWNED BY public.opdracht.id;


--
-- Name: opleiding; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.opleiding (
    id integer NOT NULL,
    aanbod_id integer,
    duur integer,
    crebo integer
);


ALTER TABLE public.opleiding OWNER TO postgres;

--
-- Name: opleiding_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.opleiding_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.opleiding_id_seq OWNER TO postgres;

--
-- Name: opleiding_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.opleiding_id_seq OWNED BY public.opleiding.id;


--
-- Name: organisation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.organisation (
    id integer NOT NULL,
    platform text,
    gid text,
    name text,
    coc integer,
    street text,
    number text,
    city text,
    lonlat point,
    tag_gid text,
    validated_ts timestamp without time zone,
    validated_by text,
    country_code character varying,
    aka text,
    website text,
    email text,
    scholen_op_de_kaart_url text,
    aantekeningen text
);


ALTER TABLE public.organisation OWNER TO postgres;

--
-- Name: organisation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.organisation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organisation_id_seq OWNER TO postgres;

--
-- Name: organisation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.organisation_id_seq OWNED BY public.organisation.id;


--
-- Name: prikbord; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prikbord (
    id integer NOT NULL,
    aanbieder_id integer,
    titel character varying(512),
    type character varying(512),
    teaser text,
    tldr text
);


ALTER TABLE public.prikbord OWNER TO postgres;

--
-- Name: prikbord_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.prikbord_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.prikbord_id_seq OWNER TO postgres;

--
-- Name: prikbord_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.prikbord_id_seq OWNED BY public.prikbord.id;


--
-- Name: property_bag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.property_bag (
    id integer NOT NULL,
    gid character(36) NOT NULL,
    belongs_to_gid character(36) NOT NULL,
    properties text
);


ALTER TABLE public.property_bag OWNER TO postgres;

--
-- Name: property_bag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.property_bag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.property_bag_id_seq OWNER TO postgres;

--
-- Name: property_bag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.property_bag_id_seq OWNED BY public.property_bag.id;


--
-- Name: session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.session (
    id integer NOT NULL,
    platform character varying(512),
    user_gid character varying(512),
    session_token character varying(512),
    hw_specs text,
    started timestamp without time zone,
    last_seen timestamp without time zone,
    upgrades text,
    gid_hash character(20)
);


ALTER TABLE public.session OWNER TO postgres;

--
-- Name: session_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.session_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.session_id_seq OWNER TO postgres;

--
-- Name: session_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.session_id_seq OWNED BY public.session.id;


--
-- Name: signal; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.signal (
    id integer NOT NULL,
    gid uuid,
    ts timestamp without time zone,
    name character varying(512),
    source character varying(40),
    session_gid uuid,
    user_gid uuid,
    evidence_id integer,
    evidence_gid uuid,
    related uuid
);


ALTER TABLE public.signal OWNER TO postgres;

--
-- Name: signal_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.signal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.signal_id_seq OWNER TO postgres;

--
-- Name: signal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.signal_id_seq OWNED BY public.signal.id;


--
-- Name: stage; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stage (
    id integer NOT NULL,
    aanbod_id integer
);


ALTER TABLE public.stage OWNER TO postgres;

--
-- Name: stage_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.stage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stage_id_seq OWNER TO postgres;

--
-- Name: stage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.stage_id_seq OWNED BY public.stage.id;


--
-- Name: stats_follow_link_activity; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.stats_follow_link_activity AS
 SELECT e.ts AS "timestamp",
    u.name AS username,
    u.email,
    i.name AS item_name,
    url.long_url AS followed_url,
    ('https://delen.meteddie.nl/item/'::text || (i.gid)::text) AS item_url,
    i.gid AS item_gid,
    u.gid AS user_gid
   FROM ((((public.session s
     JOIN click.event e ON ((s.gid_hash = e.session_gid_hash)))
     LEFT JOIN public."user" u ON (((s.user_gid)::text = (u.gid)::text)))
     JOIN public.item i ON (((i.gid)::bpchar = e.from_item_gid)))
     JOIN click.url url ON ((url.short_code = e.short_code)));


ALTER TABLE public.stats_follow_link_activity OWNER TO postgres;

--
-- Name: stats_follow_link_activity_detail; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.stats_follow_link_activity_detail AS
 SELECT e.ts AS "timestamp",
    u.name AS username,
    u.email,
    i.name AS item_name,
    url.long_url AS followed_url,
    ('https://delen.meteddie.nl/item/'::text || (i.gid)::text) AS item_url,
    i.gid AS item_gid,
    u.gid AS user_gid
   FROM ((((public.session s
     JOIN click.event e ON ((s.gid_hash = e.session_gid_hash)))
     LEFT JOIN public."user" u ON (((s.user_gid)::text = (u.gid)::text)))
     JOIN public.item i ON (((i.gid)::bpchar = e.from_item_gid)))
     JOIN click.url url ON ((url.short_code = e.short_code)));


ALTER TABLE public.stats_follow_link_activity_detail OWNER TO postgres;

--
-- Name: stats_follow_link_date_domain_count; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.stats_follow_link_date_domain_count AS
 SELECT date(event_root.ts) AS date,
    array_to_string(regexp_matches((url.long_url)::text, '://([^/]*)'::text), ''::text) AS domain,
    count(*) AS number_of_clicks
   FROM (click.event event_root
     JOIN click.url url ON ((url.short_code = event_root.short_code)))
  GROUP BY (date(event_root.ts)), (array_to_string(regexp_matches((url.long_url)::text, '://([^/]*)'::text), ''::text))
  ORDER BY (date(event_root.ts)) DESC;


ALTER TABLE public.stats_follow_link_date_domain_count OWNER TO postgres;

--
-- Name: stats_subject_favs; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.stats_subject_favs AS
 SELECT mark.subject_gid AS gid,
    count(*) AS favs
   FROM public.mark
  WHERE (((mark.name)::text = 'fav'::text) AND (mark.mark <> 0))
  GROUP BY mark.subject_gid;


ALTER TABLE public.stats_subject_favs OWNER TO postgres;

--
-- Name: stats_subject_thumbs; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.stats_subject_thumbs AS
 SELECT mark.subject_gid AS gid,
    count(*) AS thumbs
   FROM public.mark
  WHERE (((mark.name)::text = 'thumbs'::text) AND (mark.mark <> 0))
  GROUP BY mark.subject_gid;


ALTER TABLE public.stats_subject_thumbs OWNER TO postgres;

--
-- Name: stats_subject_views; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.stats_subject_views AS
 SELECT event_stream.subject_gid AS gid,
    count(DISTINCT event_stream.session_token) AS tokens
   FROM public.event_stream
  GROUP BY event_stream.subject_gid;


ALTER TABLE public.stats_subject_views OWNER TO postgres;

--
-- Name: stats_zoektermen; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.stats_zoektermen AS
 WITH bla AS (
         SELECT count(*) AS referer_count,
            (((api_activity.input ->> 'headers'::text))::json ->> 'Referer'::text) AS referer
           FROM public.api_activity
          WHERE ((((api_activity.input ->> 'headers'::text))::json ->> 'Referer'::text) ~~ 'https://delen.meteddie.nl%term=%'::text)
          GROUP BY (((api_activity.input ->> 'headers'::text))::json ->> 'Referer'::text)
        )
 SELECT bla.referer_count,
    replace(split_part(bla.referer, '&term='::text, 2), '%20'::text, ' '::text) AS replace
   FROM bla
  ORDER BY bla.referer_count DESC;


ALTER TABLE public.stats_zoektermen OWNER TO postgres;

--
-- Name: sticker; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sticker (
    id integer NOT NULL,
    tag_gid character(36) NOT NULL,
    attachment_gid character(36) NOT NULL
);


ALTER TABLE public.sticker OWNER TO postgres;

--
-- Name: sticker_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sticker_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sticker_id_seq OWNER TO postgres;

--
-- Name: sticker_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sticker_id_seq OWNED BY public.sticker.id;


--
-- Name: taak; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.taak (
    id integer NOT NULL,
    titel character varying(512),
    omschrijving text,
    auteur_id integer,
    opdracht_id integer
);


ALTER TABLE public.taak OWNER TO postgres;

--
-- Name: taak_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.taak_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.taak_id_seq OWNER TO postgres;

--
-- Name: taak_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.taak_id_seq OWNED BY public.taak.id;


--
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_id_seq OWNER TO postgres;

--
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- Name: training; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.training (
    id integer NOT NULL,
    aanbod_id integer
);


ALTER TABLE public.training OWNER TO postgres;

--
-- Name: training_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.training_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.training_id_seq OWNER TO postgres;

--
-- Name: training_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.training_id_seq OWNED BY public.training.id;


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
-- Name: user_notification; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_notification (
    id integer NOT NULL,
    gid character varying(512),
    platform character varying(512),
    user_gid character varying(512),
    subject_gid character varying(512),
    subject_type character varying(512),
    ts timestamp without time zone,
    title character varying(512),
    msg character varying(512),
    read_ts timestamp without time zone
);


ALTER TABLE public.user_notification OWNER TO postgres;

--
-- Name: user_notification_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_notification_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_notification_id_seq OWNER TO postgres;

--
-- Name: user_notification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_notification_id_seq OWNED BY public.user_notification.id;


--
-- Name: counts_per_minute; Type: TABLE; Schema: signal; Owner: postgres
--

CREATE TABLE signal.counts_per_minute (
    id integer NOT NULL,
    gid character varying(36),
    ts timestamp without time zone,
    name character varying(512),
    evidence_id integer,
    evidence_gid character varying(36),
    count integer
);


ALTER TABLE signal.counts_per_minute OWNER TO postgres;

--
-- Name: counts_per_minute_id_seq; Type: SEQUENCE; Schema: signal; Owner: postgres
--

CREATE SEQUENCE signal.counts_per_minute_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE signal.counts_per_minute_id_seq OWNER TO postgres;

--
-- Name: counts_per_minute_id_seq; Type: SEQUENCE OWNED BY; Schema: signal; Owner: postgres
--

ALTER SEQUENCE signal.counts_per_minute_id_seq OWNED BY signal.counts_per_minute.id;


--
-- Name: evidence; Type: TABLE; Schema: signal; Owner: postgres
--

CREATE TABLE signal.evidence (
    id integer NOT NULL,
    gid character varying(36),
    session_gid character varying(36),
    source json,
    sha1_digest character varying(40)
);


ALTER TABLE signal.evidence OWNER TO postgres;

--
-- Name: evidence_id_seq; Type: SEQUENCE; Schema: signal; Owner: postgres
--

CREATE SEQUENCE signal.evidence_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE signal.evidence_id_seq OWNER TO postgres;

--
-- Name: evidence_id_seq; Type: SEQUENCE OWNED BY; Schema: signal; Owner: postgres
--

ALTER SEQUENCE signal.evidence_id_seq OWNED BY signal.evidence.id;


--
-- Name: signal; Type: TABLE; Schema: signal; Owner: postgres
--

CREATE TABLE signal.signal (
    id integer NOT NULL,
    gid character varying(36),
    ts timestamp without time zone,
    name character varying(512),
    evidence_id integer,
    evidence_gid character varying(36),
    related character varying(36)
);


ALTER TABLE signal.signal OWNER TO postgres;

--
-- Name: signal_id_seq; Type: SEQUENCE; Schema: signal; Owner: postgres
--

CREATE SEQUENCE signal.signal_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE signal.signal_id_seq OWNER TO postgres;

--
-- Name: signal_id_seq; Type: SEQUENCE OWNED BY; Schema: signal; Owner: postgres
--

ALTER SEQUENCE signal.signal_id_seq OWNED BY signal.signal.id;


--
-- Name: signals_per_month; Type: VIEW; Schema: signal; Owner: postgres
--

CREATE VIEW signal.signals_per_month AS
 SELECT row_number() OVER (ORDER BY (to_char(signal.ts, 'YYYY-MM'::text))) AS id,
    signal.name,
    to_char(signal.ts, 'YYYY-MM'::text) AS year_month,
    count(*) AS count
   FROM signal.signal signal
  GROUP BY signal.name, (to_char(signal.ts, 'YYYY-MM'::text));


ALTER TABLE signal.signals_per_month OWNER TO postgres;

--
-- Name: event id; Type: DEFAULT; Schema: click; Owner: postgres
--

ALTER TABLE ONLY click.event ALTER COLUMN id SET DEFAULT nextval('click.event_id_seq'::regclass);


--
-- Name: url id; Type: DEFAULT; Schema: click; Owner: postgres
--

ALTER TABLE ONLY click.url ALTER COLUMN id SET DEFAULT nextval('click.url_id_seq'::regclass);


--
-- Name: aanbieder id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aanbieder ALTER COLUMN id SET DEFAULT nextval('public.aanbieder_id_seq'::regclass);


--
-- Name: aanbod id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aanbod ALTER COLUMN id SET DEFAULT nextval('public.aanbod_id_seq'::regclass);


--
-- Name: api_activity id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_activity ALTER COLUMN id SET DEFAULT nextval('public.api_activity_id_seq'::regclass);


--
-- Name: attachment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attachment ALTER COLUMN id SET DEFAULT nextval('public.attachment_id_seq'::regclass);


--
-- Name: change change_order; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.change ALTER COLUMN change_order SET DEFAULT nextval('public.change_change_order_seq'::regclass);


--
-- Name: comment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comment ALTER COLUMN id SET DEFAULT nextval('public.comment_id_seq'::regclass);


--
-- Name: counts_per_minute id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.counts_per_minute ALTER COLUMN id SET DEFAULT nextval('public.counts_per_minute_id_seq'::regclass);


--
-- Name: cursus id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cursus ALTER COLUMN id SET DEFAULT nextval('public.cursus_id_seq'::regclass);


--
-- Name: email_domain id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.email_domain ALTER COLUMN id SET DEFAULT nextval('public.email_domain_id_seq'::regclass);


--
-- Name: ervaring id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ervaring ALTER COLUMN id SET DEFAULT nextval('public.ervaring_id_seq'::regclass);


--
-- Name: evenement id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.evenement ALTER COLUMN id SET DEFAULT nextval('public.evenement_id_seq'::regclass);


--
-- Name: event_stream id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_stream ALTER COLUMN id SET DEFAULT nextval('public.event_stream_id_seq'::regclass);


--
-- Name: evidence id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.evidence ALTER COLUMN id SET DEFAULT nextval('public.evidence_id_seq'::regclass);


--
-- Name: ewh_implemented_features id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ewh_implemented_features ALTER COLUMN id SET DEFAULT nextval('public.ewh_implemented_features_id_seq'::regclass);


--
-- Name: fav_list id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fav_list ALTER COLUMN id SET DEFAULT nextval('public.fav_list_id_seq'::regclass);


--
-- Name: fav_list_member id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fav_list_member ALTER COLUMN id SET DEFAULT nextval('public.fav_list_member_id_seq'::regclass);


--
-- Name: gastles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gastles ALTER COLUMN id SET DEFAULT nextval('public.gastles_id_seq'::regclass);


--
-- Name: item id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item ALTER COLUMN id SET DEFAULT nextval('public.item_id_seq'::regclass);


--
-- Name: mark id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mark ALTER COLUMN id SET DEFAULT nextval('public.mark_id_seq'::regclass);


--
-- Name: opdracht id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opdracht ALTER COLUMN id SET DEFAULT nextval('public.opdracht_id_seq'::regclass);


--
-- Name: opleiding id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opleiding ALTER COLUMN id SET DEFAULT nextval('public.opleiding_id_seq'::regclass);


--
-- Name: organisation id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.organisation ALTER COLUMN id SET DEFAULT nextval('public.organisation_id_seq'::regclass);


--
-- Name: prikbord id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prikbord ALTER COLUMN id SET DEFAULT nextval('public.prikbord_id_seq'::regclass);


--
-- Name: property_bag id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.property_bag ALTER COLUMN id SET DEFAULT nextval('public.property_bag_id_seq'::regclass);


--
-- Name: session id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.session ALTER COLUMN id SET DEFAULT nextval('public.session_id_seq'::regclass);


--
-- Name: signal id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.signal ALTER COLUMN id SET DEFAULT nextval('public.signal_id_seq'::regclass);


--
-- Name: stage id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stage ALTER COLUMN id SET DEFAULT nextval('public.stage_id_seq'::regclass);


--
-- Name: sticker id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sticker ALTER COLUMN id SET DEFAULT nextval('public.sticker_id_seq'::regclass);


--
-- Name: taak id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.taak ALTER COLUMN id SET DEFAULT nextval('public.taak_id_seq'::regclass);


--
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- Name: training id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.training ALTER COLUMN id SET DEFAULT nextval('public.training_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: user_notification id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_notification ALTER COLUMN id SET DEFAULT nextval('public.user_notification_id_seq'::regclass);


--
-- Name: counts_per_minute id; Type: DEFAULT; Schema: signal; Owner: postgres
--

ALTER TABLE ONLY signal.counts_per_minute ALTER COLUMN id SET DEFAULT nextval('signal.counts_per_minute_id_seq'::regclass);


--
-- Name: evidence id; Type: DEFAULT; Schema: signal; Owner: postgres
--

ALTER TABLE ONLY signal.evidence ALTER COLUMN id SET DEFAULT nextval('signal.evidence_id_seq'::regclass);


--
-- Name: signal id; Type: DEFAULT; Schema: signal; Owner: postgres
--

ALTER TABLE ONLY signal.signal ALTER COLUMN id SET DEFAULT nextval('signal.signal_id_seq'::regclass);


--
-- Data for Name: event; Type: TABLE DATA; Schema: click; Owner: postgres
--

COPY click.event (id, short_code, session_gid_hash, from_item_gid, ts) FROM stdin;
\.


--
-- Data for Name: signal; Type: TABLE DATA; Schema: signal; Owner: postgres
--

COPY signal.signal (id, gid, ts, name, evidence_id, evidence_gid, related) FROM stdin;
\.


--
-- Name: event_id_seq; Type: SEQUENCE SET; Schema: click; Owner: postgres
--

SELECT pg_catalog.setval('click.event_id_seq', 127701, true);


--
-- Name: url_id_seq; Type: SEQUENCE SET; Schema: click; Owner: postgres
--

SELECT pg_catalog.setval('click.url_id_seq', 3865730, true);


--
-- Name: aanbieder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.aanbieder_id_seq', 1, true);


--
-- Name: aanbod_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.aanbod_id_seq', 1, true);


--
-- Name: api_activity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_activity_id_seq', 467828, true);


--
-- Name: attachment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attachment_id_seq', 3920, true);


--
-- Name: change_change_order_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.change_change_order_seq', 1, false);


--
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.comment_id_seq', 1886, true);


--
-- Name: counts_per_minute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.counts_per_minute_id_seq', 1, false);


--
-- Name: cursus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cursus_id_seq', 1, false);


--
-- Name: email_domain_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.email_domain_id_seq', 11396, true);


--
-- Name: ervaring_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ervaring_id_seq', 1, false);


--
-- Name: evenement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.evenement_id_seq', 1, false);


--
-- Name: event_stream_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.event_stream_id_seq', 283942, true);


--
-- Name: evidence_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.evidence_id_seq', 837006, true);


--
-- Name: ewh_implemented_features_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ewh_implemented_features_id_seq', 33, true);


--
-- Name: fav_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fav_list_id_seq', 411, true);


--
-- Name: fav_list_member_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fav_list_member_id_seq', 715, true);


--
-- Name: gastles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.gastles_id_seq', 1, false);


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.item_id_seq', 6925, true);


--
-- Name: mark_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mark_id_seq', 4131, true);


--
-- Name: opdracht_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.opdracht_id_seq', 1, true);


--
-- Name: opleiding_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.opleiding_id_seq', 1, true);


--
-- Name: organisation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.organisation_id_seq', 8035, true);


--
-- Name: prikbord_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.prikbord_id_seq', 1, false);


--
-- Name: property_bag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.property_bag_id_seq', 1306, true);


--
-- Name: session_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.session_id_seq', 348790, true);


--
-- Name: signal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.signal_id_seq', 870448, true);


--
-- Name: stage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.stage_id_seq', 1, false);


--
-- Name: sticker_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sticker_id_seq', 40, true);


--
-- Name: taak_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.taak_id_seq', 2, true);


--
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tag_id_seq', 32681, true);


--
-- Name: training_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.training_id_seq', 1, false);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 3571, true);


--
-- Name: user_notification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_notification_id_seq', 547, true);


--
-- Name: counts_per_minute_id_seq; Type: SEQUENCE SET; Schema: signal; Owner: postgres
--

SELECT pg_catalog.setval('signal.counts_per_minute_id_seq', 41541, true);


--
-- Name: evidence_id_seq; Type: SEQUENCE SET; Schema: signal; Owner: postgres
--

SELECT pg_catalog.setval('signal.evidence_id_seq', 22118, true);


--
-- Name: signal_id_seq; Type: SEQUENCE SET; Schema: signal; Owner: postgres
--

SELECT pg_catalog.setval('signal.signal_id_seq', 479653, true);


--
-- Name: event event_pkey; Type: CONSTRAINT; Schema: click; Owner: postgres
--

ALTER TABLE ONLY click.event
    ADD CONSTRAINT event_pkey PRIMARY KEY (id);


--
-- Name: url url_pkey; Type: CONSTRAINT; Schema: click; Owner: postgres
--

ALTER TABLE ONLY click.url
    ADD CONSTRAINT url_pkey PRIMARY KEY (id);


--
-- Name: url url_short_code_key; Type: CONSTRAINT; Schema: click; Owner: postgres
--

ALTER TABLE ONLY click.url
    ADD CONSTRAINT url_short_code_key UNIQUE (short_code);


--
-- Name: aanbieder aanbieder_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aanbieder
    ADD CONSTRAINT aanbieder_pkey PRIMARY KEY (id);


--
-- Name: aanbod aanbod_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aanbod
    ADD CONSTRAINT aanbod_pkey PRIMARY KEY (id);


--
-- Name: aanbod aanbod_titel_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aanbod
    ADD CONSTRAINT aanbod_titel_key UNIQUE (titel);


--
-- Name: api_activity api_activity_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_activity
    ADD CONSTRAINT api_activity_pk PRIMARY KEY (gid);


--
-- Name: attachment attachment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attachment
    ADD CONSTRAINT attachment_pkey PRIMARY KEY (id);


--
-- Name: change change_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.change
    ADD CONSTRAINT change_pk PRIMARY KEY (change_order);


--
-- Name: comment comment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_pkey PRIMARY KEY (id);


--
-- Name: counts_per_minute counts_per_minute_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.counts_per_minute
    ADD CONSTRAINT counts_per_minute_pkey PRIMARY KEY (id);


--
-- Name: cursus cursus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cursus
    ADD CONSTRAINT cursus_pkey PRIMARY KEY (id);


--
-- Name: email_domain email_domain_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.email_domain
    ADD CONSTRAINT email_domain_pkey PRIMARY KEY (id);


--
-- Name: ervaring ervaring_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ervaring
    ADD CONSTRAINT ervaring_pkey PRIMARY KEY (id);


--
-- Name: evenement evenement_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.evenement
    ADD CONSTRAINT evenement_pkey PRIMARY KEY (id);


--
-- Name: event_stream event_stream_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_stream
    ADD CONSTRAINT event_stream_pkey PRIMARY KEY (id);


--
-- Name: evidence evidence_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.evidence
    ADD CONSTRAINT evidence_pkey PRIMARY KEY (id);


--
-- Name: ewh_implemented_features ewh_implemented_features_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ewh_implemented_features
    ADD CONSTRAINT ewh_implemented_features_name_key UNIQUE (name);


--
-- Name: ewh_implemented_features ewh_implemented_features_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ewh_implemented_features
    ADD CONSTRAINT ewh_implemented_features_pkey PRIMARY KEY (id);


--
-- Name: fav_list_member fav_list_member_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fav_list_member
    ADD CONSTRAINT fav_list_member_pkey PRIMARY KEY (id);


--
-- Name: fav_list fav_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fav_list
    ADD CONSTRAINT fav_list_pkey PRIMARY KEY (id);


--
-- Name: gastles gastles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gastles
    ADD CONSTRAINT gastles_pkey PRIMARY KEY (id);


--
-- Name: item item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT item_pkey PRIMARY KEY (id);


--
-- Name: mark mark_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mark
    ADD CONSTRAINT mark_pkey PRIMARY KEY (id);


--
-- Name: opdracht opdracht_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opdracht
    ADD CONSTRAINT opdracht_pkey PRIMARY KEY (id);


--
-- Name: opleiding opleiding_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opleiding
    ADD CONSTRAINT opleiding_pkey PRIMARY KEY (id);


--
-- Name: organisation organisation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.organisation
    ADD CONSTRAINT organisation_pkey PRIMARY KEY (id);


--
-- Name: prikbord prikbord_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prikbord
    ADD CONSTRAINT prikbord_pkey PRIMARY KEY (id);


--
-- Name: property_bag property_bag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.property_bag
    ADD CONSTRAINT property_bag_pkey PRIMARY KEY (id);


--
-- Name: session session_gid_hash_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.session
    ADD CONSTRAINT session_gid_hash_key UNIQUE (gid_hash);


--
-- Name: session session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.session
    ADD CONSTRAINT session_pkey PRIMARY KEY (id);


--
-- Name: signal signal_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.signal
    ADD CONSTRAINT signal_pkey PRIMARY KEY (id);


--
-- Name: stage stage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stage
    ADD CONSTRAINT stage_pkey PRIMARY KEY (id);


--
-- Name: sticker sticker_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sticker
    ADD CONSTRAINT sticker_pkey PRIMARY KEY (id);


--
-- Name: taak taak_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.taak
    ADD CONSTRAINT taak_pkey PRIMARY KEY (id);


--
-- Name: tag tag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_pkey PRIMARY KEY (id);


--
-- Name: training training_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.training
    ADD CONSTRAINT training_pkey PRIMARY KEY (id);


--
-- Name: user_notification user_notification_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_notification
    ADD CONSTRAINT user_notification_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: counts_per_minute counts_per_minute_pkey; Type: CONSTRAINT; Schema: signal; Owner: postgres
--

ALTER TABLE ONLY signal.counts_per_minute
    ADD CONSTRAINT counts_per_minute_pkey PRIMARY KEY (id);


--
-- Name: evidence evidence_pkey; Type: CONSTRAINT; Schema: signal; Owner: postgres
--

ALTER TABLE ONLY signal.evidence
    ADD CONSTRAINT evidence_pkey PRIMARY KEY (id);


--
-- Name: signal signal_pkey; Type: CONSTRAINT; Schema: signal; Owner: postgres
--

ALTER TABLE ONLY signal.signal
    ADD CONSTRAINT signal_pkey PRIMARY KEY (id);


--
-- Name: click_event_id_uidex; Type: INDEX; Schema: click; Owner: postgres
--

CREATE UNIQUE INDEX click_event_id_uidex ON click.event USING btree (id);


--
-- Name: click_url_id_uidex; Type: INDEX; Schema: click; Owner: postgres
--

CREATE UNIQUE INDEX click_url_id_uidex ON click.url USING btree (id);


--
-- Name: click_url_short_code_uidex; Type: INDEX; Schema: click; Owner: postgres
--

CREATE UNIQUE INDEX click_url_short_code_uidex ON click.url USING btree (short_code);


--
-- Name: api_activity_gid_uindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX api_activity_gid_uindex ON public.api_activity USING btree (gid);


--
-- Name: api_activity_id_uindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX api_activity_id_uindex ON public.api_activity USING btree (id);


--
-- Name: change_change_order_uindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX change_change_order_uindex ON public.change USING btree (change_order);


--
-- Name: idx_item__gid__id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_item__gid__id ON public.item USING btree (gid) INCLUDE (id);


--
-- Name: idx_item_tags; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_item_tags ON public.item USING btree (gid) INCLUDE (tags);


--
-- Name: idx_mv__item_tags__item_gid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_mv__item_tags__item_gid ON public.mv__item_tags USING btree (item_gid) INCLUDE (tag_gid);


--
-- Name: idx_mv__item_tags__tag_gid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_mv__item_tags__tag_gid ON public.mv__item_tags USING btree (tag_gid) INCLUDE (item_gid);


--
-- Name: idx_tag__gid__id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_tag__gid__id ON public.tag USING btree (gid) INCLUDE (id);


--
-- Name: item_gid_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX item_gid_idx ON public.item USING btree (gid);

ALTER TABLE public.item CLUSTER ON item_gid_idx;


--
-- Name: property_bag__belongs_to_gid_uindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX property_bag__belongs_to_gid_uindex ON public.property_bag USING btree (belongs_to_gid);


--
-- Name: property_bag_gid_uindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX property_bag_gid_uindex ON public.property_bag USING btree (gid);


--
-- Name: property_bag_id_uindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX property_bag_id_uindex ON public.property_bag USING btree (id);


--
-- Name: sticker_gids_uindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX sticker_gids_uindex ON public.sticker USING btree (tag_gid, attachment_gid);


--
-- Name: sticker_id_uindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX sticker_id_uindex ON public.sticker USING btree (id);


--
-- Name: user_gid_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX user_gid_idx ON public."user" USING btree (gid);

ALTER TABLE public."user" CLUSTER ON user_gid_idx;


--
-- Name: signal_timestamp; Type: INDEX; Schema: signal; Owner: postgres
--

CREATE INDEX signal_timestamp ON signal.signal USING btree (ts);


--
-- Name: aanbod aanbod_aanbieder_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aanbod
    ADD CONSTRAINT aanbod_aanbieder_id_fkey FOREIGN KEY (aanbieder_id) REFERENCES public.aanbieder(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: counts_per_minute counts_per_minute_evidence_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.counts_per_minute
    ADD CONSTRAINT counts_per_minute_evidence_id_fkey FOREIGN KEY (evidence_id) REFERENCES public.evidence(id) ON DELETE CASCADE;


--
-- Name: cursus cursus_aanbod_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cursus
    ADD CONSTRAINT cursus_aanbod_id_fkey FOREIGN KEY (aanbod_id) REFERENCES public.aanbod(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ervaring ervaring_aanbod_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ervaring
    ADD CONSTRAINT ervaring_aanbod_id_fkey FOREIGN KEY (aanbod_id) REFERENCES public.aanbod(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: evenement evenement_aanbod_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.evenement
    ADD CONSTRAINT evenement_aanbod_id_fkey FOREIGN KEY (aanbod_id) REFERENCES public.aanbod(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: gastles gastles_aanbod_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gastles
    ADD CONSTRAINT gastles_aanbod_id_fkey FOREIGN KEY (aanbod_id) REFERENCES public.aanbod(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: opdracht opdracht_aanbod_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opdracht
    ADD CONSTRAINT opdracht_aanbod_id_fkey FOREIGN KEY (aanbod_id) REFERENCES public.aanbod(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: opleiding opleiding_aanbod_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opleiding
    ADD CONSTRAINT opleiding_aanbod_id_fkey FOREIGN KEY (aanbod_id) REFERENCES public.aanbod(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: prikbord prikbord_aanbieder_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prikbord
    ADD CONSTRAINT prikbord_aanbieder_id_fkey FOREIGN KEY (aanbieder_id) REFERENCES public.aanbieder(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: signal signal_evidence_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.signal
    ADD CONSTRAINT signal_evidence_id_fkey FOREIGN KEY (evidence_id) REFERENCES public.evidence(id) ON DELETE CASCADE;


--
-- Name: stage stage_aanbod_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stage
    ADD CONSTRAINT stage_aanbod_id_fkey FOREIGN KEY (aanbod_id) REFERENCES public.aanbod(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: taak taak_opdracht_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.taak
    ADD CONSTRAINT taak_opdracht_id_fkey FOREIGN KEY (opdracht_id) REFERENCES public.opdracht(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: training training_aanbod_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.training
    ADD CONSTRAINT training_aanbod_id_fkey FOREIGN KEY (aanbod_id) REFERENCES public.aanbod(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: counts_per_minute counts_per_minute_evidence_id_fkey; Type: FK CONSTRAINT; Schema: signal; Owner: postgres
--

ALTER TABLE ONLY signal.counts_per_minute
    ADD CONSTRAINT counts_per_minute_evidence_id_fkey FOREIGN KEY (evidence_id) REFERENCES signal.evidence(id) ON DELETE CASCADE;


--
-- Name: signal signal_evidence_id_fkey; Type: FK CONSTRAINT; Schema: signal; Owner: postgres
--

ALTER TABLE ONLY signal.signal
    ADD CONSTRAINT signal_evidence_id_fkey FOREIGN KEY (evidence_id) REFERENCES signal.evidence(id) ON DELETE CASCADE;


--
-- Name: mv__item_tags; Type: MATERIALIZED VIEW DATA; Schema: public; Owner: postgres
--

REFRESH MATERIALIZED VIEW public.mv__item_tags;


--
-- Name: mv__tag_arrays; Type: MATERIALIZED VIEW DATA; Schema: public; Owner: postgres
--

REFRESH MATERIALIZED VIEW public.mv__tag_arrays;


--
-- PostgreSQL database dump complete
--

