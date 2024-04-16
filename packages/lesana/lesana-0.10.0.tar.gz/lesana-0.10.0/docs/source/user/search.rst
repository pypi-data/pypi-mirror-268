***************
 Search syntax
***************

Searches in lesana use the human readable query string format defined by
xapian.

The simplest search is just a list of terms: e.g. searching for
``thing object`` will find entries where either ``thing`` or ``object``
is present in one of the fields with ``free`` indexing.

It is also possible to specify that a term must be in one specific
field: the syntax for this is the name of the field follwed by ``:`` and
the term, e.g. ``name:object`` will search for entries with the term
``object`` in the ``name`` field.

Search queries can of course include the usual logical operators
``AND``, ``OR`` and ``NOT``.

More modifiers are available; see the `Query Parser`_ documentation from
xapian for details.

.. _`Query Parser`: https://getting-started-with-xapian.readthedocs.io/en/latest/concepts/search/queryparser.html

.. _search aliases:

Search templates and ``search_aliases``
=======================================

In some contexts, search queries are rendered as jinja2 templates with
the contents of the ``search_aliases`` property as set in
``settings.yaml``.

The values of those search aliases should be valid search snippets with
the syntax documented above; it's usually a good idea to wrap them in
parenthesis, so that they are easier to use in complex queries; e.g.::

   my_alias: '(name:object OR name:thing)'

can correctly be used in a query like::

   {{ my_alias }} AND description:shiny
