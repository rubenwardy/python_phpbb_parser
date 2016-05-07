import __init__ as parser

profile = parser.get_profile("https://forum.minetest.net", "rubenwardy")

if profile:
	print(profile.signature.text)
	print(profile.get("github"))
else:
	print("Could not get profile!")
