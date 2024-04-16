"""
Custom jinja2 filters and other templating helpers
"""
import decimal
import io

import jinja2
import ruamel.yaml


class Environment(jinja2.Environment):
    """
    A customized jinja2 environment that includes our filters.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filters['to_yaml'] = to_yaml


def to_yaml(data):
    """
    Return the yaml representation of data.
    """
    if isinstance(data, str):
        if len(data) > 75 or "\n" in data:
            try:
                data = ruamel.yaml.scalarstring.LiteralScalarString(
                    data + "\n"
                )
            except AttributeError:
                data = ruamel.yaml.scalarstring.PreservedScalarString(
                    data + "\n"
                )
    elif isinstance(data, decimal.Decimal):
        data = str(data)
    elif data is None:
        return 'null'
    yaml = ruamel.yaml.YAML()
    s_io = io.StringIO()
    yaml.dump({'data': data}, s_io)
    res = s_io.getvalue()
    res = res.lstrip('{data:').lstrip().strip('...\n').strip()
    return res
