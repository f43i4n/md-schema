from unittest.mock import MagicMock, patch
import pytest


def test_import_works():
    import md_schema.__main__


def test_titlearea_simple():
    from md_schema.__main__ import Parser
    markdown = r'''
# Tool
long history
some text
'''[1:-1]
    schema_dict = [{
        'selector': 'h1',
        'name': 'nameOfTool',
        'type': 'titlearea',
    }]
    exp = {
        'nameOfTool': {
            'title': 'Tool',
            'description': 'long history\nsome text',
        },
    }

    parser = Parser(schema_dict)
    res = parser.parse(markdown)

    assert res == exp


@pytest.mark.xfail
def test_list_simple():
    from md_schema.__main__ import Parser
    markdown = r'''
# Licenses
- LGPL
- Apache
'''[1:-1]
    schema_dict = [{
        'selector': 'h1[text=\'Licenses\']',
        'name': 'licenses',
        'type': 'list',
    }]
    exp = {
        'licenses': {
            'elements': [
                {
                    'value': 'LGPL',
                    'raw_value': 'LGPL',
                }, {
                    'value': 'Apache',
                    'raw_value': 'Apache',
                }
            ]
            # 'description': 'long history\nsome text',
        },
    }

    parser = Parser(schema_dict)
    res = parser.parse(markdown)

    assert res == exp
