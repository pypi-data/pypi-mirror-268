=================
lesana-get-values
=================

SYNOPSIS
========

lesana search [--help] [--collection COLLECTION] [--template TEMPLATE] \
   --field FIELD [query [query ...]]

DESCRIPTION
===========

Lesana get-values will list all values found in a field and the number
of entries where that value has been found.

A template can be specified to format the results.

Extracting the values from a sortable field is significantly more
efficient than doing so from a non-sortable field, but adding too many
sortable fields can make general searches and indexing slower.

OPTIONS
=======

-h, --help
   Prints an help message and exits.
--collection COLLECTION, -c COLLECTION
   The collection to work on. Default is ``.``
--template TEMPLATE, -t TEMPLATE
   Template to use when displaying results
--field
   Name of the desired field.
