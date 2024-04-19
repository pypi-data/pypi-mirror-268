import collections


def width_first_tree_sort(tag_list):
    # robin en remco hebben hun hoofd gebogen over deze functie, om met zo min mogelijk overhead
    # en zonder recursie een tag_list zo te sorteren dat alle parents voor hun children in de lijst staan.
    # Dit gebeurt met een bag model: zolang er nog tags te verwerken zijn, worden ze uitgezocht en verwerkt.
    # een tag wordt pas uit de bag verwijderd als de parents al opgenomen zijn, zodat een verwijzing naar
    # niet bestaande parents niet mogelijk is.
    # om oneindige loops te voorkomen (bijvoorbeeld omdat er verwezen wordt naar een niet bestaande parent)
    # wordt er een value error gegenereerd. Deze is op dit moment nog niet erg verbose, dus er zit geen troubleshooter
    # bij. Dit kan wel toegevoegd worden.
    # todo(nice-to-have): troubleshoot value bij de infinite loop detectie van de waarde(n) die fouten opleveren.

    # dest bevat straks alle items op volgorde.
    # dit maakt gebruik van python3's functie dat een dictionary insert order behoudt.
    dest = {}
    # source wordt een shallow copy van de tag_list. source is de bag en wordt telkens verkleind.
    source = tag_list[:]
    # previous_source_length is de lengte zodat een constante lengte te constateren is
    previous_source_length = -1
    while source:
        # zolang er nog items in source zitten, moeten we door

        # de huidige lengte bepalen
        current_source_length = len(source)

        # bij een volgende loop is de index van een tag in source 0
        # telkens als er een tag verwijderd wordt, blijft de index in source gelijk van het volgende item in source.copy(),
        # maar mocht er een tag zijn die we niet kunnen vewerken, verhogen we de source_index
        # omdat het volgende item 1 verder is in de source (die effectief dus niet verkort)
        source_index = 0
        for tag in source.copy():
            # ga alle tags in een copy van source bijlangs.
            # de kopie is bedoeld zodat we source ondertussen kunnen manipuleren (tags verwijderen)

            if any(parent not in dest for parent in tag.parents):
                # kijk of er parents zijn die nog niet voorkomen in dest,
                # ofwel, kijk of er parents zijn die later in de source gedefinieerd worden.
                # als dat zo is, dan kunnen we dit item nog niet verwerken.
                # verhoog de source_index zodat een delete bij een volgende tag, niet dit item verwijderd.
                source_index += 1
                # ga door naar de volgende tag
                continue
            else:
                # als alle parents al voorkomen in de dest, dan mag deze tag ook toegevoegd worden
                # verwijder daarmee deze tag uit de source. De index wordt niet opgehoogd, want alle indexen
                # van de andere tags worden verkleind met 1. Ofwel, de index van  de volgende tag,
                # houdt de index source_index.
                dest[tag.gid] = tag
                # verwijder de tag uit source.
                del source[source_index]

        # sentinal loop
        if previous_source_length == current_source_length:
            # tijd voor gekte
            raise HTTP(508, "Infinite Loop Detected: " + repr(source))

        # onthoud de huidige als de laatste en begin opnieuw
        previous_source_length = current_source_length
    return list(dest.values())


class TagTree:
    def __init__(
        self,
        drag_root: bool = False,
        checkbox: bool = True,
        sort: bool = True,
        search: bool = True,
        wholerow: bool = True,
        drag_n_drop: bool = False,
        move_to_root: bool = False,
        show_user_generated_tags: bool = True,
        selected_tag_gids: list = None,
        save_url: str = None,
        _id: str = "tag_tree",
        _class: str = "tag-tree",
    ):
        """
        Tree 'widget' voor het beheren van tags. Door een item_id mee te geven kun je gemakkelijk
        de item_tags van een item aanpassen.

        :param _id: id attribuut van de html.
        :param _class: class attribuut van de html.
        :param item_id: id van het item waarvan je de item_tags aan wilt passen.
        :param drag_root: om aan te geven of een root node versleept mag worden, werkt alleen als de dnd plugin aan staat.
        :param checkbox: om aan te geven of de checkbox plugin gebruikt mag worden.
        :param sort: om aan te geven of de sort plugin gebruikt mag worden.
        :param wholerow: om aan te geven of de wholerow plugin gebruikt mag worden.
        :param: allow_move_to_root: om aan te geven of een child een root element mag worden.
        :param save_url: de URL waar de Ajax call van de save knop naar toe gaat.
        """
        self.drag_parent = drag_root
        self.drag_n_drop = drag_n_drop
        self.checkbox = checkbox
        self.sort = sort
        self.search = search
        self.wholerow = wholerow
        self.allow_move_to_root = move_to_root
        self.save_url = save_url
        self.show_user_generated = show_user_generated_tags
        self.selected_tag_gids = selected_tag_gids or []

        self.data = self.tags()
        self.plugins = self.setup_plugins()
        self.settings = self._settings()
        self._id = _id
        self._class = _class

    def tree(self):
        # TODO: wellicht een andere aanpak, maar voor nu werkt dit.
        #       note van Robin: ik vind dit erg onleesbaar en cursed

        container = DIV()

        settings = self.settings
        _tree = XML(f".jstree({settings})")
        if self.drag_n_drop and not self.allow_move_to_root:
            _tree = XML(
                ".on('move_node.jstree', function(e, data){console.log(movedNodes); if(data.parent === '#')"
                "{data.instance.move_node(data.node.id, data.old_parent);"
                "alert('Je kunt geen nieuwe root nodes aanmaken.');}"
                "else if (data.old_parent !== data.parent){"
                "if (data.node.id in movedNodes){movedNodes[data.node.id].new_parent = data.parent;}"
                "else{movedNodes[data.node.id] = {'new_parent': data.parent, 'old_parent': data.old_parent};}}})%s"
                % _tree
            )
        _tree = """
                        <script>

                            function saveTree(){
                                $.ajax({
                                    type: 'POST',
                                    url: '%s',
                                    data: {'data': JSON.stringify(movedNodes)},
                                    dataType: 'json',
                                })
                            }

                            var movedNodes = {};
                            var divId = '#%s';
                            $(divId).on('select_node.jstree', function (e, data) {
                                if (data.node.children.length > 0) {
                                    $(divId).jstree(true).deselect_node(data.node);
                                    $(divId).jstree(true).toggle_node(data.node);
                                }
                            })%s;
                        </script>""" % (
            self.save_url,
            self._id,
            _tree,
        )

        _tree = DIV(XML(_tree), _id=self._id, _class=self._class)
        container.append(_tree)
        if not self.checkbox:
            container.append(
                DIV(
                    "Houdt CTRL ingedrukt tijdens het slepen om een tag te kopiëren.",
                    _class="text-muted",
                )
            )

        if self.save_url:
            container.append(
                self.button(
                    "Opslaan",
                    onclick="saveTree();",
                    _id="save_tree_button",
                )
            )

        return container

    def button(
        self,
        text,
        onclick="",
        _id="tag_tree_button",
        _class="tag_tree_btn btn btn-sm btn-info",
    ):
        return BUTTON(text, _onclick=onclick, _id=_id, _class=_class)

    def _settings(self):
        """Levert een dictionary op met configuratie voor de JSTree

        :return: dict
        """

        _config = dict(core={}, checkbox={}, dnd={}, search={}, plugins=[])
        _config["core"]["data"] = self.data
        _config["core"]["check_callback"] = XML("true")
        _config["core"]["expand_selected_onload"] = XML("false")

        if not self.drag_n_drop:
            # om onnodige keys in de dictionary te voorkomen
            del _config["dnd"]
        if not self.drag_parent and self.drag_n_drop:
            # als een parent niet gesleept mag worden, dan voegen we een script toe aan de config van de drag and drop
            # configuratie. dit script zorgt ervoor dat een parent node niet gesleept mag worden.
            _config["dnd"]["is_draggable"] = XML(
                "function (node) {if (node[0].parent === '#'){return false;} if (node[0].children.length) {return false;} return true;}"
            )
        if self.search:
            _config["search"]["show_only_matches"] = XML("true")
        if self.checkbox:
            _config["checkbox"]["three_state"] = XML("false")
        else:
            # om onnodige keys in de dictionary te voorkomen.
            del _config["checkbox"]

        _config["plugins"] = self.plugins
        return _config

    def setup_plugins(self):
        """Maakt een lijst van plugins a.d.h.v. argumenten van TagTree

        :return: lijst van plugins
        """
        plugins = []
        if self.checkbox:
            plugins.append("checkbox")
        if self.drag_n_drop:
            plugins.append("dnd")
        if self.wholerow:
            plugins.append("wholerow")
        if self.sort:
            plugins.append("sort")
        if self.search:
            plugins.append("search")
        return plugins

    def create_node(
        self,
        _id: str,
        parent: str,
        text: str,
        has_children: bool,
        selectable: bool,
        selected: bool = False,
        disabled: bool = False,
        extra_state=None,
        extra_a_attr=None,
        description=None,
    ):
        icon = "glyphicon glyphicon-tags" if has_children else "glyphicon glyphicon-tag"
        attributes = {"class": "no-checkbox"} if not selectable else {}
        if extra_a_attr:
            attributes.update(extra_a_attr)
        if description:
            attributes["title"] = description
        state = {}
        if disabled:
            state["disabled"] = XML("true")
        if selected:
            state["selected"] = XML("true")
        if extra_state:
            state.update(extra_state)
        return dict(
            id=_id, parent=parent, text=text, icon=icon, state=state, a_attr=attributes
        )

    def tags(self):
        """Levert alle tags in JSON format aan. Dit is nodig voor de JSTree.

        https://www.jstree.com/docs/json/
        {
          id          : "string" // required
          parent      : "string" // required
          text        : "string" // node text
          icon        : "string" // string for custom
          state       : {
            opened    : boolean  // is the node open
            disabled  : boolean  // is the node disabled
            selected  : boolean  // is the node selected
          },
          li_attr     : {}  // attributes for the generated LI node
          a_attr      : {}  // attributes for the generated A node
        }
        """
        # tags om helemaal niet mee te nemen in de select statement.
        ITEM_GID = "fc8a7d36-e23e-4aba-8ee9-f5269ecc8dfc"
        SYSTEM_GID = "19682a99-50a3-4fc0-bb67-e0f6eff5da55"
        excluded_gids = [ITEM_GID]

        query = ~database.tag.gid.belongs(excluded_gids)
        query &= database.tag.deprecated == False
        nodes = database(query).select(orderby=database.tag.parents)

        items_per_tag_gid = collections.Counter()
        for item in database(
            (database.item.platform == "SvS") & (database.item.author != None)
        ).select(database.item.gid, database.item.tags):
            for tag in item.tags:
                items_per_tag_gid[tag] += 1
        # de join van de items aan de tags zou in de database kunnen,
        # maar omdat deze nu nog via een web2py lists gecontructie gaat is die lookup
        # belachelijk graag. een ilike '%|' || tag.gid || '|%' is niet bevorderlijk.
        # nodes = database(query).select(
        #     database.tag.gid,
        #     database.tag.name,
        #     database.tag.description,
        #     database.tag.children,
        #     database.tag.meta_tags,
        #     database.item.gid.count(),
        #     left=database.item.on(database.item.tags.contains(database.tag.gid)),
        #     groupby=(
        #         database.tag.gid,
        #         database.tag.name,
        #         database.tag.description,
        #         database.tag.children,
        #         database.tag.meta_tags,
        #     ),
        # )
        # explain plan:
        # HashAggregate  (cost=325477.45..325567.24 rows=8979 width=199)
        # "  Group Key: tag.gid, tag.name, tag.description, tag.children, tag.meta_tags"
        #   ->  Nested Loop Left Join  (cost=0.00..324263.93 rows=80901 width=228)
        #         Join Filter: (item.tags ~~ (('%|'::text || (tag.gid)::text) || '|%'::text))
        #         ->  Seq Scan on tag  (cost=0.00..458.25 rows=8979 width=191)
        #               Filter: ((gid)::text <> 'fc8a7d36-e23e-4aba-8ee9-f5269ecc8dfc'::text)
        #         ->  Materialize  (cost=0.00..207.03 rows=1802 width=311)
        #               ->  Seq Scan on item  (cost=0.00..198.02 rows=1802 width=311)

        # item.gid as key, node dict as value
        data = []
        identifiers_per_tag_gid = collections.defaultdict(list)

        nodes = width_first_tree_sort([*nodes])

        for node in nodes:
            if node.name:
                # tag wordt gebruikt, anders is node.name leeg
                if node.parents:
                    # per node-parent combinatie, voeg een Node toe
                    for parent in node.parents:
                        _id = f"{len(data)}:{node.gid}"  # <- id moet uniek zijn maar nog wel koppelbaar aan de tag gid
                        identifiers_per_tag_gid[node.gid].append(_id)
                        # ^ gebruikt om de child tags aan de (unieke) parents te koppelen
                        data.append(
                            self.create_node(
                                _id=_id,
                                parent=identifiers_per_tag_gid[parent][0],
                                text=f"{node.name} ({items_per_tag_gid[node.gid]})",
                                has_children=bool(node.children),
                                selectable=ITEM_GID in node.meta_tags,
                                description=f"""DESC:{node.description}\nREST:{node.restrictions}\n"""
                                f"""DEF:{node.definition}\nREM:{node.remarks}""",
                                selected=node.gid in self.selected_tag_gids,
                                disabled=ITEM_GID not in node.meta_tags,
                            )
                        )
                    # de normale nodes nu niet opnieuw opbouwen, anders wordt de lijst dubbel zo lang
                    #  en staan sommige tags er 2 keer in. Waarom snap ik nog niet. Kevin?!?!
                else:
                    # root nodes hebben geen parents
                    # zoals 'Doelgroep', 'Organisations', 'System', 'Omvang', ...

                    identifiers_per_tag_gid[node.gid].append(node.gid)

                    data.append(
                        self.create_node(
                            _id=node.gid,
                            # ^  parent nodes kunnen nooit geselecteerd worden
                            # dus die hoeven niet geprefixt te worden
                            parent="#",
                            text=node.name,
                            has_children=bool(node.children),
                            description=node.description,
                            selectable=False,
                        )
                    )

        return data
