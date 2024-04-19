drop view if exists aangeboden_opleiding;
create view aangeboden_opleiding as
with source_tables as (select onderwijslocatiecode, onderwijsaanbiederid, 'aangeboden_bo_opleidingen' as ao_table
                       from aangeboden_bo_opleidingen
                       union all
                       select onderwijslocatiecode, onderwijsaanbiederid, 'aangeboden_ho_opleidingen' as ao_table
                       from aangeboden_ho_opleidingen
                       union all
                       select onderwijslocatiecode, onderwijsaanbiederid, 'aangeboden_mbo_opleidingen' as ao_table
                       from aangeboden_mbo_opleidingen
                       union  all
                       select onderwijslocatiecode, onderwijsaanbiederid, 'aangeboden_so_opleidingen' as ao_table
                       from aangeboden_so_opleidingen
                       union all
                       select onderwijslocatiecode, onderwijsaanbiederid, 'aangeboden_vavo_opleidingen' as ao_table
                       from aangeboden_vavo_opleidingen
                       union all
                       select onderwijslocatiecode, onderwijsaanbiederid, 'aangeboden_vo_opleidingen' as ao_table
                       from aangeboden_vo_opleidingen
                       union all
                       select onderwijslocatiecode, onderwijsaanbiederid, 'aangeboden_vso_opleidingen' as ao_table
                       from aangeboden_vso_opleidingen
                       union all
                       select onderwijslocatiecode, onderwijsaanbiederid, 'aangeboden_nfo_opleidingen' as ao_table
                       from aangeboden_nfo_opleidingen)
select onderwijslocatiecode, onderwijsaanbiederid, group_concat(ao_table, ',') as sources
from source_tables
group by onderwijslocatiecode, onderwijsaanbiederid
;

--

select group_concat(id, ','),
       onderwijsbestuurid,
       inbedrijfdatum,
       uitbedrijfdatum,
       kvk_nummer,
       rsin,
       begindatum_periode,
       einddatum_periode,
       internationale_naam,
       naam
from onderwijsbesturen
group by onderwijsbestuurid, inbedrijfdatum, uitbedrijfdatum, kvk_nummer, rsin, begindatum_periode, einddatum_periode,
         internationale_naam, naam

select * from mbo_aantallen_bron;

with per_org  as (
    select
        instellingscode,
        sum(cast(aantal_hoofdinschrijvingen as integer)) as leerlingen
    from mbo_aantallen_bron
    group by instellingscode
)
select
    main.instellingscode as brinnummer,
    main.onderwijslocatie,
    main.aantal_hoofdinschrijvingen as aantal_leerlingen_per_vestiging,
    per_org.leerlingen as aantal_leerlingen_per_organisatie
from mbo_aantallen_bron main
    inner join per_org on main.instellingscode = per_org.instellingscode



--drop view if exists edwh_onderwijslocaties;
create index versnel_onderwijslocatiecode on onderwijslocaties (onderwijslocatiecode);

--create view edwh_onderwijslocaties as

PRAGMA analysis_limit=1000;
PRAGMA optimize;

explain query plan
select case
           when oa.naam is null and olg.uitbedrijfdatum is not null then 'Niet langer gebruikt'
           when oa.naam is null and olg.uitbedrijfdatum is null then 'Geen opleiding geregistreerd'
           else oa.naam end                                                                                   as naam
     --, oa.onderwijsaanbiederid
     , group_concat(ob.naam, '; ')                                                                            as besturen
     -- , group_concat(ob.naam || '(' || ob.onderwijsbestuurid || ')', ';') as besturen_met_code
     --, ob.onderwijsbestuurid
     , ol.straatnaam
     , ol.huisnummer
     , ol.huisnummertoevoeging
     , ol.postcode
     , ol.plaatsnaam
     , ol.gps_latitude
     , ol.gps_longitude
     , ol.onderwijslocatiecode
     , replace(replace(ao.sources, 'aangeboden_', ''), '_opleidingen', '')                                    as sources
     , group_concat(distinct rov.vestigingscode)                                                              as vestiging_brins
     , case
           when coalesce(olg.uitbedrijfdatum, oa.einddatum_periode, 'Y') = 'Y' then 'Y'
           else 'N' end                                                                                       as in_bedrijf
     , coalesce(sum(mbo_aantallen.aantal), 0)
    + coalesce(sum(po_aantallen.aantal_2022), 0)
    + coalesce(sum(vo_aantallen.aantal), 0)
    + coalesce(sum(ho_aantallen.aantal_2022), 0)
    + coalesce(sum(wo_aantallen.aantal_2022), 0)
                                                                                                              as aantal_leerlingen_per_vestiging
     , coalesce(sum(mbo_aantallen.aantal), 0)
    + coalesce(sum(po_aantallen.aantal_2022), 0)
    + coalesce(sum(vo_aantallen.aantal), 0)
    + coalesce(sum(ho_aantallen.aantal_2022), 0)
    + coalesce(sum(wo_aantallen.aantal_2022), 0)
                                                                                                              as aantal_leerlingen_per_organisatie
from onderwijslocatiegebruiken olg
         left outer join onderwijslocaties ol
                         on olg.onderwijslocatiecode = ol.onderwijslocatiecode
         left outer join onderwijsbesturen ob
                         on olg.onderwijsbestuurid = ob.onderwijsbestuurid and ob.einddatum_periode is null
         left outer join aangeboden_opleidingen_materialized ao on ol.onderwijslocatiecode = ao.onderwijslocatiecode
         left outer join onderwijsaanbieders oa
                         on oa.onderwijsaanbiederid = ao.onderwijsaanbiederid -- and oa.einddatum_periode is null
         left outer join relaties_onderwijsbesturen_onderwijsaanbieders roa
                         on roa.onderwijsaanbiederid = oa.onderwijsaanbiederid
                             and roa.onderwijsbestuurid = ob.onderwijsbestuurid
    --and roa.einddatum is null
         left outer join relaties_onderwijslocatiegebruiken_vestigingserkenningen rov
                         on rov.onderwijslocatiecode = ol.onderwijslocatiecode
    --and rov.einddatum is null
         left outer join mbo_aantallen_materialized as mbo_aantallen on mbo_aantallen.onderwijslocatie = ol.onderwijslocatiecode
         left outer join po_aantallen_materialized as po_aantallen on po_aantallen.vestigingsnummer = rov.vestigingscode
         left outer join vo_aantallen_materialized as vo_aantallen on vo_aantallen.vestigingsnummer = rov.vestigingscode
         left outer join ho_aantallen_materialized as ho_aantallen on rov.vestigingscode like ho_aantallen.brin || '%'
         left outer join wo_aantallen_materialized as wo_aantallen on rov.vestigingscode like wo_aantallen.brin || '%'
where ol.plaatsnaam = 'Assen' -- ###########################
group by oa.naam
       , oa.onderwijsaanbiederid
       , ol.straatnaam
       , ol.huisnummer
       , ol.huisnummertoevoeging
       , ol.postcode
       , ol.plaatsnaam
       , ol.gps_latitude
       , ol.gps_longitude
       , ol.onderwijslocatiecode
       , rov.onderwijslocatiecode


drop index if exists olg_idx;
create unique index olg_idx on onderwijslocatiegebruiken (onderwijslocatiecode, onderwijsbestuurid, uitbedrijfdatum);
drop index if exists oa_idx;
create index oa_idx on onderwijsaanbieders (onderwijsaanbiederid, naam, einddatum_periode);
drop index if exists ol_idx;
create unique index ol_idx on onderwijslocaties (onderwijslocatiecode, gps_latitude, gps_longitude, plaatsnaam, straatnaam, huisnummer, huisnummertoevoeging, postcode)
drop index if exists ob_idx;
create index ob_idx on onderwijsbesturen (onderwijsbestuurid, naam);
drop table if exists aangeboden_opleidingen_materialized;
create table aangeboden_opleidingen_materialized as
select onderwijsaanbiederid, onderwijslocatiecode, sources
from aangeboden_opleiding
group by onderwijslocatiecode;
drop index if exists ao_idx;
create unique index ao_idx on aangeboden_opleidingen_materialized (onderwijslocatiecode, onderwijsaanbiederid, sources);

drop index if exists roa_idx;
create index roa_idx on relaties_onderwijsbesturen_onderwijsaanbieders (onderwijsaanbiederid, onderwijsbestuurid);
drop index if exists rov_idx;
create index rov_idx on relaties_onderwijslocatiegebruiken_vestigingserkenningen (onderwijslocatiecode);




-- locatie
-- grootte  (leerling aantallen) : student_count
-- onderwijsniveau : education_level
-- EDUCATION_LEVEL = dict(
--     bo="Basis onderwijs",
--     po="Praktijk onderwijs",
--     lwoo="LWOO",
--     bb="VMBO Basis beroeps",
--     bk="VMBO Kader beroeps",
--     gl="VMBO Gemende leerweg",
--     tl="VMBO theoretische leerweg",
--     havo="HAVO",
--     vwo="VWO",
--     gym="Gymnasium",
-- )
-- onderwijstype : education_type
-- EDUCATION_TYPE = dict(r="Regulier onderwijs", s="Speciaal onderwijs")
-- EDUCATION_SECTOR = dict(
--     po="Primair onderwijs",
--     so="Speciaal onderwijs",
--     vo="Voortgezet onderwijs",
--     vso="Voortgezet speciaal onderwijs",
--     mbo="Middelbaar beroeps onderwijs",
--     hbo="Hoger beroeps onderwijs",
--     wo="Wetenschappelijk onderwijs",
-- )
;

select *
from vo_aantallen_bron

select sources, count(*)
from edwh_onderwijs;
locaties
group by sources
-- where sources like '%,%'

-- ################### op jacht naar brin codes:
select count(distinct onderwijslocatiecode)
from relaties_onderwijslocatiegebruiken_vestigingserkenningen --where vestigingscode like '25PW%' and einddatum is null
select *
from vestigingserkenningen
where vestigingscode like '25PW%'
  and einddatum is null
;
select *
from sqlite_master
where sql like '%bevoegd%' -- zo heet de brincode vaak, maar niet de organisatie brincode, alleen vestigingsbrincodes worden gebruikt; een goeie is waar ik nog naar zoek, want als ik nu filter, houd ik nog maar 56 scholen over, en dat is wat krap.
;

select *
from leerlingen_po_per_vestiging;
select distinct schooljaar
from leerlingen_vo_per_vestiging;


select onderwijslocatiecode, naam, straatnaam || ' ' || huisnummer, postcode, plaatsnaam, vestiging_brins
from edwh_onderwijslocaties
where 1 = 1
  and naam like '%%'
  and straatnaam like '%Zijpendaalseweg%'
  and plaatsnaam like '%%'
order by naam, plaatsnaam, 3;


select vestigingscode, count(*)
from relaties_onderwijslocatiegebruiken_vestigingserkenningen
group by vestigingscode
having count(vestigingscode) > 1;

select *
from relaties_onderwijslocatiegebruiken_vestigingserkenningen
where vestigingscode = '01QH01'

select *
from edwh_onderwijslocaties
where vestiging_brins like '%01QH01%'

select *
from onderwijslocaties
where onderwijslocatiecode = '107X388'

select *
from relaties_onderwijslocatiegebruiken_vestigingserkenningen
where onderwijslocatiecode = '102X202'
select *
from relaties_onderwijsbesturen_onderwijsaanbieders
where onderwijsbestuurid = '104B819'

select *
from onderwijslocatiegebruiken
where onderwijslocatiecode = '107X388'

select *
from sqlite_master
where sql like '%oie_code%'

select *
from ho_onderwijslicenties

select *
from onderwijsinstellingserkenningen

select *
from relaties_onderwijsaanbieders_onderwijsinstellingserkenningen

select *
from relaties_onderwijsinstellingserkenningen_vestigingserkenningen
where einddatum is null

create view wo_aantallen as
select brin_nummer_actueel                                                                 as brin,
       round(sum(case when jaar_2022 = '<5' then 2.5 else cast(jaar_2022 as integer) end)) as aantal_2022,
       round(sum(case when jaar_2021 = '<5' then 2.5 else cast(jaar_2021 as integer) end)) as aantal_2021,
       round(sum(case when jaar_2020 = '<5' then 2.5 else cast(jaar_2020 as integer) end)) as aantal_2020,
       round(sum(case when jaar_2019 = '<5' then 2.5 else cast(jaar_2019 as integer) end)) as aantal_2019
from wo_aantallen_bron
group by brin_nummer_actueel


select onderwijslocatie, aantal_hoofdinschrijvingen as aantal
from mbo_aantallen_bron

select vestigingsnummer, totaal_aantal_leerlingen as aantal, *
from vo_aantallen_bron


select brinnummer || po_aantallen_bron.vestigingsnummer                                                as vestigingsnummer,
       round(sum(case when leerlingen_2022 = '<5' then 2.5 else cast(leerlingen_2022 as integer) end)) as aantal_2022,
       round(sum(case when leerlingen_2021 = '<5' then 2.5 else cast(leerlingen_2021 as integer) end)) as aantal_2021,
       round(sum(case when leerlingen_2020 = '<5' then 2.5 else cast(leerlingen_2020 as integer) end)) as aantal_2020,
       round(sum(case when leerlingen_2019 = '<5' then 2.5 else cast(leerlingen_2019 as integer) end)) as aantal_2019
from po_aantallen_bron
group by brinnummer, vestigingsnummer

select *
from edwh_onderwijslocaties
where plaatsnaam = 'Assen'


create view po_aantallen as
select brinnummer || po_aantallen_bron.vestigingsnummer                                                as vestigingsnummer,
       round(sum(case when leerlingen_2022 = '<5' then 2.5 else cast(leerlingen_2022 as integer) end)) as aantal_2022,
       round(sum(case when leerlingen_2021 = '<5' then 2.5 else cast(leerlingen_2021 as integer) end)) as aantal_2021,
       round(sum(case when leerlingen_2020 = '<5' then 2.5 else cast(leerlingen_2020 as integer) end)) as aantal_2020,
       round(sum(case when leerlingen_2019 = '<5' then 2.5 else cast(leerlingen_2019 as integer) end)) as aantal_2019
from po_aantallen_bron
group by brinnummer, vestigingsnummer
;


select *
from po_aantallen

select *
from edwh_onderwijslocaties


select *
from onderwijslocaties
where onderwijslocatiecode = '102X202'

select *
from onderwijsbesturen
where onderwijsbestuurid = '100B490'

select v.*
from ho_onderwijslicenties hol
         inner join relaties_onderwijsinstellingserkenningen_vestigingserkenningen rov
                    on rov.oie_code = hol.oie_code and rov.einddatum is null
         inner join vestigingserkenningen v on rov.vestigingscode = v.vestigingscode and v.einddatum is null
where hol.einddatum is null


select *
from ho_aantallen_bron
group by gemeentenaam, brin_nummer_actueel
having count(gemeentenaam || brin_nummer_actueel) > 1


select bevoegd_gezag_nummer,
       brinnummer || vestigingsnummer                                                                  as vestigingsnummer,
       round(sum(case when leerlingen_2022 = '<5' then 2.5 else cast(leerlingen_2022 as integer) end)) as aantal_2022,
       round(sum(case when leerlingen_2021 = '<5' then 2.5 else cast(leerlingen_2021 as integer) end)) as aantal_2021,
       round(sum(case when leerlingen_2020 = '<5' then 2.5 else cast(leerlingen_2020 as integer) end)) as aantal_2020,
       round(sum(case when leerlingen_2019 = '<5' then 2.5 else cast(leerlingen_2019 as integer) end)) as aantal_2019
from po_aantallen_bron
group by bevoegd_gezag_nummer, brinnummer, vestigingsnummer;


create index versnel_leerlingen_po_per_vestiging on leerlingen_po_per_vestiging (brinnummer, vestigingsnummer, peiljaar)

drop index versnel_leerlingen_po_per_vestiging

explain query plan
    select vestigingsnummer, brinnummer, max(peiljaar) as peiljaar
                           from leerlingen_po_per_vestiging
                           group by vestigingsnummer, brinnummer

select * from leerlingen_po_per_vestiging;

select * from leerlingen_vo_per_vestiging;

create view recente_tellingen_po_per_verstiging as
with
zoek_max_leerjaar as (select vestigingsnummer, brinnummer, max(peiljaar) as peiljaar
                           from leerlingen_po_per_vestiging
                           group by vestigingsnummer, brinnummer)
,per_jaar_per_org as (select brinnummer, peiljaar, sum(aantal_leerlingen) as aantal_leerlingen
                 from leerlingen_po_per_vestiging
                 group by brinnummer, peiljaar)
select
    main.brinnummer
    ,main.brinnummer ||  substring(('00' || cast(main.vestigingsnummer as integer)), length('00' || cast(main.vestigingsnummer as integer))+1-2) as vestigingsnummer
     , group_concat(distinct main.type_po)                                                          as types
     , sum(main.aantal_leerlingen)                                                                  as aantal_leerlingen_per_vestiging
     , per_org.aantal_leerlingen                                                               as aantal_leerlingen_per_organisatie
     , main.peiljaar
from leerlingen_po_per_vestiging main
         inner join zoek_max_leerjaar
                    on zoek_max_leerjaar.vestigingsnummer = main.vestigingsnummer
                        and zoek_max_leerjaar.brinnummer = main.brinnummer
                        and zoek_max_leerjaar.peiljaar = main.peiljaar
         inner join per_jaar_per_org per_org
                    on per_org.brinnummer = main.brinnummer
                           and per_org.peiljaar = main.peiljaar
-- where main.brinnummer = '02CV'
group by main.brinnummer, main.vestigingsnummer, per_org.brinnummer, per_org.peiljaar

select *
from leerlingen_po_per_vestiging
where brinnummer = '03EH'

select
    main.brinnummer
    ,main.brinnummer ||  substring(('00' || cast(main.vestigingsnummer as integer)), length('00' || cast(main.vestigingsnummer as integer))+1-2) as vestigingsnummer
    , length('00' || cast(main.vestigingsnummer as integer))+1-2
     , group_concat(distinct main.type_po)                                                          as types
     , sum(main.aantal_leerlingen)
from leerlingen_po_per_vestiging main
group by main.brinnummer, main.vestigingsnummer



select * from vo_aantallen_bron;


with per_org  as (
    select
        brin_nummer,
        sum(cast(totaal_aantal_leerlingen as integer)) as leerlingen
    from vo_aantallen_bron
    group by brin_nummer
)
select
    main.brin_nummer as brinnummer,
    main.totaal_aantal_leerlingen as aantal_leerlingen_per_vestiging,
    per_org.leerlingen as aantal_leerlingen_per_organisatie
from vo_aantallen_bron main
    inner join per_org on main.brin_nummer = per_org.brin_nummer
