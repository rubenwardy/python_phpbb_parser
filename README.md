# Python-PhpBB-Parser

## Profiles

```Python
import phpbb_parser as parser
profile = parser.get_profile("https://forum.minetest.net", "rubenwardy")
```

Signature is a BeautifulSoup object.

```Python
print(profile.signature.text)
```

Properties are pure text

```Python
print(profile.get("github"))
```

Keys are lowercase.

## Topics

TODO: no support yet
