***********
 CHANGELOG
***********

Unreleased
==========

0.10.0
======

* Command line code has been split in the hazwaz library.
* Code cleanup.
* Modernize packaging with pyproject.toml and setuptool_scm.
* Bump minimum supported Python version to 3.8.

0.9.1
=====

Bugfix release

* Included the post-checkout script in the released package.

0.9.0
=====

* New data type: geo (for Geo URIs).
* New custom filter for templates: to_yaml.
* git hook to update the lesana cache when files are changed by git.

  This hook is installed when running ``lesana init``; you may want to
  add it to existing repositories by running ``lesana init`` on them
  (this is safe to do and won't change your settings or your data).
* New command: get-values to get a list of values for a field. #6
* lesana-search now defaults to a query of ``'*'``.

  This means that ``lesana search --all`` is now enough to list all
  entries, while ``lesana search`` with no other options will list the
  first 12 entries (possibly according to a default sorting setting).
* New collection example: ticket_tracker.
* Add support for bash autocompletion via argcomplete, if installed.
* Add support for the ``values`` property in the settings, to limit the
  contents of a field.
* New property ``precision`` for ``decimal`` fields, to force rounding
  values to that number of decimal digits.
* New settings property ``search_aliases`` with a dict of values to be
  filled in in a jinja2 template for a search query.
* New experimental script openlibrary2lesana to search for book data on
  openlibrary and pre-fill a lesana entry.

Bugfixes
--------

* date fields are now parsed and loaded as date, not datetime.
* help strings are added as comments with just one #, not two.

0.8.1
=====

Bugfix release.

* Fixes running on an environment where EDITOR is not set. #7
* Fixes editing an entry. #8
* Fixes searches when default_sort isn't present. #9

0.8.0
=====

* New collection example: books.
* Fixes to the tellico2lesana script (python 2.9 compatibility).
* New option default_sort for collection, to sort search results by
  default. (#2)
* Added support to sort the list of all entries.
* Add the option to autofill date and datetime fields at creation and
  update time.  (#1)
* Add the option to autoincrement integer values.

0.7.0
=====

* Improved round trip loading of data results in less spurious changes
  when editing entries.
* More documentation and examples.
* Added support for sorting search results.
* Added --reset option to lesana index.

0.6.2
=====

* Documentation improvements.
* The timestamp field is now always interpreted as UTC.
* Updated links to the published homepage and docs.

0.6.1
=====

* Tarball fixes

0.6.0
=====

* Validation of field contents have been made stricter: invalid contents
  that were accepted in the past may now cause an indexing error.
* The timestamp field type is now deprecated and expected to contain a
  unix timestamp (a yaml datetime is accepted, but may be converted to a
  unix timestamp) and the types datetime and date have been added.

0.5.1
=====

Library
-------

* This version changes the name of entry IDs from the nonsensical ``uid`` to
  ``eid`` (Entry ID) everywhere in the code, including the property
  ``Entry.uid`` and all method names.
