import datetime
import decimal
import logging
import os.path
import shutil
import tempfile
import unittest

import git
import ruamel.yaml

import lesana


class testEntries(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        shutil.copytree(
            'tests/data/simple',
            self.tmpdir.name,
            dirs_exist_ok=True
        )
        self.collection = lesana.Collection(self.tmpdir.name)
        self.basepath = self.collection.itemdir
        self.filenames = []
        self.yaml = ruamel.yaml.YAML(typ='safe', pure=True)

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_simple(self):
        fname = '085682ed-6792-499d-a3ab-9aebd683c011.yaml'
        with open(os.path.join(self.basepath, fname)) as fp:
            data = self.yaml.load(fp)
        entry = lesana.Entry(self.collection, data=data, fname=fname)
        self.assertEqual(entry.idterm, 'Q' + data['eid'])
        fname = '11189ee47ddf4796b718a483b379f976.yaml'
        eid = '11189ee47ddf4796b718a483b379f976'
        with open(os.path.join(self.basepath, fname)) as fp:
            data = self.yaml.load(fp)
        entry = lesana.Entry(self.collection, data=data, fname=fname)
        self.assertEqual(entry.idterm, 'Q' + eid)
        self.assertEqual(entry.short_id, eid[:8])

    @unittest.skipIf(
        ruamel.yaml.version_info < (0, 16, 0),
        "Preservation of data on file requires ruamel.yaml >= 0.16",
    )
    def test_write_new(self):
        new_entry = lesana.Entry(self.collection)
        self.collection.save_entries(entries=[new_entry])
        entry_fname = os.path.join(self.basepath, new_entry.fname)
        with open(entry_fname) as fp:
            text = fp.read()
        self.assertIn('# quantity (integer): how many items are there', text)
        self.assertIn('# other (yaml):', text)
        self.assertNotIn('# position (string)', text)
        self.assertNotIn('# # other (yaml)', text)
        written = self.yaml.load(text)
        self.assertIsInstance(written['quantity'], int)
        self.assertIsInstance(written['name'], str)

    def test_entry_representation(self):
        eid = '11189ee47ddf4796b718a483b379f976'
        entry = self.collection.entry_from_eid(eid)
        self.assertEqual(str(entry), eid)
        label = '{{ eid }}: {{ name }}'
        self.collection.settings['entry_label'] = label
        self.assertEqual(
            str(entry), '{eid}: {name}'.format(eid=eid, name='Another item')
        )

    def test_entry_creation_eid_but_no_filename(self):
        fname = '11189ee47ddf4796b718a483b379f976.yaml'
        with open(os.path.join(self.basepath, fname)) as fp:
            data = self.yaml.load(fp)
        data['eid'] = '11189ee47ddf4796b718a483b379f976'
        entry = lesana.Entry(self.collection, data=data)
        self.assertEqual(entry.fname, fname)

    def test_entry_creation_no_eid_no_filename(self):
        fname = '11189ee47ddf4796b718a483b379f976.yaml'
        with open(os.path.join(self.basepath, fname)) as fp:
            data = self.yaml.load(fp)
        entry = lesana.Entry(self.collection, data=data)
        self.assertIsNotNone(entry.eid)
        self.assertIsNotNone(entry.fname)

    def test_entry_creation_filename_but_no_eid(self):
        fname = '11189ee47ddf4796b718a483b379f976.yaml'
        eid = '11189ee47ddf4796b718a483b379f976'
        with open(os.path.join(self.basepath, fname)) as fp:
            data = self.yaml.load(fp)
        entry = lesana.Entry(self.collection, data=data, fname=fname)
        self.assertEqual(entry.eid, eid)

    def test_entry_str_filename_and_eid(self):
        fname = '11189ee47ddf4796b718a483b379f976.yaml'
        with open(os.path.join(self.basepath, fname)) as fp:
            data = self.yaml.load(fp)
        data['eid'] = '11189ee47ddf4796b718a483b379f976'
        entry = lesana.Entry(self.collection, data=data)
        self.assertEqual(str(entry), data['eid'])
        self.collection.settings['entry_label'] = '{{ eid }}: {{ name }}'
        self.assertEqual(str(entry), data['eid'] + ': Another item')

    def test_entry_str_filename_no_eid(self):
        fname = '11189ee47ddf4796b718a483b379f976.yaml'
        with open(os.path.join(self.basepath, fname)) as fp:
            data = self.yaml.load(fp)
        entry = lesana.Entry(self.collection, data=data)
        eid = entry.eid
        self.assertEqual(str(entry), eid)
        self.collection.settings['entry_label'] = '{{ eid }}: {{ name }}'
        self.assertEqual(str(entry), eid + ': Another item')

    def test_render_entry(self):
        fname = '11189ee47ddf4796b718a483b379f976.yaml'
        with open(os.path.join(self.basepath, fname)) as fp:
            data = self.yaml.load(fp)
        entry = lesana.Entry(self.collection, data=data)
        eid = entry.eid
        res = entry.render('tests/data/simple/templates/trivial_template.txt')
        self.assertIn(eid, res)

    def test_empty_data(self):
        entry = lesana.Entry(self.collection)
        self.assertIn("name: ''", entry.yaml_data)
        self.assertIn('quantity: 0', entry.yaml_data)

    def test_update_entry(self):
        eid = '11189ee47ddf4796b718a483b379f976'
        entry = self.collection.entry_from_eid(eid)
        old_data = entry.data.copy()
        entry.auto()
        self.assertEqual(old_data, entry.data)


class testEmptyCollection(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        shutil.copytree(
            'tests/data/empty',
            self.tmpdir.name,
            dirs_exist_ok=True
        )
        self.collection = lesana.Collection(self.tmpdir.name)

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_loaded(self):
        self.assertEqual(self.collection.settings, {})

        indexed = self.collection.update_cache()
        self.assertIsNotNone(self.collection.stemmer)
        self.assertEqual(indexed, 0)


class testSimpleCollection(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        shutil.copytree(
            'tests/data/simple',
            self.tmpdir.name,
            dirs_exist_ok=True
        )
        self.collection = lesana.Collection(self.tmpdir.name)
        self.yaml = ruamel.yaml.YAML(typ='safe', pure=True)

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_loaded(self):
        self.assertIsNotNone(self.collection.settings)
        self.assertEqual(
            self.collection.settings['name'], "Simple lesana collection"
        )
        self.assertEqual(len(self.collection.settings['fields']), 7)
        self.assertEqual(len(self.collection.indexed_fields), 3)

        indexed = self.collection.update_cache()
        self.assertIsNotNone(self.collection.stemmer)
        self.assertEqual(indexed, 3)

    def test_full_search(self):
        self.collection.start_search('Item')
        res = self.collection.get_all_search_results()
        matches = list(res)
        self.assertEqual(len(matches), 2)
        for m in matches:
            self.assertIsInstance(m, lesana.Entry)

    def test_search(self):
        self.collection.start_search('Item')
        res = self.collection.get_search_results()
        matches = list(res)
        self.assertEqual(len(matches), 2)
        for m in matches:
            self.assertIsInstance(m, lesana.Entry)

    def test_search_wildcard(self):
        self.collection.start_search('Ite*')
        res = self.collection.get_search_results()
        matches = list(res)
        self.assertEqual(len(matches), 2)
        for m in matches:
            self.assertIsInstance(m, lesana.Entry)

    def test_search_non_init(self):
        matches = list(self.collection.get_search_results())
        self.assertEqual(matches, [])
        matches = list(self.collection.get_all_search_results())
        self.assertEqual(matches, [])

    def test_all_entries(self):
        res = self.collection.get_all_documents()
        matches = list(res)
        self.assertEqual(len(matches), 3)
        for m in matches:
            self.assertIsInstance(m, lesana.Entry)

    def test_entry_from_eid(self):
        entry = self.collection.entry_from_eid(
            '11189ee47ddf4796b718a483b379f976'
        )
        self.assertEqual(entry.eid, '11189ee47ddf4796b718a483b379f976')
        self.collection.safe = True
        entry = self.collection.entry_from_eid(
            '11189ee47ddf4796b718a483b379f976'
        )
        self.assertEqual(entry.eid, '11189ee47ddf4796b718a483b379f976')

    def test_entry_from_short_eid(self):
        entries = self.collection.entries_from_short_eid('11189ee4')
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].eid, '11189ee47ddf4796b718a483b379f976')
        entries = self.collection.entries_from_short_eid(
            '11189ee47ddf4796b718a483b379f976'
        )
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].eid, '11189ee47ddf4796b718a483b379f976')
        entries = self.collection.entries_from_short_eid('12345678')
        self.assertEqual(len(entries), 0)

    def test_index_missing_file(self):
        with self.assertLogs(level=logging.WARNING) as cm:
            self.collection.update_cache(['non_existing_file'])
        self.assertEqual(len(cm.output), 1)
        self.assertIn("non_existing_file", cm.output[0])

    def test_index_reset(self):
        indexed = self.collection.update_cache(reset=True)
        self.assertEqual(indexed, 3)

    def test_get_entry_missing_eid(self):
        entry = self.collection.entry_from_eid('this is not an eid')
        self.assertIsNone(entry)

    def test_render_collection(self):
        template = self.collection.get_template(
            'tests/data/simple/templates/collection_template.txt'
        )
        res = template.render(entries=self.collection.get_all_documents())
        self.assertIn('11189ee4: Another item', res)

    def test_update(self):
        self.collection.update_field('Item', field="position", value="new_pos")
        with open(
            os.path.join(
                self.collection.basedir,
                'items',
                '11189ee47ddf4796b718a483b379f976.yaml',
            )
        ) as fp:
            self.assertIn("new_pos", fp.read())
            pass
        self.assertEqual(
            self.collection.entry_from_eid(
                "11189ee47ddf4796b718a483b379f976"
            ).data['position'],
            "new_pos",
        )

        self.assertIsNone(
            self.collection.entry_from_eid(
                "8b69b063b2a64db7b5714294a69255c7"
            ).data['position']
        )

    def test_representation_decimal(self):
        entry = self.collection.entry_from_eid(
            '085682ed6792499da3ab9aebd683c011'
        )
        data = self.yaml.load(entry.yaml_data)
        self.assertEqual(data['cost'], '1.99')

        fname = 'tests/data/simple/items/' + \
            '085682ed-6792-499d-a3ab-9aebd683c011.yaml'
        with open(fname, 'r') as fp:
            self.assertEqual(entry.yaml_data, fp.read())

    def test_list_values(self):
        values = self.collection.get_field_values('position')
        values = list(values)
        self.assertEqual(len(values), 2)
        self.assertEqual(values, [
            {'value': 'somewhere', 'frequency': 2},
            {'value': None, 'frequency': 1},
        ])

    def test_entry_from_template(self):
        # TODO: make finding the templates less prone to breaking and
        # then remove the cwd change from here
        old_cwd = os.getcwd()
        os.chdir(self.tmpdir.name)
        data = {
            "name": "This is a name",
        }
        entry = self.collection.entry_from_rendered_template(
            "templates/new_entry_from_data.yaml",
            data
        )
        os.chdir(old_cwd)
        self.assertIsInstance(entry, lesana.Entry)
        self.assertEqual(entry.data["name"], "This is a name")

    def test_entry_from_template_multiple_data_sources(self):
        # TODO: make finding the templates less prone to breaking and
        # then remove the cwd change from here
        old_cwd = os.getcwd()
        os.chdir(self.tmpdir.name)
        data = {
            "name": "This is a name",
        }
        values = {
            "quantity": 5,
            "cost": decimal.Decimal("3.5"),
        }
        entry = self.collection.entry_from_rendered_template(
            "templates/new_entry_from_multiple_data.yaml",
            {
                "data": data,
                "values": values
            }
        )
        os.chdir(old_cwd)
        self.assertIsInstance(entry, lesana.Entry)
        self.assertEqual(entry.data["name"], "This is a name")
        self.assertEqual(entry.data["quantity"], 5)

    def test_entry_from_bad_template(self):
        # TODO: make finding the templates less prone to breaking and
        # then remove the cwd change from here
        old_cwd = os.getcwd()
        os.chdir(self.tmpdir.name)
        data = {
            "name": "This is a name",
        }
        with self.assertRaises(lesana.collection.TemplatingError):
            self.collection.entry_from_rendered_template(
                "templates/new_entry_from_data_broken.yaml",
                data
            )
        os.chdir(old_cwd)

    def test_entry_from_bad_yaml(self):
        # TODO: make finding the templates less prone to breaking and
        # then remove the cwd change from here
        old_cwd = os.getcwd()
        os.chdir(self.tmpdir.name)
        data = {
            "name": "This is a name",
        }
        with self.assertRaises(lesana.collection.TemplatingError):
            self.collection.entry_from_rendered_template(
                "templates/new_entry_from_data_invalid_yaml.yaml",
                data
            )
        os.chdir(old_cwd)


class testComplexCollection(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        shutil.copytree(
            'tests/data/complex',
            self.tmpdir.name,
            dirs_exist_ok=True
        )
        self.collection = lesana.Collection(self.tmpdir.name)

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_init(self):
        self.assertIsNotNone(self.collection.settings)
        self.assertEqual(
            self.collection.settings['name'],
            "Fully featured lesana collection",
        )
        self.assertEqual(len(self.collection.settings['fields']), 16)
        self.assertIsNotNone(self.collection.stemmer)
        self.assertEqual(len(self.collection.indexed_fields), 9)

    def test_index(self):
        indexed = self.collection.update_cache()
        self.assertEqual(indexed, 10)

    def test_indexing_list(self):
        self.collection.update_cache(['73097121f1874a6ea2f927db7dc4f11e.yaml'])
        self.collection.start_search('tags:this')
        res = self.collection.get_search_results()
        matches = list(res)
        self.assertEqual(len(matches), 1)
        for m in matches:
            self.assertIsInstance(m, lesana.Entry)

    def test_boolean_field(self):
        entry = self.collection.entry_from_eid(
            '73097121f1874a6ea2f927db7dc4f11e'
        )
        self.assertIsInstance(entry.data['exists'], bool)

    def test_empty_data(self):
        entry = lesana.Entry(self.collection)
        self.assertIn("name: ''", entry.yaml_data)
        self.assertIn('with_default', entry.yaml_data)
        self.assertIn('amount: 0', entry.yaml_data)
        self.assertIn("tags: []", entry.yaml_data)
        self.assertIn("exists:\n", entry.yaml_data)
        # we just check that created starts with a date and ends with
        # the utc timezone to keep the regex short and manageable
        self.assertRegex(
            entry.yaml_data,
            r"created: [\d]{4,4}-[\d]{2,2}-[\d]{2,2} .*\+00\:00"
        )
        self.assertIn("epoch:\n", entry.yaml_data)

    def test_load_field_loaders(self):
        # Check that all fields have been loaded, with the right types
        to_test = (
            ('name', lesana.types.LesanaString),
            ('description', lesana.types.LesanaText),
            ('position', lesana.types.LesanaString),
            ('something', lesana.types.LesanaYAML),
            ('tags', lesana.types.LesanaList),
            ('keywords', lesana.types.LesanaList),
            ('exists', lesana.types.LesanaBoolean),
            ('with_default', lesana.types.LesanaString),
            ('amount', lesana.types.LesanaInt),
        )
        for f in to_test:
            self.assertIsInstance(self.collection.fields[f[0]], f[1])

    @unittest.skipIf(
        ruamel.yaml.version_info < (0, 16, 0),
        "Preservation of data on file requires ruamel.yaml >= 0.16",
    )
    def test_comments_are_preserved(self):
        e = self.collection.entry_from_eid('5084bc6e94f24dc6976629282ef30419')
        yaml_data = e.yaml_data
        self.assertTrue(
            yaml_data.startswith("# This entry has a comment at the beginning")
        )
        self.assertTrue(
            yaml_data.endswith("# and a comment at the end\n")
        )

    @unittest.skipIf(
        ruamel.yaml.version_info < (0, 16, 0),
        "Preservation of data on file requires ruamel.yaml >= 0.16",
    )
    def test_data_is_stored_as_written_on_file(self):
        e = self.collection.entry_from_eid('5084bc6e94f24dc6976629282ef30419')
        fname = 'tests/data/complex/items/' + \
            '5084bc6e94f24dc6976629282ef30419.yaml'
        with open(fname, 'r') as fp:
            self.assertEqual(e.yaml_data, fp.read())

    def test_data_is_stored_as_written_on_file_with_apices(self):
        e = self.collection.entry_from_eid('8e9fa1ed3c1b4a30a6be7a98eda0cfa7')
        fname = 'tests/data/complex/items/' + \
            '8e9fa1ed3c1b4a30a6be7a98eda0cfa7.yaml'
        with open(fname, 'r') as fp:
            self.assertEqual(e.yaml_data, fp.read())

    def test_sorted_search(self):
        # search in ascending order
        self.collection.start_search('Amount', sort_by=['amount'])
        res = self.collection.get_search_results()
        matches = list(res)
        self.assertEqual(len(matches), 4)
        self.assertEqual(matches[0].data['amount'], 2)
        self.assertEqual(matches[1].data['amount'], 10)
        self.assertEqual(matches[2].data['amount'], 15)
        self.assertEqual(matches[3].data['amount'], 20)

        # and in descending order
        self.collection.start_search('Amount', sort_by=['-amount'])
        res = self.collection.get_search_results()
        matches = list(res)
        self.assertEqual(len(matches), 4)
        self.assertEqual(matches[0].data['amount'], 20)
        self.assertEqual(matches[1].data['amount'], 15)
        self.assertEqual(matches[2].data['amount'], 10)
        self.assertEqual(matches[3].data['amount'], 2)

    def test_default_sorted_search(self):
        # search in ascending order
        self.collection.start_search('Amount')
        res = self.collection.get_search_results()
        matches = list(res)
        self.assertEqual(len(matches), 4)
        print([m.data['order'] for m in matches])
        self.assertEqual(matches[0].data['order'], None)
        self.assertEqual(matches[1].data['order'], 'alpha')
        self.assertEqual(matches[2].data['order'], 'charlie')
        self.assertEqual(matches[3].data['order'], 'zucchini')

    def test_search_all_documents_default_sort(self):
        self.collection.start_search('*')
        res = self.collection.get_search_results()
        matches = list(res)
        self.assertEqual(len(matches), 10)
        for i in range(5):
            self.assertEqual(matches[i].data['order'], None)
        self.assertEqual(matches[6].data['order'], 'alpha')
        self.assertEqual(matches[7].data['order'], 'charlie')
        self.assertEqual(matches[8].data['order'], 'delta')
        self.assertEqual(matches[9].data['order'], 'zucchini')

    def test_update_entry(self):
        eid = '5084bc6e94f24dc6976629282ef30419'
        entry = self.collection.entry_from_eid(eid)
        # we keep the old data, and check that the updated field is
        # empty and the version field is 0
        old_data = entry.data.copy()
        self.assertEqual(entry.data['updated'], None)
        self.assertEqual(entry.data['version'], 0)

        entry.auto()

        # after the update, fields that were not supposed to be updated
        # are equal to what they were before, while updated has been
        # changed to a datetime in this year (we don't check too deeply
        # to avoid breaking tests too often with race conditions) and
        # version has grown to 2.
        for field in ('created', 'epoch'):
            self.assertEqual(old_data[field], entry.data[field])
        now = datetime.datetime.now(datetime.timezone.utc)
        self.assertIsInstance(entry.data['updated'], datetime.datetime)
        self.assertEqual(entry.data['updated'].year, now.year)
        self.assertEqual(entry.data['version'], 2)

    def test_list_values(self):
        values = self.collection.get_field_values('position')
        values = list(values)
        self.assertEqual(values, [
            {'value': b'Somewhere', 'frequency': 1},
            {'value': b'over there', 'frequency': 1},
            {'value': b'somewhere', 'frequency': 1},
            {'value': b'there', 'frequency': 1},
        ])

    def test_decimal_as_float(self):
        eid = 'a4265cc5dfa94c3d8030d7df4a0ab747'
        entry = self.collection.entry_from_eid(eid)
        self.assertEqual(entry.data['price'], "1.90")

    def test_search_aliases(self):
        search_query = "{{ nice }}"
        search_query = self.collection.render_query_template(search_query)
        print("QUERY IS", search_query)
        self.collection.start_search(search_query)
        res = self.collection.get_search_results()
        matches = list(res)
        self.assertEqual(len(matches), 2)
        matches_ids = [m.eid for m in matches]
        self.assertIn('8e9fa1ed3c1b4a30a6be7a98eda0cfa7', matches_ids)
        self.assertIn('5084bc6e94f24dc6976629282ef30419', matches_ids)


class testCollectionWithErrors(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        shutil.copytree(
            'tests/data/wrong',
            self.tmpdir.name,
            dirs_exist_ok=True
        )
        self.collection = lesana.Collection(self.tmpdir.name)

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_load_wrong_language(self):
        # We reload this collection, with an invalid value in lang, to
        # check that the log contains a warning.
        with self.assertLogs(level=logging.WARNING) as cm:
            self.collection = lesana.Collection(self.tmpdir.name)
        self.assertEqual(len(cm.output), 2)
        self.assertIn("Invalid language", cm.output[1])
        # The collection will default to english, but should still work.
        self.collection.update_cache()
        self.assertIsNotNone(self.collection.settings)
        self.assertIsNotNone(self.collection.stemmer)

    def test_no_index_for_one_field(self):
        # In the “wrong” collection, some of the entries have no "index"
        # field.
        self.collection.update_cache()
        self.assertIsNotNone(self.collection.settings)
        self.assertIsNotNone(self.collection.stemmer)
        # Fields with no "index" entry are not indexed
        self.assertEqual(len(self.collection.settings['fields']), 10)
        self.assertEqual(len(self.collection.indexed_fields), 3)

    def test_init(self):
        self.assertIsNotNone(self.collection.settings)
        self.assertEqual(
            self.collection.settings['name'],
            "Lesana collection with certain errors",
        )
        self.assertEqual(len(self.collection.settings['fields']), 10)
        self.assertIsNotNone(self.collection.stemmer)
        self.assertEqual(len(self.collection.indexed_fields), 3)

    def test_index(self):
        loaded = self.collection.update_cache()
        self.assertEqual(loaded, 0)


class testCollectionCreation(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_init(self):
        collection = lesana.Collection.init(self.tmpdir.name)
        self.assertIsInstance(collection, lesana.Collection)
        self.assertTrue(os.path.isdir(os.path.join(self.tmpdir.name, '.git')))
        self.assertTrue(os.path.isdir(os.path.join(
            self.tmpdir.name,
            '.lesana'
        )))
        self.assertTrue(
            os.path.isfile(os.path.join(self.tmpdir.name, 'settings.yaml'))
        )
        self.assertTrue(
            os.path.isfile(os.path.join(self.tmpdir.name, '.gitignore'))
        )
        checkout_hook = os.path.join(
            self.tmpdir.name,
            '.git',
            'hooks',
            'post-checkout',
        )
        merge_hook = os.path.join(
            self.tmpdir.name,
            '.git',
            'hooks',
            'post-merge',
        )
        self.assertTrue(os.path.isfile(checkout_hook))
        self.assertTrue(os.path.islink(merge_hook))
        self.assertEqual(
            os.path.abspath(checkout_hook),
            os.path.abspath(os.readlink(merge_hook))
        )
        # and then run it twice on the same directory, nothing should break
        collection = lesana.Collection.init(self.tmpdir.name)
        self.assertIsInstance(collection, lesana.Collection)
        self.assertTrue(os.path.isdir(os.path.join(self.tmpdir.name, '.git')))
        self.assertTrue(os.path.isdir(os.path.join(
            self.tmpdir.name,
            '.lesana'
        )))
        self.assertTrue(
            os.path.isfile(os.path.join(self.tmpdir.name, 'settings.yaml'))
        )
        self.assertTrue(
            os.path.isfile(os.path.join(self.tmpdir.name, '.gitignore'))
        )
        created = lesana.Collection(self.tmpdir.name)
        self.assertTrue(created.settings['git'])

    def _do_nothing(*args, **kwargs):
        # A function that does nothing instead of editing a file
        pass

    def test_init_edit_file(self):
        collection = lesana.Collection.init(
            self.tmpdir.name, edit_file=self._do_nothing
        )
        self.assertIsInstance(collection, lesana.Collection)
        self.assertTrue(os.path.isdir(os.path.join(self.tmpdir.name, '.git')))
        self.assertTrue(os.path.isdir(os.path.join(
            self.tmpdir.name,
            '.lesana'
        )))
        self.assertTrue(
            os.path.isfile(os.path.join(self.tmpdir.name, 'settings.yaml'))
        )
        self.assertTrue(
            os.path.isfile(os.path.join(self.tmpdir.name, '.gitignore'))
        )

    def test_init_no_git(self):
        collection = lesana.Collection.init(
            self.tmpdir.name,
            git_enabled=False
        )
        self.assertIsInstance(collection, lesana.Collection)
        self.assertFalse(os.path.isdir(os.path.join(self.tmpdir.name, '.git')))
        self.assertTrue(os.path.isdir(os.path.join(
            self.tmpdir.name,
            '.lesana'
        )))
        self.assertTrue(
            os.path.isfile(os.path.join(self.tmpdir.name, 'settings.yaml'))
        )
        self.assertFalse(
            os.path.isfile(os.path.join(self.tmpdir.name, '.gitignore'))
        )
        # and then run it twice on the same directory, nothing should break
        collection = lesana.Collection.init(
            self.tmpdir.name,
            git_enabled=False
        )
        self.assertIsInstance(collection, lesana.Collection)
        self.assertFalse(os.path.isdir(os.path.join(self.tmpdir.name, '.git')))
        self.assertTrue(os.path.isdir(os.path.join(
            self.tmpdir.name,
            '.lesana'
        )))
        self.assertTrue(
            os.path.isfile(os.path.join(self.tmpdir.name, 'settings.yaml'))
        )
        self.assertFalse(
            os.path.isfile(os.path.join(self.tmpdir.name, '.gitignore'))
        )
        created = lesana.Collection(self.tmpdir.name)
        self.assertFalse(created.settings['git'])

    def test_deletion(self):
        shutil.copy('tests/data/simple/settings.yaml', self.tmpdir.name)
        shutil.copytree(
            'tests/data/simple/items', os.path.join(self.tmpdir.name, 'items'),
        )
        collection = lesana.Collection.init(self.tmpdir.name)
        # We start with one item indexed with the term "another"
        collection.start_search('another')
        mset = collection._enquire.get_mset(0, 10)
        self.assertEqual(mset.get_matches_estimated(), 1)
        # Then delete it
        collection.remove_entries(['11189ee47ddf4796b718a483b379f976'])
        # An now we should have none
        self.assertFalse(
            os.path.exists(
                os.path.join(
                    self.tmpdir.name,
                    'items',
                    '11189ee47ddf4796b718a483b379f976.yaml',
                )
            )
        )
        collection.start_search('another')
        mset = collection._enquire.get_mset(0, 10)
        self.assertEqual(mset.get_matches_estimated(), 0)

    def test_partial_eid_deletion(self):
        shutil.copy('tests/data/simple/settings.yaml', self.tmpdir.name)
        shutil.copytree(
            'tests/data/simple/items', os.path.join(self.tmpdir.name, 'items'),
        )
        collection = lesana.Collection.init(self.tmpdir.name)
        # We start with one item indexed with the term "another"
        collection.start_search('another')
        mset = collection._enquire.get_mset(0, 10)
        self.assertEqual(mset.get_matches_estimated(), 1)
        # Then delete it, using the short id
        collection.remove_entries(['11189ee4'])
        # An now we should have none
        self.assertFalse(
            os.path.exists(
                os.path.join(
                    self.tmpdir.name,
                    'items',
                    '11189ee47ddf4796b718a483b379f976.yaml',
                )
            )
        )
        collection.start_search('another')
        mset = collection._enquire.get_mset(0, 10)
        self.assertEqual(mset.get_matches_estimated(), 0)

    def _find_file_in_git_index(self, fname, index):
        found = False
        for (path, stage) in index.entries:
            if fname in path:
                found = True
                break
        return found

    def test_git_adding(self):
        shutil.copy('tests/data/simple/settings.yaml', self.tmpdir.name)
        shutil.copytree(
            'tests/data/simple/items', os.path.join(self.tmpdir.name, 'items'),
        )
        collection = lesana.Collection.init(self.tmpdir.name)
        fname = '11189ee47ddf4796b718a483b379f976.yaml'
        repo = git.Repo(self.tmpdir.name)
        # By default, this collection doesn't have any git entry in the
        # settings (but there is a repo)
        collection.git_add_files([os.path.join(collection.itemdir, fname)])
        self.assertFalse(self._find_file_in_git_index(fname, repo.index))
        # Then we set it to false
        collection.settings['git'] = False
        collection.git_add_files([os.path.join(collection.itemdir, fname)])
        self.assertFalse(self._find_file_in_git_index(fname, repo.index))
        # And only when it's set to true we should find the file in the
        # staging area
        collection.settings['git'] = True
        collection.git_add_files([os.path.join(collection.itemdir, fname)])
        self.assertTrue(self._find_file_in_git_index(fname, repo.index))

    def test_init_custom_settings(self):
        collection = lesana.Collection.init(
            self.tmpdir.name,
            edit_file=self._do_nothing,
            settings={
                'name': 'A different name',
                'fields': [
                    {'name': 'title', 'type': 'string'},
                    {'name': 'author', 'type': 'string'},
                ],
            },
        )
        self.assertIsInstance(collection, lesana.Collection)
        self.assertTrue(
            os.path.isfile(os.path.join(self.tmpdir.name, 'settings.yaml'))
        )
        self.assertEqual(collection.settings['name'], 'A different name')
        self.assertEqual(len(collection.settings['fields']), 2)


if __name__ == '__main__':
    unittest.main()
