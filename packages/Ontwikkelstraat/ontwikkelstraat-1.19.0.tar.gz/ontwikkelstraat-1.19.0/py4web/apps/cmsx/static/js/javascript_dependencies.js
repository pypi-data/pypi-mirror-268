// execute hyperscript in JS in a similar way as in HTML: with _('...') vs _="..."
window._ = _hyperscript;

(function () {
    const ALLOW_DEBUG = true;
    let DEBUG = true;
    const PREFIX = "ew";

// "hack" event listeners:
    ALLOW_DEBUG &&
    (function () {
        Element.prototype._addEventListener =
            Element.prototype.addEventListener;
        Element.prototype.addEventListener = function (
            event_name,
            callback,
            options
        ) {
            // original listener:
            this._addEventListener(event_name, callback, options);

            if (!this.eventListenerList) this.eventListenerList = {};
            if (!this.eventListenerList[event_name]) {
                this.eventListenerList[event_name] = [];
                // debug listener (1 per type):
                event_name.startsWith(`${PREFIX}:`) &&
                this._addEventListener(
                    event_name,
                    (ev) => {
                        if (DEBUG) {
                            console.debug(event_name, ev.detail);
                        }
                    },
                    options
                );
            }
            this.eventListenerList[event_name].push(callback);
        };
    })();
})() // (function(){})() fixes Const scope issue

/**
 * add JSON capabilities to the Set type
 * @returns {Array}
 */
Set.prototype.toJSON = function () {
    return Array.from(this);
};

/**
 * Toggle functionality for Sets
 *
 * @param {string} el value to toggle
 * @param {boolean|undefined} action if undefined, do default toggle. if True, only add. if False, only delete
 */
Set.prototype.toggle = function (el, action = undefined) {
    if (action === undefined) this.has(el) ? this.delete(el) : this.add(el);
    else if (action) this.add(el);
    else this.delete(el);
};

// custom EDWH HTML helpers:

function edwh_html_helpers() {
    /**
     * Helper system to easily extend HTML elements with new helpers
     *
     * @param {String} name - helper name
     * @param {Function} method - helper code
     */
    const _add_helper = function (name, method) {
        // Q[name] = method;

        Element.prototype[name] =
            // Q().__proto__[name] =
            function (...a) {
                return method(this, ...a);
            };
    };

    _add_helper(
        "toggleClass",
        /**
         * Simply add/remove a class on element
         *
         * @param {HTMLElement} element
         * @param {Array|string} classes - one or more classes to toggle
         * @returns {*} ignorable
         */
        (element, classes) => element.classList.toggle(classes)
    );
    _add_helper(
        "addClass",
        /**
         * Add one or more classes to element
         * @param {HTMLElement} element
         * @param {Array|string} classes
         * @returns {*}
         */
        (element, classes) => element.classList.add(classes)
    );
    _add_helper(
        "removeClass",
        /**
         * Remove one or more classes from element
         * @param {HTMLElement} element
         * @param {Array|string} classes
         * @returns {*}
         */
        (element, classes) => element.classList.remove(classes)
    );

    _add_helper(
        "formData",
        /**
         * get the Form Data as an object from a <form> element
         * @param {HTMLFormElement} element
         * @returns {Object}
         */
        (element) => Object.fromEntries(new FormData(element))
    );

    _add_helper(
        "data",
        /**
         * Get all or one of the data- attributes of element
         * @param {HTMLElement} element
         * @param {void|string} x - leave empty to get an object of all data attributes
         * @returns {string|Object}
         */
        (element, ...x) => {
            const data = {...element.dataset};
            if (!x.length) {
                return data;
            }
            if (x[1]) {
                element.dataset[x[0]] = x[1];
            } else if (x[0]) {
                return data[x[0]];
            } else {
                throw "Invalid number of arguments (0, 1 or 2 allowed)";
            }
        }
    );

    _add_helper(
        "disable",
        /**
         * Set one or more elements to disabled
         * @param {HTMLElement|Array} element
         */
        (element) => element.forEach((element) => (element.disabled = true))
    );

    // calling it 'css' breaks _hs 0.9.4:

    _add_helper(
        "_css",
        /**
         * Set a css property on element
         * @param {HTMLElement} element
         * @param {string} property
         * @param {string} [value]
         */
        (element, property, value) => (element.style[property] = value)
    );

    _add_helper(
        "text",
        /**
         * Set the innertext of an element
         * @param {HTMLElement} element
         * @param {string} [value]
         * @returns {*}
         */
        (element, value) => {
            if (value === undefined) {
                return element.innerText;
            } else {
                element.innerText = value;
            }
        }
    );

    _add_helper(
        "html",
        /**
         * Set the innerHTML of an element
         * @param {HTMLElement} element
         * @param {string} value
         * @returns {*}
         */
        (element, value) => {
            if (value === undefined) {
                return element.innerHTML;
            } else {
                element.innerHTML = value;
            }
        }
    );

    // end helpers
}

edwh_html_helpers();

/**
 * Example usage:
 * data('tag-gid', {selector: 'a'}) to get <a tag-gid="anything">
 * data('tag-gid', {value: '56428ab5-78db-47dd-897b-a540284c7fc3'}) to get a specific tag-gid
 *
 * @param {string} attribute data-... to get
 * @param {string} [value] optional value to match
 * @param {HTMLElement} [parent] element to search in (default = everything)
 * @param {string} [selector] css selector to apply
 * @returns {NodeListOf<Element>}
 */
function data(
    attribute,
    {value = undefined, parent = undefined, selector = ""}
) {
    parent = parent || document;
    value = value ? `='${value}'` : "";
    return parent.querySelectorAll(`${selector}[data-${attribute}${value}]`);
}

/**
 * After loading the quick filter bar, set the right qf button to active
 */
function initial_qf(state) {
    // closest .edwh-state met #state als default
    state = state || document.querySelector("#state");

    const qf = state.querySelector("[name=qf]").value;

    const id = qf
        ? data("tag-gid", {selector: ".edwh-quickfilter-button", value: qf})[0]
            .id
        : "qf-btn-0";

    _(`add .is-active to #${id}`);
}

/**
 * On every ew:filters_changed (which is called by #tiles reload), set the right filters to active
 */
function activate_filters(id) {
    // first empty:
    document
        .querySelectorAll(`#filtermenu [data-tag-gid]`)
        .forEach((el) => el.removeClass("is-active"));

    const filters = json_tags({id});

    filters.forEach((el) => {
        document
            .querySelector(`#filtermenu [data-tag-gid='${el}']`)
            ?.addClass("is-active");
    });
}

/**
 * Verwijdert de oude quick filter tag uit de lijst van tags
 * en voegt de nieuwe qf er aan toe
 *
 * @param {string} old_gid
 * @param {string} new_gid
 */
function toggle_qf(old_gid, new_gid) {
    let tags;
    if (new_gid) {
        tags = new Set(json_tags());
        tags.delete(old_gid);
        tags.add(new_gid);
    } else {
        // empty
        tags = new Set();
    }

    return JSON.stringify(tags);
}

/**
 * Remove duplicate from array
 *
 * @param {array} list
 * @return {array}
 */
function unique(list) {
    return Array.from(new Set(list));
}

/**
 * Combine an array of tags (in JSON or CSV) and base tags to a unique array
 *
 * @param {string} tags
 * @param {array} base_tags
 *
 * @return {array}
 * @private
 */
function _json_tags(tags, base_tags) {
    if (!tags) {
        return base_tags;
    }
    let taglist;
    try {
        taglist = JSON.parse(tags);
    } catch {
        // not JSON, try csv
        taglist = tags.split(",");
    }

    taglist.push(...base_tags);

    return unique(taglist);
}

/**
 * Load the tags from the hidden <input> as an array
 *
 * @returns {Array}
 */
function json_tags({id = "state", base_tags = []} = {}) {
    const tags = _(`#${id}'s tags.value`);

    return _json_tags(tags, base_tags);
}

/**
 * Get the current set of tags
 *
 * @returns {Set}
 */
function get_tags(id) {
    return new Set(json_tags({id}));
}

/**
 * Push new tags to state
 *
 * @param {Set|Array} tags
 * @param {string} id .edwh-state's id
 */
function set_tags(tags, id = "state") {
    _(`set #${id}'s tags.value to ${JSON.stringify(tags)}`);
    // _(`send ew:change_state(page: 1) to closest .edwh-messagebus`);
}

/**
 * Toggle a specific tag
 * Used by StateMachine on ew:change_state
 *
 * @param {string} taggid gid of the tag to toggle
 * @param {string} state_id id of the edwh-state (used to handle multiple states)
 * @param {boolean|undefined} option action to pass to toggle (to force on/off with bool)
 * @return {boolean} whether the tags now include the new tag or not
 */
function toggle_tag(taggid, state_id, option = undefined) {
    const tags = get_tags(state_id);
    tags.toggle(taggid, option);
    set_tags(tags, state_id);
    return tags.has(taggid);
}

/**
 * Save a state object to a state <form>
 *
 * @param {HTMLFormElement} state
 * @param {Iterable|ArrayLike} settings - Object.entries of object or an array in the shape [[key, value], [key, value], ...]
 */
function state_to_form(state, settings) {
    for (let [key, value] of settings) {
        const field = state.querySelector(`[name=${key}]`);
        if (!field) continue;
        field.value = value;
        // voeg dit aan je div toe om bijv de waarde van q in te laden:
        // _="on ew:history_recovered_for_q from closest .edwh-messagebus set my value to event.detail.value"
        _(
            `send ew:history_recovered_for_${key}(value: '${value}') to closest .edwh-messagebus`
        );
    }
}

/**
 * Extract js object (dict) from state input values and vals.
 *
 * @param  {HTMLFormElement} state
 */
function state_to_obj(state) {
    return {
        ...state.formData(),
        ...htmx.expression_vars(state),
    };
}

/**
 * Get one specific value (form input or hx-val/hx-var) from state
 * Used by the _hs function 'get_state_value'
 *
 * @param {HTMLFormElement} state
 * @param {string} somevar value key to get value for
 * @returns {*}
 */
function get_var_from_state(state, somevar) {
    return state_to_obj(state)[somevar];
}

/**
 * Load settings from URL and update the state form
 * Used my multiple .edwh-state's in the _hs init
 *
 * @param {HTMLFormElement} state reference to <form>
 */
function url_to_state(state) {
    const urlsettings = new URLSearchParams(window.location.search);
    const settings = Array.from(urlsettings);
    state_to_form(state, settings);
    _("send ew:state_changed to closest .edwh-messagebus");
}

/**
 * Store an object in history and URL
 *
 * @param {object} data
 * @param {boolean} skip_empty remove params where value is falsey
 */
function _state_to_url(data, skip_empty = true) {
    let query = [];
    for (let [param, value] of Object.entries(data)) {
        if (param.startsWith("_")) {
            // internal use only, don't push to URL
            continue;
        }

        if (typeof value === "object") {
            value = JSON.stringify(value);
        }
        if (skip_empty && !value) continue;
        query.push(`${param}=${encodeURIComponent(value)}`);
    }

    const stringified_state = "?" + query.join("&");

    window.history.pushState(data, "_", stringified_state);
}

/**
 * On ew:state_changed, save current state in URL
 * Used by 'StateToURL on ew:state_changed'
 *
 * @param {HTMLElement} state
 */
function state_to_url(state) {
    if (event.detail.freeze) {
        // on popstate, call the event with (freeze: true),
        // to prevent overwriting history
        return;
    }

    _state_to_url(state.formData()); // Q helper 'formData'
}

/**
 *
 * @param {String} tag
 * @returns {String}
 */
function search_tag_url(tag) {
    const base = input("GHOST_BASE");
    return base + "?tags=" + JSON.stringify([tag]);
}

/**
 *
 * @param {String} tag
 * @returns {boolean}
 */
function handle_search_tag(tag) {
    window.location = search_tag_url(tag)
    return false;
}

/**
 * Used by htmx/_hs for the user and item page
 * Get the GID from the url, so e.g. /user/123 -> 123
 *
 * @param {String} type (deprecated)
 *
 * @returns {string}
 */
function extract_id_from_url(type = "DEPRECATED") {
    const path = window.location.pathname;
    return path.split("/").pop(); // return last part after / (= <id>)
}

let _timeout;

function avatar_file_hover(ev) {
    ev.preventDefault(); // also required for some reason
    const $box = _("#file-js-example");
    $box._css("border", "1px dotted black");
    clearTimeout(_timeout);
    _timeout = setTimeout((_) => {
        $box._css("border", "1px dotted white");
    }, 300);
}

function avatar_file_drop(holder, file) {
    try {
        holder.querySelector(".file-name").innerText = file.name;
        if (file.type.startsWith("image/")) {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => {
                const base64 = reader.result.split("base64,")[1];
                // set hidden field values:
                _(`set avatarcontent's value to '${base64}'
                 set avatar's value to '${file.name}'
                 add .is-success to #avatar-feedback then
                 take .is-danger from #avatar-feedback then
                 set #avatar-feedback's innerText to "Avatar geüpload, klik op 'Verzenden' om deze op te slaan."`);
            };
            reader.onerror = (error) => {
                console.error(error);
                throw {
                    msg: "Er ging iets mis bij het uploaden",
                };
            };
        } else {
            throw {
                msg: `Dit bestand (${file.name}) lijkt geen afbeelding te zijn.`,
            };
        }
    } catch (e) {
        const msg = e.msg || "Er is iets misgegaan";
        _(`
         add .is-danger to #avatar-feedback then
         take .is-success from #avatar-feedback then
         set #avatar-feedback's innerText to '${msg}'
          `);
    }
}

/**
 *
 * @param {HTMLElement} element
 * @param {String} classes
 */
function toggle_classes(element, ...classes) {
    for (let cls of classes) {
        element.classList.toggle(cls);
    }
    return true;
}

/**
 * Get the value of an <input> by name (NOT id)
 * @param {String} selector
 * @return {String}
 */
function input(selector) {
    return document.querySelector(`[name=${selector}]`).value;
}

// on popstate, use #state as default state holder (todo: anders; eventueel met hx of _ oid?)
window.addEventListener("popstate", (event) => {
    if (!event.state) {
        // go back one extra, stateless = probably referred from other page
        history.back();
    }

    // todo: what to do in case of multiple states?

    state_to_form(
        document.querySelector(".edwh-state"),
        Object.entries(event.state) // -> [[key, value], [key, value]]
    );

    _(`
        send ew:order_changed(order: '${event.state.order}') to closest .edwh-messagebus -- force 'order' update
        send ew:state_changed(freeze: true) to closest .edwh-messagebus -- send other state updates
        `);
});

// JSON encode extension to use hx-vals:

htmx.defineExtension("json-enc", {
    onEvent: function (name, evt) {
        if (name === "htmx:configRequest") {
            evt.detail.headers["Content-Type"] = "application/json";
        }
    },

    encodeParameters: function (xhr, parameters, elt) {
        xhr.overrideMimeType("text/json");
        return JSON.stringify(parameters);
    },
});

function debug() {
    if (!ALLOW_DEBUG) {
        throw "Debugging is not allowed!";
    }
    // toggle debug
    DEBUG = !DEBUG;
    console.debug(`Debug is now ${DEBUG ? "on" : "off"}`);
}
