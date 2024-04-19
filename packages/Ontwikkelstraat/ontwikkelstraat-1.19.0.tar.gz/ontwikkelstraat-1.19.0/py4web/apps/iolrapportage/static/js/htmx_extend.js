// HTMX internals ripped out and put together again in htmx public api methods
// expose internal HTMX methods that can be useful for working with hx-vars and hx-vals from javascript
// from htmx.js:2653

((_) => {
    function mergeObjects(obj1, obj2) {
        for (var key in obj2) {
            if (obj2.hasOwnProperty(key)) {
                obj1[key] = obj2[key];
            }
        }
        return obj1;
    }

    function getRawAttribute(elt, name) {
        return elt.getAttribute && elt.getAttribute(name);
    }

    function getAttributeValue(elt, qualifiedName) {
        return (
            getRawAttribute(elt, qualifiedName) ||
            getRawAttribute(elt, "data-" + qualifiedName)
        );
    }

    function parentElt(elt) {
        return elt.parentElement;
    }

    function parseJSON(jString) {
        try {
            return JSON.parse(jString);
        } catch (error) {
            console.error(error);
            return null;
        }
    }

    function getValuesForElement(elt, attr, evalAsDefault, values) {
        if (values == null) {
            values = {};
        }
        if (elt == null) {
            return values;
        }
        var attributeValue = getAttributeValue(elt, attr);
        if (attributeValue) {
            var str = attributeValue.trim();
            var evaluateValue = evalAsDefault;
            if (str.indexOf("javascript:") === 0) {
                str = str.substr(11);
                evaluateValue = true;
            } else if (str.indexOf("js:") === 0) {
                str = str.substr(3);
                evaluateValue = true;
            }
            if (str.indexOf("{") !== 0) {
                str = "{" + str + "}";
            }
            var varsValues;
            if (evaluateValue) {
                varsValues = Function("return (" + str + ")")();
            } else {
                varsValues = parseJSON(str);
            }
            for (var key in varsValues) {
                if (varsValues.hasOwnProperty(key)) {
                    if (values[key] == null) {
                        values[key] = varsValues[key];
                    }
                }
            }
        }
        return getValuesForElement(parentElt(elt), attr, evalAsDefault, values);
    }

    /**
     * Extract hx-vars as object
     *
     * @param {HTMLElement} elt element with hx-vars
     * @param {Object} expressionVars defaults
     * @returns {{}|*}
     */
    function getHXVarsForElement(elt, expressionVars) {
        return getValuesForElement(elt, "hx-vars", true, expressionVars);
    }

    /**
     * Extract hx-vals as object
     *
     * @param {HTMLElement} elt element with hx-vals
     * @param {Object} expressionVars defaults
     * @returns {{}|*}
     */
    function getHXValsForElement(elt, expressionVars) {
        return getValuesForElement(elt, "hx-vals", false, expressionVars);
    }

    /**
     * Extract hx-vals and hx-vars from elt, combined as object
     *
     * @param {HTMLElement} elt element with hx-vars and/or hx-vals
     * @returns {*}
     */
    function getExpressionVarsForElement(elt) {
        return mergeObjects(getHXVarsForElement(elt), getHXValsForElement(elt));
    }

    // extend htmx api:
    htmx.vals = getHXValsForElement;
    htmx.vars = getHXVarsForElement;
    htmx.expression_vars = getExpressionVarsForElement;
})();
