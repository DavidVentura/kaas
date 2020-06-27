# KAAS

Parse PowerShell data files (psd1) into python objects

Example:

```python
>>> P = Parser()
>>> P.parse_text("@{ VAR = 1}")
{'VAR': 1}
>>> P.parse_text('@( 1 @{ V = @{} Q = @{} } )')
[1, {'V': {}, 'Q': {}}]
```

Requires `pyleri`.

The package also contains a very small utility, `psd2json`, that can be used to convert files to json:

```bash
$ psd2json file.psd1
{                                                                          
    "AllNodes": [                                                          
        {                                                                  
            "CertificateId": "",                                           
            "ConfigurationMode": "ApplyAndMonitor"
	 }]
}
```
