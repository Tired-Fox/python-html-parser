AST(position=None, children=[Element('doctype', position=Position(Point(0, 0), Point(0, 15)), attributes={'lang': 'html'}, children=None), Element('html', position=Position(Point(0, 15), Point(28, 56)), attributes={}, children=[Element('head', position=Position(Point(0, 21), Point(10, 24)), attributes={}, children=[Element('title', position=Position(Point(0, 27), Point(2, 16)), attributes={}, children=[Literal('text', 'Sample title')]), Element('python', position=Position(Point(2, 16), Point(10, 17)), attributes={}, children=[Literal('text', '\n            start = "Start"\n            end = "end."\n\n            errors = [\n                "1",\n                "2"\n            ]\n        ')])]), Element('body', position=Position(Point(10, 24), Point(28, 49)), attributes={}, children=[Element('Component', position=Position(Point(10, 30), Point(10, 62)), attributes={':message': 'message'}, children=None), Literal('comment', ' Sample Comment 1 '), Literal('text', 'Sample Text'), Literal('comment', ' Sample Comment 2 '), Element('Sub.Component', position=Position(Point(12, 33), Point(14, 25)), attributes={}, children=[Element('p', position=Position(Point(12, 48), Point(12, 9)), attributes={}, children=[Literal('text', 'Child')]), Literal('text', 'Generic text'), Element('p', position=Position(Point(14, 12), Point(14, 9)), attributes={'slot': 'extra'}, children=[Literal('text', 'Extra')])]), Element('input', position=Position(Point(14, 25), Point(20, 40)), attributes={'type': 'text', 'max': '100', 'value': '{{ start }} with this, not {{ end }}', ':hidden': 'True', 'data-is-active': False}, children=None), Element('p', position=Position(Point(20, 40), Point(20, 15)), attributes={'@if': 'False'}, children=[Literal('text', 'Never shows')]), Element('p', position=Position(Point(20, 15), Point(20, 17)), attributes={'@elif': 'not blank(message)'}, children=[Literal('text', '{{ message }}')]), Element('p', position=Position(Point(20, 17), Point(20, 12)), attributes={'@else': True}, children=[Literal('text', 'Fallback')]), Element('pre', position=Position(Point(20, 12), Point(20, 10)), attributes={}, children=[Literal('text', 'text', in_pre=True)], in_pre=True), Element('ul', position=Position(Point(20, 10), Point(20, 23)), attributes={}, children=[Element('For', position=Position(Point(20, 14), Point(20, 20)), attributes={':each': 'error in errors'}, children=[Element('li', position=Position(Point(20, 43), Point(20, 14)), attributes={}, children=[Literal('text', '{{error}}')])]), Element('li', position=Position(Point(20, 20), Point(20, 18)), attributes={'@else': True}, children=[Literal('text', 'Loop fallback')])]), Element('Markdown', position=Position(Point(20, 23), Point(28, 42)), attributes={'src': 'tests/src/readme.md', 'extras': 'footnotes', ':configs': "{\n            'footnotes': {\n              'BACKLINK_TEXT': '$'\n            }\n          }"}, children=None)])]), Literal('comment', 'Extra comment at end of file'), Literal('text', 'Extra text at end of file')])