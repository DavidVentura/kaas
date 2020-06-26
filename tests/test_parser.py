from parser import Parser
def test_parser():
    P = Parser()
    assert P.parse_text("@{ VAR = 1}") == {'VAR': 1}
    assert P.parse_text("@{}") == {}
    assert P.parse_text("@{ VAR = @{} }") == {'VAR': {}}
    assert P.parse_text("@{ VAR = @() }") == {'VAR': []}
    assert P.parse_text("@{ VAR = @( $False $True ) }") == {'VAR': [False, True]}
    assert P.parse_text("@{ VAR = 'hi' }") == {'VAR': 'hi'}
    assert P.parse_text("@{ VAR = '' B = 1 }") == {'VAR': '', 'B': 1}
    assert P.parse_text('@{ VAR = @( @() @() ) }') == {'VAR': [ [], [] ]}
    assert P.parse_text('@{ VAR = @{ V = @{} Q = @{} } }') == {'VAR': { 'V': {}, 'Q': {}}}
    assert P.parse_text('@( 1 @{ V = @{} Q = @{} } )') == [1, { 'V': {}, 'Q': {}}]
