# python datatype.py
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
# Text Type
from pickle import TRUE
from typing import Type

strType = "This is string"
# Numeric Types
intType = 7
floatType = 7.8
complexType = 5-9j
# Sequence Types
listType = ["Huy", "Nhan", "Trong"]
tupleType = ("Huy", "Nhan", "Trong")
rangeType = range(10)
# Mapping Type
dictType = {"Huy": "Nhan", "Trong": 36}
# Set Types
setType = {"Huy", "Nhan", "Trong"}
frozensetType = frozenset({"Huy", "Nhan", "Trong"})
# Boolean Type
boolType = True
# Binary Types
byteType = b"Huy"
bytearrayType = bytearray(10)
memoryviewType = memoryview(bytes(10))
# None Type
NoneType = None
# using keyword type to check datatype
print(NoneType)
print(type(NoneType))
