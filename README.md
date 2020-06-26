# KAAS

Parse PSD1 into python objects

Example:

```python
    >>> P = Parser()
    >>> P.parse_text("@{ VAR = 1}")
    {'VAR': 1}
    >>> P.parse_text('@( 1 @{ V = @{} Q = @{} } )')
    [1, {'V': {}, 'Q': {}}]
```

Requires `pyleri`.
