import argparse
import logging
import os
import sys

import hazwaz

try:
    import argcomplete
except ImportError:
    argcomplete = None  # type: ignore

from . import Collection, Entry, TemplatingError

logger = logging.getLogger(__name__)


class Command(hazwaz.Command):
    def __init__(self, collection_class=Collection, entry_class=Entry):
        super().__init__()
        self.collection_class = collection_class
        self.entry_class = entry_class

    def add_arguments(self, parser: argparse.ArgumentParser):
        # compatibility with the old way to add arguments: for new
        # commands override add_arguments directly
        for arg in self.arguments:
            parser.add_argument(*arg[0], **arg[1])


class New(Command, hazwaz.mixins.ExternalEditorMixin):
    """
    Create a new entry
    """
    arguments = [
        (
            ['--collection', '-c'],
            dict(help='The collection to work on (default .)'),
        ),
        (
            ['--no-git'],
            dict(
                help="Don't add the new entry to git",
                action="store_false",
                dest='git',
            ),
        ),
    ]

    def main(self):
        collection = self.collection_class(self.args.collection)
        new_entry = self.entry_class(collection)
        collection.save_entries([new_entry])
        filepath = os.path.join(collection.itemdir, new_entry.fname)
        if self.edit_file_in_external_editor(filepath):
            collection.update_cache([filepath])
            if self.args.git:
                collection.git_add_files([filepath])
        saved_entry = collection.entry_from_eid(new_entry.eid)
        print(saved_entry)


class Edit(Command, hazwaz.mixins.ExternalEditorMixin):
    """
    Edit a lesana entry
    """
    arguments = [
        (
            ['--collection', '-c'],
            dict(help='The collection to work on (default .)'),
        ),
        (
            ['--no-git'],
            dict(
                help="Don't add the new entry to git",
                action="store_false",
                dest='git',
            ),
        ),
        (['eid'], dict(help='eid of an entry to edit',)),
    ]

    def main(self):
        collection = self.collection_class(self.args.collection)
        entries = collection.entries_from_short_eid(self.args.eid)
        if len(entries) > 1:
            return "{} is not an unique eid".format(self.args.eid)
        if not entries:
            return "Could not find an entry with eid starting with: {}".format(
                self.args.eid
            )
        entry = entries[0]
        # update the entry before editing it
        entry.auto()
        collection.save_entries([entry])
        # and then edit the updated file
        filepath = os.path.join(collection.itemdir, entry.fname)
        if self.edit_file_in_external_editor(filepath):
            collection.update_cache([filepath])
            if self.args.git:
                collection.git_add_files([filepath])
        saved_entry = collection.entry_from_eid(entry.eid)
        print(saved_entry)


class Show(Command):
    """
    Show a lesana entry
    """
    arguments = [
        (
            ['--collection', '-c'],
            dict(help='The collection to work on (default .)'),
        ),
        (
            ['--template', '-t'],
            dict(help='Use the specified template to display results.',),
        ),
        (['eid'], dict(help='eid of an entry to edit',)),
    ]

    def main(self):
        collection = self.collection_class(self.args.collection)
        entries = collection.entries_from_short_eid(self.args.eid)
        if len(entries) > 1:
            return "{} is not an unique eid".format(self.args.eid)
        if not entries:
            return "Could not find an entry with eid starting with: {}".format(
                self.args.eid
            )
        entry = entries[0]
        if self.args.template:
            try:
                print(entry.render(self.args.template))
            except TemplatingError as e:
                logger.error("{}".format(e))
                sys.exit(1)
        else:
            print(entry.yaml_data)


class Index(Command):
    """
    Index entries in a lesana collection
    """
    arguments = [
        (
            ['--collection', '-c'],
            dict(help='The collection to work on (default .)'),
        ),
        (
            ['--reset'],
            dict(
                action='store_true',
                help='Delete the existing index and reindex from scratch.',
            ),
        ),
        (
            ['files'],
            dict(
                help='List of files to index (default: everything)',
                default=None,
                nargs='*',
            ),
        ),
    ]

    def main(self):
        collection = self.collection_class(self.args.collection)
        if self.args.files:
            files = (os.path.basename(f) for f in self.args.files)
        else:
            files = None
        indexed = collection.update_cache(
            fnames=files,
            reset=self.args.reset
        )
        print("Found and indexed {} entries".format(indexed))


class Search(Command):
    """
    Search for entries
    """
    arguments = [
        (
            ['--collection', '-c'],
            dict(help='The collection to work on (default .)'),
        ),
        (
            ['--template', '-t'],
            dict(help='Template to use when displaying results',),
        ),
        (['--offset'], dict(type=int,)),
        (['--pagesize'], dict(type=int,)),
        (
            ['--all'],
            dict(action='store_true', help='Return all available results'),
        ),
        (
            ['--sort'],
            dict(action='append', help='Sort results by a sortable field'),
        ),
        (
            ['--expand-query-template', '-e'],
            {
                'action': 'store_true',
                'help':
                    'Render search_aliases in the query as a jinja2 template',
            },
        ),
        (
            ['query'],
            {
                'help': 'Xapian query to search in the collection',
                'nargs': '*',
                'default': '*',
            },
        ),
    ]

    def main(self):
        # TODO: implement "searching" for everything
        if self.args.offset:
            logger.warning(
                "offset exposes an internal knob and MAY BE REMOVED "
                + "from a future release of lesana"  # noqa: W503
            )
        if self.args.pagesize:
            logger.warning(
                "pagesize exposes an internal knob and MAY BE REMOVED "
                + "from a future release of lesana"  # noqa: W503
            )
        offset = self.args.offset or 0
        pagesize = self.args.pagesize or 12
        collection = self.collection_class(self.args.collection)
        query = self.args.query
        if self.args.expand_query_template:
            for i, q in enumerate(query):
                query[i] = collection.render_query_template(q)
        # sorted results require a less efficient full search rather
        # than being able to use the list of all documents.
        if query == ['*'] and not (
            self.args.sort
            or getattr(collection.settings, 'default_sort', False)
        ):
            results = collection.get_all_documents()
        else:
            collection.start_search(
                ' '.join(query),
                sort_by=self.args.sort
            )
            if self.args.all:
                results = collection.get_all_search_results()
            else:
                results = collection.get_search_results(offset, pagesize)
        if self.args.template:
            try:
                template = collection.get_template(self.args.template)
                print(template.render(entries=results))
            except TemplatingError as e:
                logger.error("{}".format(e))
                sys.exit(1)
        else:
            for entry in results:
                print("{entry}".format(entry=entry,))


class GetValues(Command):
    """
    List all values for one field, with entry counts.
    """
    name = "get-values"

    arguments = [
        (
            ['--collection', '-c'],
            {
                'help': 'The collection to work on (default .)'
            },
        ),
        (
            ['--field', '-f'],
            {
                'help': 'Name of the field',
                'required': True,
            },
        ),
        (
            ['--template', '-t'],
            {
                'help': 'Template to use when displaying results',
            },
        ),
        (
            ['query'],
            {
                'help': 'Xapian query to limit the count search " \
                      + "in the collection',
                'nargs': '*',
                'default': '*'
            },
        ),
    ]

    def main(self):
        collection = self.collection_class(self.args.collection)
        counts = collection.get_field_values(
            self.args.field,
            ' '.join(self.args.query)
        )
        if self.args.template:
            try:
                template = collection.get_template(self.args.template)
                print(template.render(counts=counts))
            except TemplatingError as e:
                logger.error("{}".format(e))
                sys.exit(1)
        else:
            for v in counts:
                print("{value}: {count}".format(
                    value=v['value'],
                    count=v['frequency']
                ))


class Export(Command):
    """
    Export entries to a different collection
    """
    arguments = [
        (
            ['--collection', '-c'],
            dict(help='The collection to work on (default .)'),
        ),
        (
            ['--query', '-q'],
            dict(help='Xapian query to search in the collection',),
        ),
        (['destination'], dict(help='The collection to export entries to')),
        (['template'], dict(help='Template to convert entries',)),
    ]

    def main(self):
        collection = self.collection_class(self.args.collection)
        destination = self.collection_class(self.args.destination)
        if not self.args.query:
            results = collection.get_all_documents()
        else:
            collection.start_search(' '.join(self.args.query))
            results = collection.get_all_search_results()
        for entry in results:
            data = {
                "entry": entry
            }
            data.update(entry.data)
            try:
                destination.entry_from_rendered_template(
                    self.args.template,
                    data
                )
            except TemplatingError as e:
                logger.error("Error converting entry: {}".format(entry))
                logger.error("{}".format(e))
                sys.exit(1)


class Init(Command, hazwaz.mixins.ExternalEditorMixin):
    """
    Initialize a lesana collection
    """
    arguments = [
        (
            ['--collection', '-c'],
            dict(help='The directory to work on (default .)', default='.'),
        ),
        (
            ['--no-git'],
            dict(
                help='Skip setting up git in this directory',
                action="store_false",
                dest='git',
            ),
        ),
    ]

    def main(self):
        self.collection_class.init(
            self.args.collection,
            git_enabled=self.args.git,
            edit_file=self.edit_file_in_external_editor,
        )


class Remove(Command):
    """
    Remove an entry from a collection
    """
    name = "rm"

    arguments = [
        (
            ['--collection', '-c'],
            dict(help='The collection to work on (default .)',),
        ),
        (['entries'], dict(help='List of entries to remove', nargs='+',)),
    ]

    def main(self):
        collection = self.collection_class(self.args.collection)
        collection.remove_entries(eids=self.args.entries)


class Update(Command):
    """
    Update a field in multiple entries
    """
    arguments = [
        (
            ['--collection', '-c'],
            dict(help='The collection to work on (default .)',),
        ),
        (['--field', '-f'], dict(help='The field to change',)),
        (['--value', '-t'], dict(help='The value to set',)),
        (
            ['query'],
            dict(help='Xapian query to search in the collection', nargs='+'),
        ),
    ]

    def main(self):
        collection = self.collection_class(self.args.collection)
        collection.update_field(
            ' '.join(self.args.query),
            field=self.args.field,
            value=self.args.value,
        )


class Lesana(hazwaz.MainCommand):
    """
    Manage collections
    """

    commands = (
        New(),
        Edit(),
        Show(),
        Index(),
        Search(),
        GetValues(),
        Update(),
        Export(),
        Init(),
        Remove(),
    )
