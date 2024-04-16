*******************
 Release procedure
*******************

* Check that the version number in setup.py and in docs/source/conf.py
  is correct.

* Check that the changelog is up to date.

* Tag the version you are preparing::

     $ git tag -s v$VERSION
     $ git push
     $ git push --tags

  for the tag content use something like::

     Version $VERSION

     * contents
     * of the relevant
     * changelog

* Generate the distribution files::

     $ python3 -m build

* Upload ::

     $ twine upload -s dist/*

* Send the release announce to::

     valhalla/lesana-announce@lists.sr.ht, ~valhalla/lesana-discuss@lists.sr.ht

* Close the bugs marked as pending_release on
  https://todo.sr.ht/~valhalla/lesana.
