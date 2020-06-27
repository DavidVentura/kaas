from kaas.parser import Parser

import pytest

p = Parser()

@pytest.mark.parametrize("test_input,expected", [
    ("@{ VAR = 1}", {'VAR': 1}),
    ("@{}", {}),
    ("@{ VAR = @{} }", {'VAR': {}}),
    ("@{ VAR = @() }", {'VAR': []}),
    ("@{ VAR = @( $False $True ) }", {'VAR': [False, True]}),
    ("@{ VAR = 'hi' }", {'VAR': 'hi'}),
    ("@{ VAR = '' B = 1 }", {'VAR': '', 'B': 1}),
    ('@{ VAR = @( @() @() ) }', {'VAR': [ [], [] ]}),
    ('@{ VAR = @{ V = @{} Q = @{} } }', {'VAR': { 'V': {}, 'Q': {}}}),
    ('@( 1 @{ V = @{} Q = @{} } )', [1, { 'V': {}, 'Q': {}}]),
    ])
def test_parser(test_input, expected):
    assert p.parse_text(test_input) == expected
