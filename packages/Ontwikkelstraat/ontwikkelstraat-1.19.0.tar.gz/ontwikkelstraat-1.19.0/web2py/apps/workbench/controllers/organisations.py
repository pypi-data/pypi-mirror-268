# -*- coding: utf-8 -*-
import re
import typing

import edwh.core.web2py_tools
from edwh.core.backend.engine import OrganisationPriority, update_effectivedated

# from edwh.core.web2py_tools import effective_dated_grid, hide
from edwh_web2py_effdted_prio_grid import effective_dated_grid, hide
from gluon.tools import prettydate

if typing.TYPE_CHECKING:
    from gluon import URL, auth, redirect, request, session, response
    from gluon.html import PRE, SPAN, TT, XML, A
    from gluon.sqlhtml import SQLFORM
    from pydal import Field
    from pydal.validators import IS_MATCH

    from ..models.db import (
        database,
        is_admin,
        is_eddie,
        is_minion,
        last_opened_warning,
        organisation_priority_level,
    )
    from ..models.db_z_backend import backend
    from ..models.menu import without_none


@auth.requires(is_eddie or is_minion)
def boards():
    database.board.id.readable = False
    database.board.gid.writable = False
    database.board.postalcode.requires = IS_MATCH("\d{4} [a-zA-Z]{2}")

    def onvalidation(form):
        form.vars.last_saved_when = request.now
        form.vars.last_saved_by = auth.user.email

    grid = SQLFORM.grid(
        database.board,
        exportclasses=dict(
            xml=False,
            html=False,
            json=False,
            tsv=False,
            tsv_with_hidden_cols=False,
            csv_with_hidden_cols=False,
        ),
        deletable=is_admin,
        advanced_search=is_admin,
        maxtextlength=50,
        onvalidation=onvalidation,
    )
    return dict(form=grid)


ORG_GID = "e5b80b90-1851-42d9-aebc-87327e87ed09"

KomootData = typing.TypedDict("KomootData", {
    "lonlat": str,
    "number": str,
    "street": str,
    "postalcode": str,
    "city": str,
})


def load_geo(street: str,
             number: str,
             postalcode: str,
             city: str, country="Netherlands"
             ) -> KomootData:
    import httpx
    result: KomootData = {}

    resp = httpx.get(
        f"https://photon.komoot.io/api/?q={street}+{number}+{postalcode}+{city}+'{country}'",
        headers={
            "User-Agent": "EducationWarehouse workbench (httpx python), thanks for saving us time!"
        },
        timeout=10,
    )

    print(resp.json())
    if resp.is_success:
        js = resp.json()
        try:
            if not js["features"]:
                raise KeyError("geen succes")

            # save in swapped version for database
            result['lonlat'] = "({0},{1})".format(
                *js["features"][0]["geometry"]["coordinates"]
            )
            print("lonlat set:", result['lonlat'])
        except KeyError as e:
            print(e)
            response.flash = "Geocoordinaten konden niet geladen worden voor het gegeven adres."
        try:
            if js["features"]:
                features = js["features"][0]
                properties = features["properties"]

                result["street"] = properties["street"]
                result["number"] = properties["housenumber"]
                result["postalcode"] = properties["postcode"]
                result["city"] = properties["city"]
        except KeyError as e:
            print(e)
    else:
        print(resp.content)
        response.flash = (
            "Geocoordinaten konden niet geladen worden voor het gegeven adres."
        )

    return result


@auth.requires(is_eddie or is_minion)
def index():
    warning = last_opened_warning("org")

    mdash = XML("&mdash;")
    organisation = database.organisation
    organisation.id.readable = False

    # organisation.gid.represent = lambda x, row: PRE(x)
    # organisation.gid.writable = False
    organisation.gid.widget = edwh.core.web2py_tools.ReadonlyWidget

    organisation.country_code.represent = lambda x, row: x if x else mdash
    organisation.aka.represent = lambda x, row: TT(x) if x else mdash
    organisation.validated_by.represent = (
        lambda x, row: (x.split("@")[0] if "@educationwarehouse.nl" in x else x)
        if x
        else mdash
    )
    organisation.validated_ts.represent = (
        lambda x, row: f"{x.date()} ({prettydate(x)})" if x else mdash
    )

    def tag_represent(tag, row):
        result = mdash
        error = False
        if not tag:
            error = True
            result = "X"
        # controleer of de tagnaam gelijk is aan de doopnaam + plaats
        # de plaats die we eerder gebruikten is dan irrelvant omdat een andere locatie binnen dezelfde plaats
        # een andere roeopnaam zal hebben. (quintus/penta vs Nassau ...)
        elif tag != str(row.aka if "aka" in row else row.organisation.aka) + " " + str(
            row.city if "city" in row else row.organisation.city
        ):
            error = True
            result = "?"
        if error:
            return SPAN(result, _style="color:RED")
        return result

    database.tag.name.represent = tag_represent
    database.tag.name.label = "Tag-status"
    organisation.name.represent = lambda name, row: TT(name)
    # database.organisation.name.represent = lambda name, row: A(
    #     name,
    #     _class="btn button btn-primary",
    #     _href=URL(f="quick_edit", args=(row.organisation.gid,)),
    # )
    fields = [
        organisation.effdt,
        organisation.validated_ts,
        organisation.validated_by,
        database.tag.name,
        organisation.aka,
        organisation.name,
        organisation.city,
        organisation.postalcode,
        # database.organisation.gid,
    ]
    # fields = [
    #     organisation.effdt,
    #     organisation.prio,
    #     organisation.country_code,
    #     organisation.city,
    #     organisation.postalcode,
    #     organisation.aka,
    #     organisation.name,
    #     organisation.validated_ts,
    #     organisation.validated_by,
    #     organisation.brin,
    # ]
    orderby = (
        ~organisation.effdt,
        # database.organisation.city,
        # database.organisation.name,
        # database.organisation.id,
    )
    left = database.tag.on(
        (organisation.tag_gid == database.tag.gid) & (database.tag.deprecated == False)
    )
    # rows = database(query).select(*fields, orderby=orderby, left=left)
    # form = SQLTABLE(rows, truncate=100)
    # https://github.com/web2py/web2py/blob/c2ed5016e161430ecb020ddc96b16a6e5dde0e2e/gluon/sqlhtml.py#L2248
    # http://www.web2py.com/books/default/chapter/29/07/forms-and-validators#SQLFORM-grid
    if is_minion:
        hide(organisation.brin)
        hide(organisation.vestigingscode)
        hide(organisation.platform)
        hide(organisation.correspondence_city)
        hide(organisation.correspondence_street)
        hide(organisation.correspondence_number)
        hide(organisation.correspondence_postalcode)
        hide(organisation.correspondence_country)
        hide(organisation.country_code)
        hide(organisation.scholen_op_de_kaart_url)
        hide(organisation.sector)
        hide(organisation.education_level)
        hide(organisation.education_type)
        hide(organisation.denomination)
        hide(organisation.so_cluster)
        hide(organisation.so_type)
        hide(organisation.concept)
        hide(organisation.prio)
        hide(organisation.effstatus)

        # explicitly add comments to each field from the organisation table
        organisation.name.comment = "Dit is de naam van de school zoals bekend bij DUO. Hier hoef je niks aan te doen."
        organisation.student_count.comment = "De hoeveelheid leerlingen op deze school"
        organisation.aka.comment = "Dit is de naam van de school die mensen gebruiken als ze het over de school hebben. Dit kun je vinden in de lopende tekst op de website van de school."
        organisation.coc.comment = "Als je het Kvk-nummer van de school niet kunt vinden, vul dan het KvK-nummer van het schoolbestuur in."
        organisation.coc_location.comment = "Als je het vestgingsnummer van de school niet kunt vinden, vul dan het vestigingsnummer van het schoolbestuur in."
        organisation.quality_assurance_plan.comment = "Hier vul je de URL van de pagina in waarop het schoolplan te vinden is. Dit is altijd een pagina op de schoolwebsite. Als je het schoolplan niet kunt vinden, dan vul je de URL naar de schoolgids in."

    organisation.board_gid.widget = SQLFORM.widgets.autocomplete(
        request,
        database.board.name,
        db=database,
        id_field=database.board.gid,
        orderby=database.board.name,
        at_beginning=False,
        help_fields=[database.board.name, database.board.city],
        help_string="%(name)s (%(city)s)",
    )
    organisation.board_gid.comment = "Zoek op naam van een bestuur."

    # organisation.tag_gid.widget = SQLFORM.widgets.autocomplete(
    #     request,
    #     database.tag.name,
    #     db=database,
    #     id_field=database.tag.gid,
    #     orderby=database.tag.name,
    #     at_beginning=False,
    #     help_fields=[database.tag.name],
    #     help_string="%(name)s",
    #     limitby=None,
    # )
    organisation.tag_gid.widget = edwh.core.web2py_tools.HTMXAutocompleteWidget(
        request,
        database.tag.name,
        database.tag.gid,
        query=database.tag.parents.contains(ORG_GID),
    )

    def onvalidation(form):
        if (
            (form.vars.street and form.vars.number and form.vars.city)
            or (form.vars.number and form.vars.postalcode)
        ) and not form.vars.lonlat:
            geo_data = load_geo(form.vars.street, form.vars.number, form.vars.postalcode, form.vars.city)
            form.vars.update(geo_data)
        if form.vars.lonlat:
            import geopy.distance
            import geopy.point

            try:
                lon, lat = form.vars.lonlat.strip().strip("()").split(",")
                lon, lat = float(lon), float(lat)
                point = geopy.point.Point(lat, lon)
                if point.latitude < point.longitude:
                    # reverse lon lat
                    # we save it as longitude latitude for geospatial functions,
                    # but the world uses it latitude, longitude
                    point = geopy.point.Point(point.longitude, point.latitude)
                form.vars.lonlat = f"({point.longitude},{point.latitude})"
            except Exception as e:
                print(e)
                form.errors.lonlat = str(e) + "," + str(form.vars.lonat)

        if tag_gid := form.vars.tag_gid:
            if isinstance(tag_gid, list) and len(tag_gid) > 1:
                form.errors.tag_gid = "Kies maximaal één tag."

    def upper(value: typing.Optional[str]) -> str:
        return value.upper() if value else ""

    form = effective_dated_grid(
        organisation,
        use_prio=organisation_priority_level,
        keyfieldname="gid",
        fields=fields,
        archive_fields=organisation.fields,
        left=left,
        orderby=orderby,
        searchable=True,
        advanced_search=False,
        details=False,
        create=is_eddie,
        maxtextlength=100,
        paginate=200,
        onvalidation=onvalidation,
        exportclasses=dict(
            xml=False,
            html=False,
            json=False,
            tsv=False,
            tsv_with_hidden_cols=False,
            csv_with_hidden_cols=False,
        ),
        links=without_none(
            [
                dict(
                    header="Valideer",
                    body=lambda row: A(
                        "Valideer",
                        _class="button btn btn-primary",
                        _href=URL(
                            f="validate",
                            args=(
                                row.gid
                                if "gid" in row
                                else row.organisation_effdted_now.gid
                            ),
                        ),
                    ),
                ),
                dict(
                    header="Hernoem tag",
                    body=lambda row: A(
                        "Hernoem tag",
                        _class="button btn btn-primary",
                        _tile=f"Hernoem naar {row.aka} {upper(row.city)}",
                        _href=URL(
                            f="rename_tag",
                            args=(row.tag_gid,),
                            vars=dict(new_name=f"{row.aka} {upper(row.city)}"),
                        ),
                    ),
                )
                if is_eddie
                else None,
                dict(
                    header="Zoek Basis scholen",
                    body=lambda row: A(
                        "Zoek basisschool",
                        _class="button btn btn-primary",
                        _tile=f"Zoek naar {row.aka} {upper(row.city)}",
                        _href=f"https://scholenopdekaart.nl/zoeken/basisscholen?zoektermen={row.aka if row.aka else row.name} {upper(row.city)}&weergave=Lijst",
                        _target="new",
                    ),
                )
                if is_admin
                else None,
                dict(
                    header="Zoek Middelbare scholen",
                    body=lambda row: A(
                        "Zoek Middelbare scholen",
                        _class="button btn btn-primary",
                        _tile=f"Zoek naar {row.aka} {upper(row.city)}",
                        _href=f"https://scholenopdekaart.nl/zoeken/middelbare-scholen?zoektermen={row.aka if row.aka else row.name} {upper(row.city)}&weergave=Lijst",
                        _target="new",
                    ),
                )
                if is_admin
                else None,
            ]
        ),
        links_in_grid=False,  # alleen in details
        buttons_placement="left",
        links_placement="left",
    )
    return dict(warning=warning, form=form)
    # return dict(form=database(~database.user.password.like("$2a%")).select())


@auth.requires(is_eddie)
def rename_tag():
    # catch request.args as (gid, name), but also (gid, name HAVO/VWO)
    new_name = request.vars.new_name.strip()
    tag_gid = request.args[0]
    if rows := database(database.tag.name.lower() == new_name.lower()).select():
        return f"Fout, tag '{new_name}' bestaat al met gids: {[t.gid for t in rows]} "
    database.tag(gid=tag_gid).update_record(name=new_name)
    database.commit()
    return """
    <html>
    <script>
      window.history.go(-1)
    </script>
    </html>
    """


@auth.requires(is_eddie)
def quick_create():
    form = SQLFORM.factory(
        Field(
            "name",
            "string",
            label="Naam",
            comment="Organisatie naam",
        )
    )

    if form.process().accepted:
        name = form.vars.name
        # dit is meer een placeholder, omdat de GraphQL een short description vereist.
        short_description = "Begin hier met het schrijven van een ontwikkelpraktijk..."

        new_org_gid = backend.add_organisation(name=name)
        return redirect(URL("quick_edit", args=[new_org_gid]))

    return dict(form=form)


@auth.requires(is_eddie)
def quick_edit():
    database.organisation.gid.writable = False
    database.organisation.gid.represent = lambda x: PRE(x)
    org_gid = request.args[0]
    record = database.organisation(gid=org_gid)
    form = SQLFORM(
        database.organisation,
        record=record,
        deletable=False,
        submit_button="Update",
    )
    if form.process().accepted:
        backend.invalidate("organisation", org_gid)
        session.flash = "Success!"
        redirect(URL(args=request.args))
    return dict(form=form, org_gid=org_gid)


@auth.requires(is_eddie or is_minion)
def validate():
    org_gid = request.args[0]

    update_effectivedated(
        db=database,
        table=database.organisation,
        where=database.organisation.gid == org_gid,
        values=dict(validated_ts=request.utcnow, validated_by=auth.user.email),
        last_saved_by=auth.user.email,
        prio=OrganisationPriority.MINION if is_minion else OrganisationPriority.EDDIE,
    )
    redirect(URL(f="index"))
