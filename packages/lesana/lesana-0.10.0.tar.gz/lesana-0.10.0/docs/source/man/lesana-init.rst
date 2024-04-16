===========
lesana-init
===========

SYNOPSIS
========

lesana init [--help] [--collection <collection>] [--no-git]

DESCRIPTION
===========

lesana init initializes a new lesana collection.

It will create the directory (if it does not exist) and, unless
``--no-git`` is specified it will initialize it as a git repository,
create a ``.gitignore`` file with some relevant contents and add hooks
to update the local cache when the files are changed via git.

It will then create a skeleton ``settings.yaml`` file and open it in an
editor to start configuring the collection.

When leaving the editor, again unless ``--no-git`` is used, it will add
this file to the git staging area, but not commit it.

It is safe to run this command on an existing repository, e.g. to
install the hooks on a new clone, but it will overwrite the hooks
themselves even if they have been changed by the user.

OPTIONS
=======

--help, -h
   Prints an help message and exits.
--collection COLLECTION, -c COLLECTION
   The directory where the collection will be initialized. Default is .
--no-git
   Do not use git in the current collection.
